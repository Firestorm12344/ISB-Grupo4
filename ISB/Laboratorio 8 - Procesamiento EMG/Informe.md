# Lab 8 - Procesamiento EMG

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
La electromiografía de superficie (sEMG) es una técnica ampliamente utilizada en diversos campos como aplicaciones clínicas ya que nos arroja una señal eléctrica conocida como señal mioeléctrica generada a partir de los músculos esqueléticos lo que incluye información importante respecto a la contracción muscular [1]. Sin embargo, la calidad de esta señal puede verse alterada por diversos tipos de ruido como la interferencia y los artefactos lo que puede llevar a una interpretación errónea de esta [2]. Dentro de estos tenemos ruido inherente (de parte de otros equipos electrónicos), ruido ambiental, contaminación cruzada por parte de otros músculos activos cercanos al músculo esquelético de interés, entre otros [1]. Por ende, para obtener la señal EMG se debe tomar en cuenta las características adecuadas que se deben extraer de la señal tanto en el dominio del tiempo, de la frecuencia o del tiempo-frecuencia ya que de tomar un enfoque incorrecto también se puede alterar la señal real [1]. En síntesis, la extracción de características en sEMG es el primer paso en el procesamiento de la señal y se utiliza para remover el ruido y obtener la señal real [1]. La extracción de características en el dominio del tiempo presenta el comportamiento de la señal en este y es utilizado en una amplia gama de aplicaciones como sistemas biológicos debido a que ofrece una reducción respecto a la complejidad relacionada a la extracción de características y facilidad de implementación [1]. Dentro de estas características se encuentran el valor de la media absoluta (MAV), la pendiente del valor de la media absoluta (MAVS), entre otros [1]. Cabe resaltar que esta señal es no estacionaria aunque al ser analizada en el dominio del tiempo se suele asumir que sí lo que conlleva ciertos problemas [1]. Una de las técnicas más utilizadas satisfactoriamente para el análisis de las señales no estacionarias como esta es la transformada de wavelet discreta en el dominio del tiempo aunque esta implica un vector de características de múltiples dimensiones lo que causa un aumento en los parámetros para la clasificación por lo que se debe reducir la dimensionalidad de dicho vector preservando la precisión de la clasificación de características [3]. 
</p>

<p align="justify">
Para la práctica se utilizó el programa Python para aplicar el filtro seleccionado, graficar la señal y extraer sus características. 
</p>

## Metodología


### Diseño del Filtro EMG

<p align="justify">
Las señales de EMG suelen ser adquiridas junto a ruido (ruido de base, ruido de interferencia, ruido de artefactos, etc.), el cual, dependiendo de su naturaleza, puede tener efecto tanto en el dominio del tiempo como la frecuencia [2]. El artículo “Reducing Noise, Artifacts and Interference in Single-Channel EMG Signals: A Review” [2] sugiere que, debido a la variedad de características de cada posible contaminante dentro de la señal, no es posible identificar un método único de filtrado que funcione bien para todos los tipos de contaminantes o ruidos. Dicho artículo menciona características de diversos filtros que son capaces de filtrar el ruido y reconstruir la señal, garantizando la conservación de la mayor cantidad posible de información contenida en la señal EMG; entre ellos menciona el filtro Wavelet y resalta la capacidad de adaptabilidad de sus parámetros basado en las características de la señal. 

Para la determinación del mejor filtro, se optó por comparar los filtros ya utilizados (IIR, FIR y Wavelet). Para ello, un parámetro a considerar será la relación señal/ruido (SNR) de las señales obtenidas luego de cada filtro respectivo. 

| Filtro IIR - Butterworth | Filtro FIR | Filtro Wavelet |
|:--------------:|:--------------:| :--------------:|
| Figura 1 | Figura 2 | Figura 3 |
| <img src="image-1.png" alt="alt text" width="400" height="200"> |<img src="image-2.png" alt="alt text" width="400" height="200">  | <img src="image.png" alt="alt text" width="400" height="200">|
| SNR = 2.3529 | SNR = -2.4112 | SNR = 8.7686 |

Luego de los cálculos respectivos, se observa que la señal con un SNR más alto es la señal obtenida tras el uso del filtro Wavelet, lo cual indica una mayor atenuación del ruido en comparación a los otros filtros.

El artículo “MUAP extraction and classification based on wavelet transform and ICA for EMG decomposition” [4], presenta el uso de un filtro wavelet frente a los filtros digitales comunes, debido a que sugiere que estos último pueden causar demoras en el dominio del tiempo (time-delay). Para el filtrado de la señal EMG, se adoptarán los parámetros utilizados por este artículo: 
- Tipo de wavelet: Daubechies 5 (db5)
- Nivel de la wavelet: 9
- Threshold: Hard.
</p>

### Segmentación

<p align="justify">
Un segmento es una secuencia de datos dada en un intervalo de tiempo y se utiliza para la extracción de las características de la señal [5]. Por ende, al tomar segmentos tantos cortos como largos se pueden generar inconvenientes como sesgo y varianza en la estimación de dichas características y también limitación computacional sobretodo en aplicaciones en tiempo real  [5]. Asimismo, se debe tomar en cuenta el tiempo de procesamiento al momento de escoger la longitud del segmento [5]. Existen dos métodos de segmentación conocidos como segmentación disjunta y segmentación superpuesta siendo esta última la que demanda una mayor carga computacional [5]. Para la segmentación de la señal en este trabajo utilizamos el método de segmentación disjunta con segmentos cada 200 ms ya que es el intervalo mínimo entre dos contracciones distintas en los músculos de la mano por lo que un segmento de este tamaño contiene información suficiente para estimar el movimiento en estos sin exceder las limitaciones computacionales presentadas [5]. 
</p>

### Extracción de características

<p align="justify">
La segmentación se llevó a cabo mediante ventanas de 200 ms (200 muestras) en los periodos de 0 a 20s, que corresponde a la etapa de reposo, y de 40 a 70s, que refiere a la etapa en excitación. 
</p>

<p align="justify">
Los parámetros a temporales a considerar, tal como N. Burhan et al [6], son el Valor Medio Absoluto (MAV), Raiz Cuadrada Media (RMS), Valor Medio Absoluto de Pendiente (MAVS), Varianza, señal EMG integrado (iEMG), Longitud de forma de onda (WL), Intersecciones con cero (ZC) y Cambio de Signo de la Señal (SSC). Del mismo artículo, se menciona que el análisis frecuencial se debe realizar mediante parámetros como la Densidad de Potencia Espectral (PSD), Frecuencia Promedio y Frecuencia Mediana. Sin embargo, adicional a la PSD, se compara el espectro de Fourier antes y después del filtro empleado 
</p>

<p align="justify">
Cabe resaltar que para la extracción de características se eliminó a partir de filtrado digital  el componente DC de la señal el cual puede surgir en la conversión A/D debido a inexactitudes en el convertidor y puede repercutir en algoritmos de procesamiento de señales [7]. 
</p>


## Resultados

***NOTA**: El ploteo de las señales se realizó en intervalos distintos, para una mejor apreciación de las señales. Asimismo, la frecuencia de muestreo fue de 1000 Hz.*

### EMG

Los resultados analizados en la siguiente tabla se obtuvieron al realizar el EMG del bíceps. 
Los electrodos fueron colocados como se observa en la figura 1. Los electrodos positivo y negativo será colocados en el músculo de interés, en este caso el bíceps mientras que el electrodo de referencia será colocado en una zona neutra como la muñeca.
Se tomó registro de la señal en el usuario en estado de reposo o silencio eléctrico y realizando la contracción muscular.

| Posicionamiento de los electrodos |
|:--------------:|
| <img src="image-1-1.png" alt="Descripción de la imagen" width="300"/> |
| Figura 4 |


| Campo | Señal Cruda | Filtro wavelet | 
|:--------------:|:--------------:|:--------------:|
| Figura 5. Señal completa| ![alt text](image-3.png) | ![alt text](image-4.png) |
| Figura 6. Reposo | ![alt text](image-5.png)| ![alt text](image-6.png)| 
| Figura 7. Contracción muscular | ![alt text](image-7.png) | ![alt text](image-8.png)|

| FFT señal cruda | FFT señal filtrada | 
|:--------------:|:--------------:|
| ![alt text](image-9.png) | ![alt text](image-10.png)| 
| FIgura 8 | Figura 9 | 

| PSD señal cruda | PSD señal filtrada | 
|:--------------:|:--------------:|
| ![alt text](image-11.png) | ![alt text](image-12.png)| 
| Figura 10 | Figura 11 | 

| Parámetros de frecuencia | Valor en reposo (Hz) | Valor en exitación (Hz) |
|:--------------:|:--------------:|:--------------:|
|  Frecuencia pico | 1.0 | 21.433 |
|  Mediana | 0.00018 |  0.1231 |
| Promedio  | 1.9076 | 77.465 |


| Parámetros de tiempo | Valor en reposo | Valor en exitación |
|:--------------:|:--------------:|:--------------:|
| Mean Absolute Value | 6.3*10^-5 | 0.0361 |
| Root Mean Square | 0.00016 | 0.0496 |
| Mean Absolute Value Slope  | 1.8175 |  0.0159|
| Variance | 2.0411 | 0.0063 |
| iEMG | 7337.02 | 7337.015 |
|  Waveform Length (WL)| 153449 | 153449 |
| Zeros Crosses (ZC) | 29410 | 29410 |
| Sign Signal Change (SSC) | 72504 | 72504 |


## Código en Python


### Librerías

``` python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pywt
from scipy import signal
from scipy.signal import lfilter, firwin

```

### Funciones Generales

``` python

def get_values(path, col):
  df = pd.read_csv(path, sep='\t', skiprows=3)  # saltar las dos primeras filas (encabezado)
  novena_columna = df.iloc[:, col].values
  n = [i/1000 for i in range(0, len(novena_columna))]
  signal = [(float(valor)/(2**10)-1/2)*3.3/1009*1000 for valor in novena_columna]
  return n, signal


def plot_values(n, y, label, ini, fin):
  plt.plot(n[ini:fin], y[ini:fin])
  plt.xlabel('Tiempo (s)')
  plt.ylabel('Voltaje (mv)')
  plt.title(label)
  plt.grid(True)
  plt.show()


def FreqAnalysis_FFT (signal):
  global fs
  fs = 1000
  fft_result = np.fft.fft(signal)
  freqs = np.fft.fftfreq(len(signal), 1/fs)
  # Graficar la magnitud de la FFT
  plt.figure(figsize=(10, 5))
  plt.plot(freqs, np.abs(fft_result))
  plt.xlim(-600, 600)
  plt.title('Magnitud de la Transformada Rápida de Fourier (FFT)')
  plt.xlabel('Frecuencia (Hz)')
  plt.ylabel('Magnitud')
  plt.grid(True)
  plt.show()
  return fft_result

```

### Funciones para Filtros


```python

def WaveletFiltering(signal, ini, fin):
    coeffs = pywt.wavedec(signal, 'db5', level=9)
    # sigma = np.median(coeffs[-1])/0.6745
    # print(sigma)
    # thresh = sigma*np.sqrt(2*np.log10(len(signal)))
    # print(thresh)
    # Filtrar los coeficientes
    threshold = 0.2
    filtered_coeffs = [pywt.threshold(coeff, threshold, mode='hard') for coeff in coeffs]

    # Reconstruir la señal filtrada
    filtered_signal = pywt.waverec(filtered_coeffs, 'db5')
    plt.figure()
    plt.plot(signal[ini:fin], label='Señal original')
    plt.plot(filtered_signal[ini:fin], label='Señal filtrada')
    plt.title('Señal filtrada')
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.ylim([-1.2, 1.2])
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return filtered_signal

def IIR_Butter(EMGsignal, ini, fin):
  b,a = signal.butter(2, 10, 'highpass', fs=1000, output='ba')
  filteredEMG =signal.filtfilt(b,a, EMGsignal)
  b,a = signal.butter(8, 400, 'lowpass', fs=1000, output='ba')
  filteredEMG =signal.filtfilt(b,a, filteredEMG)
  b,a = signal.butter(2, [40, 80], 'stop', fs=1000, output='ba')
  filteredEMG =signal.filtfilt(b,a, filteredEMG)
  b,a = signal.butter(2, [100, 140], 'stop', fs=1000, output='ba')
  filteredEMG =signal.filtfilt(b,a, filteredEMG)
  b,a = signal.butter(2, [160, 200], 'stop', fs=1000, output='ba')
  filteredEMG =signal.filtfilt(b,a, filteredEMG)
  b,a = signal.butter(2, [220, 260], 'stop', fs=1000, output='ba')
  filteredEMG =signal.filtfilt(b,a, filteredEMG)
  b,a = signal.butter(2, [280, 320], 'stop', fs=1000, output='ba')
  filteredEMG =signal.filtfilt(b,a, filteredEMG)
  b,a = signal.butter(2, [340, 380], 'stop', fs=1000, output='ba')
  filteredEMG =signal.filtfilt(b,a, filteredEMG)
  plt.figure()
  plt.plot(EMGsignal[ini:fin], label='Señal original')
  plt.plot(filteredEMG[ini:fin], label='Señal filtrada')
  plt.title('Señal filtrada')
  plt.xlabel('Tiempo')
  plt.ylabel('Amplitud')
  plt.ylim([-1.2, 1.2])
  plt.legend()
  plt.grid(True)
  plt.tight_layout()
  plt.show()
  return filteredEMG

def FIR(EMGsignal, ini, fin):
  n = [i/1000 for i in range(0,len(EMGsignal))]
  t = [num / fs for num in n]; N=len(n)
  M = 37
  Fc = 30
  wc = 2*np.pi*Fc/fs
  w = firwin(numtaps=M, cutoff=Fc, window='hamming', fs=1000, pass_zero=False)
  w = np.round(w,3)
  nm = np.arange(M)
  W = np.fft.fft(w,N)
  W = np.round(W[0:N//2],3)
  y_filtrado = lfilter(w, np.array(1),EMGsignal)
  plt.figure()
  plt.plot(n[ini: fin], EMGsignal[ini: fin], label="Señal Original")
  plt.plot(n[ini: fin], y_filtrado[ini: fin], label="Señal Filtrada")
  plt.ylabel("Amplitud (mv)")
  plt.xlabel("Tiempo (s)")
  plt.title("EMG")
  plt.legend()
  plt.grid(True)
  plt.margins(0, 0.05)
  return y_filtrado



def SNR(signal, filtered_signal):
    power_signal = np.mean(np.square(signal))
    noise = signal - filtered_signal
    power_noise = np.mean(np.square(noise))
    snr = 10 * np.log10(power_signal / power_noise)
    return snr

```

### Funciones de Segmentación

```python

def split_signal(signal, N):
    num_segments = len(signal) // N  # Número de pedazos completos
    segments = [signal[i*N:(i+1)*N] for i in range(num_segments)]
    return segments

# Selección de segmentos de señal en etapas de reposo y exitación
# Tiempo de reposo 0 a 20 s
# Tiempo de exitación de 40 a 70 s

signalSet = split_signal(EMGsignal_NoDC, 200)
restSegments = signalSet[0:100]
excitementSegments = signalSet[200:350]

```

### Funciones de Características en Tiempo

``` python

def timeChar(segments):
  mavlist = []
  rmslist = []
  mavslist = []
  varlist = []
  iemglist = []
  wllist = []
  zclist = []
  ssclist = []
  for EMGsignal in segments:
    mav = np.mean(np.abs(EMGsignal))
    rms = np.sqrt(np.mean(np.square(EMGsignal)))
    mavs = np.mean(np.abs(np.diff(EMGsignal)))
    var = np.var(EMGsignal)

    # Calcular el iEMG (integral de la EMG)
    iemg_value = np.sum(np.abs(EMGsignal_NoDC))
    # Calcular la longitud de la forma de onda (WL)
    wl_value = len(EMGsignal_NoDC)
    # Calcular los cruces por cero (ZC)
    zc_value = np.sum(np.diff(np.sign(EMGsignal_NoDC)) != 0)
    # Calcular los cambios en el signo de la pendiente (SSC)
    ssc_value = np.sum(np.diff(np.sign(np.diff(EMGsignal_NoDC))) != 0)
    mavlist.append(mav)
    rmslist.append(rms)
    mavslist.append(mavs)
    varlist.append(var)
    iemglist.append(iemg_value)
    wllist.append(wl_value)
    zclist.append(zc_value)
    ssclist.append(ssc_value)

    mav_mean = np.mean(mavlist)
    rms_mean = np.mean(rmslist)
    mavs_mean = np.mean(mavslist)
    var_mean = np.mean(varlist)
    iemg_mean = np.mean(iemglist)
    wl_mean = np.mean(wllist)
    zc_mean = np.mean(zclist)
    ssc_mean = np.mean(ssclist)

  print("Mean Absolute Value: ", mav_mean)
  print("Root Mean Square: ", rms_mean)
  print("Mean Absolute Value Slope: ", mavs_mean)
  print("Variance: ", var_mean);
  print("iEMG:", iemg_value)
  print("Waveform Length (WL):", wl_value)
  print("Zeros Crosses (ZC):", zc_value)
  print("Sign Signal Change (SSC):", ssc_value) 


def wavelength(signal):
  n = [i for i in range(0, len(signal))]
  t = n/1000
  peak_indices = np.where(np.diff(np.sign(np.diff(signal))) < 0)[0]
  # Calcular la longitud de onda como la distancia entre dos picos consecutivos
  if len(peak_indices) >= 2:
      wavelength = t[peak_indices[1]] - t[peak_indices[0]]
      print("Longitud de onda:", wavelength)
  else:
      print("No se encontraron suficientes picos para calcular la longitud de onda.")

timeChar(restSegments)
timeChar(excitementSegments)

```

### Funciones de Características en Frecuencia

```python

def freqChar(segments):
    peakFreqlist = []
    medFreqlist = []
    avgFreqlist = []
    
    for signal in segments:
        freqs = np.fft.fftfreq(len(signal), 1/1000)
        fft_spectrum = np.fft.fft(signal)
        magnitude_spectrum = np.abs(fft_spectrum)
        
        # Encontrar la frecuencia pico
        peak_freq_index = np.argmax(magnitude_spectrum)
        peakFreq = freqs[peak_freq_index]
        
        # Calcular frecuencias positivas
        positive_freqs = freqs[freqs >= 0]
        positive_magnitude = magnitude_spectrum[freqs >= 0]

        # Calcular promedio ponderado de magnitudes por frecuencias
        if (np.sum(positive_magnitude)==0):
          avgFreq = 0
        else:
          avgFreq = np.sum(positive_magnitude * positive_freqs) / np.sum(positive_magnitude)
        
        # Calcular mediana de las magnitudes del espectro de frecuencia
        medFreq = np.median(positive_magnitude)
        
        peakFreqlist.append(peakFreq)
        medFreqlist.append(medFreq)
        avgFreqlist.append(avgFreq)
    mPeak = np.mean(peakFreqlist)
    mMed = np.mean(medFreqlist)
    mAvg = np.mean(avgFreqlist)
    
    print("Peak Frequency: ", mPeak)
    print("Median Frequency: ", mMed)
    print("Mean Frequency: ", mAvg)

def Periodogram(signal):
  powSpectralDensity = abs(np.fft.fft(signal))**2
  freqs = np.fft.fftfreq(len(signal), 1/fs)
  plt.plot(freqs, powSpectralDensity)
  plt.title('Power Spectral Density')
  plt.xlabel('Frecuencia')
  plt.ylabel('Potencia')
  plt.legend()
  plt.grid(True)
  plt.show()
  return 

freqChar(restSegments)
freqChar(excitementSegments)

```

## Discusión de resultados
<p align="justify">
El análisis comparativo de diferentes filtros (IIR, FIR y Wavelet) mostró que el filtro Wavelet, específicamente con la wavelet Daubechies 5 (db5) y un nivel de wavelet de 9, proporciona la mejor relación señal/ruido (SNR). Esto indica que el filtro Wavelet es más efectivo para atenuar el ruido y preservar la integridad de la señal EMG en comparación con los filtros digitales comunes. La capacidad del filtro Wavelet para adaptarse a las características específicas de la señal EMG, sin introducir demoras significativas en el dominio del tiempo, lo convierte en una opción superior para el procesamiento de señales no estacionarias como la sEMG. Asimismo, la segmentación de la señal utilizando ventanas de 200 ms demostró ser una estrategia eficaz para capturar la información relevante de la actividad muscular. Este enfoque permitió la extracción precisa de características temporales y frecuenciales durante las etapas de reposo y excitación. Los parámetros extraídos, como el Valor Medio Absoluto (MAV), la Raíz Cuadrada Media (RMS), y la Densidad de Potencia Espectral (PSD), proporcionaron una visión clara de las diferencias en la actividad muscular entre los estados de reposo y excitación, destacando la importancia de seleccionar adecuadamente tanto el método de filtrado como la técnica de segmentación para el análisis de señales sEMG. 
</p>

<p align="justify">
Primero, respecto a las características en frecuencia, estas son esenciales para entender la distribución de energía de la señal EMG en diferentes estados de actividad muscular. La frecuencia pico, la cual representa el componente de frecuencia con la mayor energía, muestra un incremento significativo de 1.0 Hz en reposo a 21.433 Hz en excitación, indicando un aumento en la actividad muscular. La frecuencia mediana, que es el punto donde la mitad de la energía del espectro está por debajo de esta frecuencia, también aumenta de 0.00018 Hz en reposo a 0.1231 Hz en excitación, sugiriendo un desplazamiento de la energía hacia frecuencias más altas durante la contracción muscular. El promedio de las frecuencias es notablemente mayor en el estado de excitación (77.465 Hz) en comparación con el reposo (1.9076 Hz), reflejando una mayor actividad y complejidad de la señal durante la excitación. 
</p>

<p align="justify">
Por otro lado, respecto a las características en tiempo, estas proporcionan información directa sobre las características estadísticas de la señal EMG en diferentes estados. El Valor Medio Absoluto (MAV) y la Raíz Cuadrada Media (RMS aumentan significativamente durante la excitación (MAV: 0.0361, RMS: 0.0496) en comparación con el reposo (MAV: 6.3*10^-5, RMS: 0.00016), reflejando un aumento en la amplitud de la señal durante la contracción muscular. La Pendiente del Valor Medio Absoluto (MAVS), que mide el cambio en la amplitud de la señal, muestra un incremento durante la excitación, aunque en menor medida que otros parámetros. La varianza, que mide la dispersión de los valores de la señal, es mayor en reposo (2.0411) que en excitación (0.0063), lo cual podría indicar una mayor estabilidad de la señal durante la contracción. El iEMG, que es una medida acumulativa de la actividad eléctrica, permanece casi constante, indicando que la actividad total no varía significativamente entre los estados, aunque la intensidad y la frecuencia de las contracciones sí lo hacen. Por último, La Longitud de la Forma de Onda (WL), las Intersecciones con Cero (ZC), y el Cambio de Signo de la Señal (SSC) permanecen constantes entre los estados, sugiriendo que estos parámetros pueden no ser sensibles a las diferencias entre reposo y excitación en este contexto específico.
</p>

## Referencias

1. Burhan N, Kasno MA, Ghazali R. Feature extraction of surface electromyography (sEMG) and signal processing technique in wavelet transform: A review. En: 2016 IEEE International Conference on Automatic Control and Intelligent Systems (I2CACIS) [Internet]; 22 de octubre de 2016; Selangor, Malaysia. [lugar desconocido]: IEEE; 2016 [consultado el 26 de mayo de 2024]. Disponible en: https://doi.org/10.1109/i2cacis.2016.7885304
2. Boyer M, Bouyer L, Roy JS, Campeau-Lecours A. Reducing Noise, Artifacts and Interference in Single-Channel EMG Signals: A Review. Sensors [Internet]. 8 de marzo de 2023 [consultado el 26 de mayo de 2024];23(6):2927. Disponible en: https://doi.org/10.3390/s23062927
3. Phinyomark A, Nuidod A, Phukpattaranont P, Limsakul C. Feature Extraction and Reduction of Wavelet Transform Coefficients for EMG Pattern Classification. Electron Electr Eng [Internet]. 11 de junio de 2012 [consultado el 26 de mayo de 2024];122(6). Disponible en: https://doi.org/10.5755/j01.eee.122.6.1816
4. X. Ren, X. Hu, Z. Wang, y Z. Yan, “MUAP extraction and classification based on wavelet transform and ICA for EMG decomposition”, Med. Biol. Eng. Comput., vol. 44, núm. 5, pp. 371–382, 2006. DOI: 10.1007/s11517-006-0051-3
5. Oskoei MA, Huosheng Hu. Support Vector Machine-Based Classification Scheme for Myoelectric Control Applied to Upper Limb. IEEE Trans Biomed Eng [Internet]. Agosto de 2008 [consultado el 26 de mayo de 2024];55(8):1956-65. Disponible en: https://doi.org/10.1109/tbme.2008.919734
6. N. Burhan, M. Kasno, y R. Ghazali, “Feature extraction of surface electromyography (sEMG) and signal processing technique in wavelet transform: A review”, en 2016 IEEE International Conference on Automatic Control and Intelligent Systems (I2CACIS), 2016, pp. 141–146.
7. Stranak P. Interfering DC Component, Suppression and Influence to Digital Signal Processing. Radioengineering [Internet]. 2008 [consultado el 25 de mayo de 2024];17:121-3. Disponible en: https://dspace.vut.cz/items/5a34027c-d5f1-4d26-a13c-15c47d8f02ad/full
</div>
