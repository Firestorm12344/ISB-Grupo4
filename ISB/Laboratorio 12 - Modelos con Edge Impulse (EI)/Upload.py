import numpy as np
import glob
import os
import time
import hmac
import hashlib
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Cargamos los archivos
path = "ECG"  # Ruta de los archivos
files = glob.glob(os.path.join(path, "*.txt"))

if not files:
    raise FileNotFoundError(f"No se encontraron archivos .txt en el directorio: {path}")

def read_emg_file(file_path):
    return np.loadtxt(file_path)

# Ventanear la señal en segmentos de dos segundos
def window_signal(signal, window_size, sample_rate):
    window_samples = int(window_size * sample_rate)
    return [signal[i:i + window_samples] for i in range(0, len(signal), window_samples) if len(signal[i:i + window_samples]) == window_samples]

# Función para subir los datos a Edge Impulse
def upload_ei(name_label, values, hmac_key, api_key, endpoint):
    HMAC_KEY = hmac_key
    API_KEY = api_key
    emptySignature = ''.join(['0'] * 64)
    Fs = 1000  
    Ts = (1 / Fs) * 1000

    data = {
        "protected": {
            "ver": "v1",
            "alg": "HS256",
            "iat": time.time()
        },
        "signature": emptySignature,
        "payload": {
            "device_name": "ac:87:a3:0a:2d:1b",
            "device_type": "NANO33BLE",
            "interval_ms": Ts,
            "sensors": [{"name": "Channel_5", "units": "adu/mv"}],
            "values": values.tolist()
        }
    }

    encoded = json.dumps(data)
    signature = hmac.new(bytes(HMAC_KEY, 'utf-8'), msg=encoded.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
    data['signature'] = signature
    encoded = json.dumps(data)

    res = requests.post(
        url=endpoint,
        data=encoded,
        headers={
            'Content-Type': 'application/json',
            'x-file-name': name_label,
            'x-api-key': API_KEY
        }
    )
    if res.status_code == 200:
        print('Uploaded file to Edge Impulse', res.status_code, res.content)
    else:
        print('Failed to upload file to Edge Impulse', res.status_code, res.content)


# Configuración de HMAC_KEY y API_KEY
HMAC_KEY = "42ff517b9defd1aba74a79cfaf64507c"  # Tu HMAC Key
API_KEY = "ei_d696e62d34a51c185519c739215e649bb6314a357e44e90338be9f614a105fb8"  # Tu API Key

# Etiquetas de los archivos
labels = ["ejercicio", "reposo"]

# Procesar y subir cada archivo por separado
sample_rate = 1000  # Frecuencia de muestreo en Hz
window_size = 2  # Tamaño de la ventana en segundos

for file, label in zip(files, labels):
    signal = read_emg_file(file)
    
    # Seleccionar solo el canal 6
    channel_5_signal = signal[:, 6]  # Canal 5 (índice 4)
    
    # Convertir la señal a DataFrame
    df_signal = pd.DataFrame(channel_5_signal, columns=["Channel_5"])
    
    # Ventanear la señal
    windows = window_signal(df_signal.values, window_size, sample_rate)
    
    # Dividir las ventanas en conjuntos de entrenamiento y prueba (80%-20%)
    train_size = int(0.8 * len(windows))
    train_windows = windows[:train_size]
    test_windows = windows[train_size:]
    
    # Subir las ventanas de entrenamiento
    for window in train_windows:
        upload_ei(label, window, HMAC_KEY, API_KEY, 'https://ingestion.edgeimpulse.com/api/training/data')
    
    # Subir las ventanas de prueba
    for window in test_windows:
        upload_ei(label, window, HMAC_KEY, API_KEY, 'https://ingestion.edgeimpulse.com/api/testing/data')

# Visualización de las señales
for file, label in zip(files, labels):
    signal = read_emg_file(file)
    
    # Seleccionar solo el canal 6
    channel_5_signal = signal[:, 6]  # Canal 5 (índice 4)
    
    # Convertir la señal a DataFrame
    df_signal = pd.DataFrame(channel_5_signal, columns=["Channel_5"])
    
    # Ventanear la señal
    windows = window_signal(df_signal.values, window_size, sample_rate)
    
    train_size = int(0.8 * len(windows))
    train_windows = windows[:train_size]
    test_windows = windows[train_size:]
    
    for i, window in enumerate(train_windows):
        plt.plot(window)
        plt.title(f"{label} - Training {i}")
        plt.grid(ls=":")
        plt.show()

    for i, window in enumerate(test_windows):
        plt.plot(window)
        plt.title(f"{label} - Test {i}")
        plt.grid(ls=":")
        plt.show()

# Análisis de los archivos leídos
df_aux = {
    "name": [os.path.basename(file) for file in files],
    "value": [len(read_emg_file(file)) for file in files]
}


