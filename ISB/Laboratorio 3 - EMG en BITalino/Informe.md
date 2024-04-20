# Lab 3 - EMG con BiTalino

## Tabla de contenidos
- [Objetivos](#objetivos)
- [Materiales](#materiales)
- [Introducción](#introducción)
- [Conexión utilizada](#Conexión-utilizada)
- [Procedimiento](#Procedimiento)
- [Prueba 1](#Prueba-1)
- [Prueba 2](#Prueba-2)
- [Prueba 3](#Prueba-3)
- [Referencias](#referencias)
  
##  Objetivos
- Adquirir señales biomédicas de EMG.
- Hacer una correcta configuración de BiTalino.
- Extraer la información de las señales EMG de software OpenSignals (r)evolution.

## Materiales
| Material | Cantidad |
|--------------|--------------|
| Kit BiTalino    | 1    |
| Laptop    | 1    |
| Electrodos    | 3    |

## Introducción

El electromiograma (EMG) es un procedimiento utilizado para la evaluación de la salud muscular y las células nerviosas que intervienen (neuronas motoras). En la electromiografía se utilizan electrodos para traducir las señales eléctricas producidas por las neuronas motoras que generan la contracción muscular. Los electrodos son usados para la medición de la velocidad e intensidad de las señales que se desplazan entre 2 o más puntos [1].

Para la práctica se utilizó 1 kit BiTalino para la realización de EMG. El dispositivo de BITalino EMG posee una configuración bipolar, ideal para la adquisición de señales con bajo ruido [2]. Además, se utilizó el software OpenSignals (r)evolution para la adquisición de la señal y los datos para un posterior análisis.

## Conexión utilizada

Para la adquisición de señales electromiográficas se utilizó la siguiente conexión en BITalino con 3 electrodos

<img src="image.png" alt="Conexiones de BITalino para EMG" width="300" height="300">
Figura 1. Conexiones de BITalino para EMG

## Procedimiento

Se realizaron 3 mediciones de EMG en diferentes partes del cuerpo. Para la colocación de los electrodos se tomó de referencia los ejemplos de la “Guía De Procedimiento de Electromiografía y velocidad de conducción de nervios periféricos del INSN”, el “Manual de procedimientos en electromiografía” y “BITalino (r)evolution Lab Guide”.  

La colocación de los electrodos será la siguiente: Los electrodos positivo y negativo será colocados en el músculo de interés, mientras que el electrodo de referencia será colocado en una zona neutra (por ejemplo un hueso).

### Prueba 1

En la primera prueba se obtuvo el EMG del bíceps. Los electrodos fueron colocados como se observa en la figura 2. Se tomó registro de la señal en estado de reposo o silencio eléctrico (figura 3) y realizando la contracción muscular (figura 4).

| Posicionamiento de los electrodos para la prueba 1|
|:--------------:|
|![alt text](image-1.png)  |
|Figura 2  |

| Brazo en estado de reposo| Brazo en estado de tensión |
|:--------------:|:--------------:|
| ![alt text](image-2.png)   | ![alt text](image-3.png)   |
| Figura 3    | Figura 4   |

#### Ploteo en OpenSignals

| Estado de reposo| Contracción muscular |
|:--------------:|:--------------:|
|   ![alt text](image-12.png)  |  ![alt text](image-13.png)  |
| Figura 5    | Figura 6   |

| Video: Brazo en reposo - Brazo en estado de tensión |
|:----------------------------:|
| [![alt text](videoframe_1.png)](https://youtube.com/shorts/eBpJtWsx46A?feature=share)    |



### Prueba 2

En la segunda prueba se obtuvo el EMG del pulgar (Abductor pollicis brevis). Los electrodos fueron colocados como se observa en la figura 7, con una separación aproximada de 2 cm entre electrodo positivo y negativo. Se tomó registro de la señal en estado de reposo o silencio eléctrico (figura 8) y realizando la contracción muscular (figura 9).

| Posicionamiento de los electrodos para la prueba 2|
|:--------------:|
|![alt text](image-5.png)  |
|Figura 7  |

| Estado de reposo| Contracción muscular |
|:--------------:|:--------------:|
| ![alt text](image-6.png)    | ![alt text](image-7.png)    |
| Figura 8    | Figura 9   |

#### Ploteo en OpenSignals

| Estado de reposo| Contracción muscular |
|:--------------:|:--------------:|
| ![alt text](image-4.png)    | ![alt text](image-11.png)    |
| Figura 10   | Figura 11   |

| Video: Dedo en reposo - Dedo en estado de tensión |
|:----------------------------:|
| [![alt text](videoframe_2.png)](https://www.youtube.com/shorts/tir6_gNDhgk?feature=share)    |




### Prueba 3

En la segunda prueba se obtuvo el EMG del sóleo. Los electrodos fueron colocados como se observa en la figura 12. Se tomó registro de la señal en estado de reposo o silencio eléctrico (figura 13) y realizando la contracción muscular (figura 14).

| Posicionamiento de los electrodos para la prueba 3|
|:--------------:|
|![alt text](image-8.png)  |
|Figura 12  |

| Estado de reposo| Contracción muscular |
|:--------------:|:--------------:|
| ![alt text](image-9.png)    | ![alt text](image-10.png)    |
| Figura 13    | Figura 14   |

#### Ploteo en OpenSignals

| Estado de reposo| Contracción muscular |
|:--------------:|:--------------:|
| ![alt text](image-14.png)  | ![alt text](image-15.png)   |
| Figura 15    | Figura 16  |

| Video : Pierna en reposo - Pierna en estado de tensión |
|:----------------------------:|
| [![alt text](videoframe_3.png)](https://youtu.be/3J8K--_KSd0)    |

### Explicación

Respecto a las mediciones tomadas sobre los músculos en estado de reposo se puede observar silencio electrónico lo que significa que el sensor no detecta actividad muscular significativa. A pesar de que el silencio electrónico es diferente respecto a sensores de electromiografía con agujas intramusculares debido a que utilizamos electrodos de superficie esto se debe a que los últimos son menos precisos. Es por esto que la señal se observa con ruido ya que es más susceptible a interferencias. 

Asímismo, en dichas señales las pequeñas perturbaciones (picos de baja amplitud) también pueden causadas por potenciales eléctricos activados involuntariamente, mayormente debido a precencia de fluctuaciones leves de concentraciones de electrolitos, actividad neurogénica residual (pequeñas concentraciones de neurotransmisores en el interticio de la unida motora) y alteración de la permeabilidad de la membrana, mayormente por hormonas como la adrenalida. Sin embargo, la presencia de espasmos leves tambien genera alteraciones en la actividad muscular

Por otro lado, cuando el músculo es tensionado, el flujo de electrolitos no es precisamente constante y uniforme; asi como la secreción de neurotransmisores por parte de las células nerviosas de las unidades motoras. Por ello, es que la actividad electrica del músculo no es constante, pero si es alta. 

En general, otra motivo por el cual la señal eléctrica puede verse distorcionada, es la circulación de iones en el torrente sanguíneo, en el tejido epitelial epidérmico, subcutáneo y adiposo; lo que físicamente significaría la formación de potenciales eléctricos.

##  Ploteo de Python

- Para el ploteo de la primera señal adquirida, que refiere al EMG del paquete muscular **biceps braquial**, se tiene el siguiente código: 
(Archivo: Ploteo_s1.py)

![alt text](scatter_plot1.png)

```python
import re
with open('emg1.txt', 'r') as file:
    texto = file.read()


columna_sexta = re.findall(r'\b\d+\b', texto.split("# EndOfHeader")[1])
Signal = []
k = 10
for valor in columna_sexta:
    Signal.append((float(valor)/(2^k)-1/2)*3.3/1009)

n = [i for i in range(0,len(Signal))]
Ts = 1/1000
time = [i*Ts for i in n]

import matplotlib.pyplot as plt

plt.plot(time, Signal)
plt.xlabel('Time')
plt.ylabel('Signal')
plt.title('Electromiogram Signal taken from biceps activity')

plt.legend()
plt.savefig('scatter_plot1.png')
plt.show()
```

- Para el ploteo de la segunda señal adquirida, que refiere al EMG del músculo __abductor pollicis brevis__, se tiene el siguiente código: 
(Archivo: Ploteo_s2.py)

![alt text](scatter_plot2.png)

```python 
import re
with open('emg2.txt', 'r') as file:
    texto = file.read()


columna_sexta = re.findall(r'\b\d+\b', texto.split("# EndOfHeader")[1])
Signal2 = []

k = 10
for valor in columna_sexta:
    Signal2.append((float(valor)/(2^k)-1/2)*3.3/1009)
n = [i for i in range(0,len(Signal2))]
Ts = 1/1000
time2 = [i*Ts for i in n]
print(len(time2))
print(len(Signal2))
import matplotlib.pyplot as plt

plt.plot(time2, Signal2)
plt.xlabel('Time')
plt.ylabel('Signal')
plt.title('Electromiogram Signal taken from "Pollicis brevis abductor" activity')
plt.legend()
plt.savefig('scatter_plot2.png')
plt.show()

```
- Para el ploteo de la tercera señal adquirida, que refiere al EMG del músculo __sóleo__ y __gemelos__, se tiene el siguiente código: 
(Archivo: Ploteo_s3.py)

![alt text](scatter_plot3.png)

```python
import re
with open('emg3.txt', 'r') as file:
    texto = file.read()


columna_sexta = re.findall(r'\b\d+\b', texto.split("# EndOfHeader")[1])
Signal3 = []

k = 10
for valor in columna_sexta:
    Signal3.append((float(valor)/(2^k)-1/2)*3.3/1009)
n = [i for i in range(0,len(Signal3))]
Ts = 1/1000
time3 = [i*Ts for i in n]
print(len(time3))
print(len(Signal3))
import matplotlib.pyplot as plt

plt.plot(time3, Signal3)
plt.xlabel('Time')
plt.ylabel('Signal')
plt.title('Electromiogram Signal taken from Soleum activity')
plt.legend()
plt.savefig('scatter_plot3.png')
plt.show()
```

## Referencias

[1]  “Electromiografía”, Mayoclinic.org, 21-may-2019. [En línea]. Disponible en: https://www.mayoclinic.org/es/tests-procedures/emg/about/pac-20393913. [Consultado: 13-abr-2024].

[2] “Electromyography (EMG) Sensor User Manual”, Bitalino.com. [En línea]. Disponible en: https://www.bitalino.com/storage/uploads/media/electromyography-emg-user-manual.pdf. [Consultado: 13-abr-2024].