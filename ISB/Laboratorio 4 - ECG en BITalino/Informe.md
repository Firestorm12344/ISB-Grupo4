# Lab 4 - ECG con BiTalino

## Tabla de contenidos
- [Objetivos](#objetivos)
- [Materiales](#materiales)
- [Introducción](#introducción)
- [Conexión utilizada](#Conexión-utilizada)
- [Procedimiento](#Procedimiento)
- [Prueba 1](#Prueba-1)
- [Prueba 2](#Prueba-2)
- [Referencias](#referencias)
  
##  Objetivos
- Adquirir señales biomédicas de ECG.
- Hacer una correcta configuración de BiTalino.
- Extraer la información de las señales ECG de software OpenSignals (r)evolution.

## Materiales
| Material | Cantidad |
|--------------|--------------|
| Kit BiTalino    | 1    |
| ProSim 4 Vital Signs Simulator | 1    |
| Laptop    | 1    |
| Electrodos    | 3    |

## Marco Teórico

El electrocardiograma(ECG) es un procedimiento utilizado para evaluar la actividad eléctrica del corazón ya que nos permite diagnosticar anomalías en él como por ejemplo las arritmias [1]. Dichas anomalias pueden desencadenar eventos mortales como el infarto al miocardio por lo que una interpretación adecuada es de suma importancia para la prevención de enfermedades cardiacas [1]. 
Esta prueba muestra la variación en el tiempo de potenciales bioeléctricos que se dan en el corazón cuando este late [1]. Usualmente se utilizan las 12 derivaciones cuya interpretación es mas compleja. Sin embargo, en el presente laboratorio utilizamos unicamente derivaciones bipolares estándares por lo que utilizamos dos electrodos para detectar el potencial bioeléctrico
así como un electrodo de referencia a diferencia de un ECG con 12 derivaciones en el cual se utilizan 12 electrodos y su utilidad esta mas enfocada al diagnóstico de infartos e isquemias miocárdicas [3].

Respecto a las derivaciones bipolares, son derivaciones periféricas clásicas que nos permiten evaluar diferentes orientaciones de la actividad eléctrica del corazón. De esta manera, las derivaciones tienen un eje de derivación que junta a los polos de esta. Entre ellas existe una relación dada por la ley de Einthoven la cual nos indica que la suma de los voltajes de las derivaciones bipolares I y III nos dará el voltaje en la derivación II [3].

Diversas propuestas se estan desarrollando para permitir una interpretación automátizada del ECG para así aumentar la accesibilidad y precisión a los diagnósticos y por ende tratamientos de enfermedades cardiacas con riesgo de muerte [1]. Entre las propuestas para el procesamiento de estas señales se encuentran métodos de automático como inteligencia artificial (IA) o Machine Learning [1]. 

Para la práctica se utilizó 1 kit BiTalino para la realización de ECG así como unProSim 4 VItal Signs Simulator para simular un ECG según la derivación elegida. El dispositivo de BITalino ECG posee una configuración bipolar, ideal para la adquisición de señales con bajo ruido [2]. Además, se utilizó el software OpenSignals (r)evolution para la adquisición de la señal y los datos para un posterior análisis.

## Conexión utilizada

Primero se utilizó el dispositivo ProSim 4 Vital Signs Simulator, cuya conexión se realizó de tal manera para simular un ECG de tipo derivación III. Para ello, en el punto LL se colocó el electrodo positivo, en el punto LA se colocó el electrodo negativo y en el punto RA se colocó el de referecia (Figura 1 y 2)

![alt text](image.png)
Figura 1. Conexiones en ProSim 4 Vital Signs Simulator
![alt text](image-1.png)
Figura 2. Conexiones en ProSim 4 Vital Signs Simulator y BiTalino

Para la obtención de ECG se utilizó la guía de "BITalino (r)evolution Lab Guide: EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS". Se utilizó la conexión en el puerto A2 en el BiTalino y se realizó la colocación de los electrodos de acuerdo a la derivación I de Einthoven:

* Forma 1 : Colocación del electrodo positivo en la clavícula izquierda, electrodo negativo en la clavícula derecha y electrodo de referencia en la cresta iliaca. Observar figura 3.
* Forma 2: Colocación del electrodo positivo en la muñeca izquierda, electrodo negativo en la muñeca derecha y electrodo de referencia en la cresta iliaca. Observar figura 4.

![alt text](image-3.png)
Figura 3. Colocación de electrodos para la derivación I (forma 1)

![alt text](image-2.png)
Figura 4. Colocación de electrodos para la derivación I (forma 2)

## Procedimiento

Se realizaron 2 mediciones de ECG en diferentes partes del cuerpo y se utilizó el dispositivo ProSim 4 Vital Signs Simulator para simular una secuencia de paro cardiaco

### Prueba con ProSim 4 Vital Signs Simulator

Con la ayuda de el dispositivo ProSim 4, se simuló una parada cardiaca. Esta consiste en una autosecuencia de 2 minutos y 30 segundos con 6 etapas:
1. ECG de 80 lpm (30 s)
2. Contracciones ventriculares prematuras (CVP) del ventrículo izquierdo (30 s)
3. Taquicardia ventricular de 160 lpm (30 s)
4. Fibrilación ventricular severa (30 s)
5. Asistolia (15 s)
6. Parada del corazón (muerte)

Por cuestiones de tiempo en clase, solo se tomó registro en el simulador OpenSignals (r)evolution a partir de la fase 2 a la 6. A continuación se muestran las gráficas obtenidas en cada una de estas fases.


| Fase | Señal obtenida |
|:--------------:|:--------------:|
| Figura 5. Contracciones ventriculares prematuras (CVP) del ventrículo izquierdo   | ![alt text](image-4.png) |
| Figura 6. Taquicardia ventricular de 160 lpm   | ![alt text](image-5.png)   |
| Figura 7. Fibrilación ventricular severa| ![alt text](image-6.png)|
| Figura 8. Asistolia | ![alt text](image-7.png)|
| Figura 9. Parada del corazón (muerte)|![alt text](image-8.png) |


### Prueba ECG 

Para la prueba de electrocardiograma se realizó en 4 estados:
1. En estado de reposo con respiración normal
2. Hiperventilación
3. Después de la realización de ejercicio moderado
4. Luego de respiraciones largas (inhalación por 10 segundos, retención por 10 segundos y exhalación)

Para el estado de reposo se realizó con ambas formas de colocación de electrodos como se observa en la figura 10 y 11. Sin embargo, se observa que 



## Explicación/ Discusión de resultados



##  Ploteo de Python

Para el ploteo de las señales se utilizaron funciones (Archivo: Funciones.py) para realizar el ploteo de la señal (Archivo: Ploteo.py)

``` python

import pandas as pd
import matplotlib.pyplot as plt

def get_values(path):
  df = pd.read_csv(path, sep='\t', skiprows=3)  # saltar las dos primeras filas (encabezado)
  novena_columna = df.iloc[:, 6].values
  n = [i/1000 for i in range(0, len(novena_columna))]
  return n, novena_columna

def plot_values(n, y, label):
  plt.plot(n[1:3000], y[1:3000])

  # Etiquetas y título
  plt.xlabel('Índice')
  plt.ylabel('Valor')
  plt.title(label)

  # Mostrar el gráfico
  plt.show()
  plt.savefig(label+".png")
  
def plot_Customvalues(n, y, label, ini, fin):
  plt.plot(n[ini:fin], y[ini:fin])

  # Etiquetas y título
  plt.xlabel('Índice')
  plt.ylabel('Valor')
  plt.title(label)

  # Mostrar el gráfico
  plt.show()
  plt.savefig(label+".png")

```

- Para el ploteo de la primera señal adquirida, se tiene el siguiente código: 

``` python

from Funciones import *

path = "/content/drive/MyDrive/PUCP/7mo ciclo/Instruducción a Señales Biomédicas/Laboratorios/ECG/RESPIRACION.txt"
[n, y] = get_values(path)
label = "ECG durante respiración"
plot_values(n, y, label)

```

- Para el ploteo de la segunda señal adquirida, se tiene el siguiente código: 

``` python

path = "/content/drive/MyDrive/PUCP/7mo ciclo/Instruducción a Señales Biomédicas/Laboratorios/ECG/POS EJERCICIO.txt"
[n, y] = get_values(path)
label = "ECG Post-Ejercicio"
plot_values(n, y, label)

```

- Para el ploteo de la tercera señal adquirida, se tiene el siguiente código: 

``` python

path = "/content/drive/MyDrive/PUCP/7mo ciclo/Instruducción a Señales Biomédicas/Laboratorios/ECG/HIPER.txt"
[n, y] = get_values(path)
label = "ECG Durante Hiperventilación"
plot_values(n, y, label)

```

- Para el ploteo de la tercera señal adquirida, se tiene el siguiente código: 

``` python

path = "/content/drive/MyDrive/PUCP/7mo ciclo/Instruducción a Señales Biomédicas/Laboratorios/ECG/J1.txt"
[n, y] = get_values(path)
label = "ECG en Estado Basal: Resposo"
inicio = 2600
fin = 4200
plot_Customvalues(n, y, label, inicio, fin)

```


## Referencias

1. Kundu M, Nasipuri M, Kumar Basu D. Knowledge-based ECG interpretation: a critical review. Pattern Recognit [Internet]. Marzo de 2000 [consultado el 19 de abril de 2024];33(3):351-73. Disponible en: https://doi.org/10.1016/s0031-3203(99)00065-5

2. Breen CJ, Kelly GP, Kernohan WG. ECG interpretation skill acquisition: A review of learning, teaching and assessment. J Electrocardiol [Internet]. Abril de 2019 [consultado el 19 de abril de 2024]. Disponible en: https://doi.org/10.1016/j.jelectrocard.2019.03.010

3. www.elsevier.com [Internet]. Interpretación del ECG: Guí­a Esencial para Profesionales Médicos; 12 de junio de 2023 [consultado el 19 de abril de 2024]. Disponible en: https://www.elsevier.com/es-es/connect/electrocardiograma-de-12-derivaciones-derivaciones-y-ejes

