# Lab 8 - Procesamiento ECG

## Tabla de contenidos
- [Objetivos](#objetivos)
- [Materiales](#materiales)
- [Introducción](#introducción)
- [Metolodogía](#metodología)
- [Resultados](#resultados)
- [Discusión de resultados](#Discusión-de-resultados)
- [Referencias](#referencias)


##  Objetivos
- Comparar y seleccionar el filtro mas adecuado para la señal EMG
- Extraer y discutir las características de la señal EMG

## Materiales
| Material | Cantidad |
|:--------------:|:--------------:|
| Programa *Python* | N.A | 

## Introducción

<p align="justify">
</p>

<p align="justify">. 
</p>

## Metodología

### Diseño del Filtro ECG

<p align="justify">
Como parte del pre procesamiento de las señales de ECG, se usará la implementación del filtro Wavelet del laboratorio 7, el cual está toma de referencia el artículo “The Identification of ECG Signals Using WT-UKF and IPSO-SVM” [A], donde la transformada wavelet permite eliminar el ruido presente y, a su vez, preservar las características locales de la señal de ECG. Para el filtro el tipo de Wavelet madre a implementar es Daubechies 8 (db8) con 8 niveles de descomposición y un thresholding suave de 0.2.

[A] N. Li et al., “The identification of ECG signals using WT-UKF and IPSO-SVM”, Sensors (Basel), vol. 22, núm. 5, p. 1962, 2022. doi: 10.3390/s22051962
</p>

### Picos R

<p align="justify">
</p>

<p align="justify">
</p>

### HRV
<p align="justify">
</p>


## Resultados

***NOTA**: El ploteo de las señales se realizó en intervalos distintos, para una mejor apreciación de las señales. Asimismo, la frecuencia de muestreo fue de 1000 Hz.*

### EMG

## Código en Python


### Librerías

``` python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.signal import lfilter, firwin, find_peaks
import pywt
from pyhrv.hrv import hrv
import pyhrv
```

### Funciones Generales

``` python
def get_values(path, col):
  df = pd.read_csv(path, sep='\t', skiprows=3)  # saltar las dos primeras filas (encabezado)
  novena_columna = df.iloc[:, col].values
  n = [i/1000 for i in range(0, len(novena_columna))]
  signal = [(float(valor)/(2**10)-1/2)*3.3/1009*1000 for valor in novena_columna]
  return n, signal

def list_Df(n, signal):
  df = pd.DataFrame(list(zip(n, signal)), index=None, columns=["Time", "Signal"])
  df.to_csv('/content/drive/MyDrive/PUCP/7mo ciclo/Instruducción a Señales Biomédicas/Laboratorios/Tratamiento de ECG/ecg_signal.csv', sep=";")


```

### Funciones para Filtros


```python
def filter_Wavelet(EGGsignal1):
  coeffs = pywt.wavedec(ECGsignal1, 'db8', level=8)
  threshold = 0.2
  filtered_coeffs = [pywt.threshold(coeff, threshold, mode='soft') for coeff in coeffs]
  filtered_signal = pywt.waverec(filtered_coeffs, 'db8')
  return filtered_signal
```

```python

path = "/content/drive/MyDrive/PUCP/7mo ciclo/Instruducción a Señales Biomédicas/Laboratorios/ECG/J1.txt"
[n, ECGsignal1] = get_values(path, 6)
label = "ECG Estado Basal"
new_signal = filter_Wavelet(ECGsignal1)

fs =1000
peaks, properties = find_peaks(new_signal, height=0.05, distance=int(0.5 * fs))
t = [i/fs for i in range(0, len(new_signal))]

plt.figure(figsize=(12, 6))
plt.plot(t, new_signal, label='Filtered ECG Signal')
timeP =[]
peaksonly = []
for i in peaks:
  timeP.append(t[i])
  peaksonly.append(new_signal[i])
  plt.plot(t[i], new_signal[i], 'ro')
plt.title('ECG Signal with Detected Peaks')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()


rr_intervals = np.diff(peaks) / fs 
rr_intervals = rr_intervals[rr_intervals > 0.3]
mean_rr = np.mean(rr_intervals)
std_rr = np.std(rr_intervals)
rmssd = np.sqrt(np.mean(np.diff(rr_intervals)**2))
nn50 = np.sum(np.abs(np.diff(rr_intervals)) > 0.05)
pnn50 = (nn50 / len(rr_intervals)) * 100
print(f"Mean RR: {mean_rr:.4f} s")
print(f"SDNN: {std_rr:.4f} s")
print(f"RMSSD: {rmssd:.4f} s")
print(f"pNN50: {pnn50:.2f} %")

```
