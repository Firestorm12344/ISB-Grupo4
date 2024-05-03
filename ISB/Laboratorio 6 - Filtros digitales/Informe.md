# Lab 5 - Filtros digitales

## Tabla de contenidos
- [Objetivos](#objetivos)
- [Materiales](#materiales)
- [Introducción](#introduccion)
- [Metolodogía] (#metolodogia)
- [Resultados](#resultados)
- [Discusión de resultados](#Explicación/-Discusión-de-resultados)
- [Referencias](#referencias)
  
##  Objetivos
- Comprender los fundamentos de filtros digitales, especialmente los IRR y FIR
- Aplicar filtros IRR y FIR a señales de EMG, ECG y EEG.
- Analizar las señales tras aplicar los filtros

## Materiales
| Material | Cantidad |
|:--------------:|:--------------:|

| Programa *Python* | N.A | 

## Introducción

<div style="text-align: justify;">

Filtros Digitales 

Filtros IRR y Filtros FIR

Para la práctica se utilizó el programa Python para aplicar los filtros digitales mencionados, graficar las señales y analizarlas.


## Metolodogía

Se utilizó el siguiente código como filtro IRR para las señales EMG, ECG y EEG. En este caso el filtro es Butterworth.

Se utilizó el siguiente código como filtro FIR para las señales EMG, ECG y EEG.

### Diseño del Filtro EMG

### Diseño del Filtro ECG

### Diseño del Filtro EEG

## Resultados

***NOTA**: El ploteo de las señales se realizó en intervalos distintos, para una mejor apreciación de las señales.*

#EMG

Los resultados analizados en la siguiente tabla se obtuvieron al realizar el EMG del bíceps. 
Los electrodos fueron colocados como se observa en la figura 1. Los electrodos positivo y negativo será colocados en el músculo de interés, en este caso el bíceps mientras que el electrodo de referencia será colocado en una zona neutra como la muñeca.
Se tomó registro de la señal en el usuario en estado de reposo o silencio eléctrico y realizando la contracción muscular.

| Posicionamiento de los electrodos |
|:--------------:|
| <img src="image-1.png" alt="Descripción de la imagen" width="300"/> |
| Figura 1 |


| Campo | Señal Cruda | Filtro IRR | Filtro FIR |
|:--------------:|:--------------:|:--------------:|:--------------:|
| Figura 2. Señal completa| ![alt text](image-4.jpeg)| ![alt text](imageX.png)| ![alt text](imageX.png)|
| Figura 3. Reposo | ![alt text](image-5.jpeg)| ![alt text](imageX.jpeg)| ![alt text](imageX.png)|
| Figura 4. Contracción muscular | ![alt text](image-6.jpeg)| ![alt text](imageX.png)| ![alt text](imageX.png)|

#ECG

Los resultados analizados en la siguiente tabla se obtuvieron al realizar el ECG. 
Los electrodos fueron colocados como se observa en la figura 2. El electrodo positivo se posicionó en la clavícula izquierda, electrodo negativo en la clavícula derecha y electrodo de referencia en la cresta iliaca. 
Se tomó registro de la señal en el usuario en estado de reposo, hiperventilación, después de hacer ejercicio y al realizar respiraciones largas.

| Posicionamiento de los electrodos |
|:--------------:|
| <img src="image-2.png" alt="Descripción de la imagen" width="300"/> |
| Figura 5 |

| Campo | Señal Cruda | Filtro IRR | Filtro FIR |
|:--------------:|:--------------:|:--------------:|:--------------:|
| Figura 6. Reposo | ![alt text](image-7.png)| ![alt text](imageX.png) | ![alt text](imageX.png) |
| Figura 7. Hiperventilación   | ![alt text](image-8.png)| ![alt text](imageX.png) | ![alt text](imageX.png)|
| Figura 8. Después de ejercicio| ![alt text](image-9.png)| ![alt text](imageX.png)| ![alt text](imageX.png)|
| Figura 9. Respiraciones largas | ![alt text](image-10.png)| ![alt text](imageX.png)| ![alt text](imageX.png)|

#EEG

Los resultados analizados en la siguiente tabla se obtuvieron al realizar el EEG. 
Los electrodos fueron colocados como se observa en la figura 3 de acuerdo a la configuración del sistema internacional 10-20.
Se tomó registro de la señal en el usuario en una primera y segunda fase de referencia, en ciclos de ojos cerrados y abierto y realizando ejercicios mentales simples y complejos.

| Posicionamiento de los electrodos |
|:--------------:|
| <img src="image-3.png" alt="Descripción de la imagen" width="300"/> |
| Figura X |

| Campo| Señal Cruda | Filtro IRR | Filtro FIR |
|:--------------:|:--------------:|:--------------:|:--------------:|
| Figura X. Primera fase de referencia | ![alt text](image-11.png) | ![alt text](imageX.png) | ![alt text](imageX.png) |
| Figura X. Fase 2 - Ciclo de "ojos cerrados " | ![alt text](image-12.png) |![alt text](imageX.png) |![alt text](imageX.png) |
| Figura X. Fase 2 - Ciclo de "ojos abiertos" | ![alt text](image-13.png) |![alt text](imageX.png) |![alt text](imageX.png) |
| Figura X. Segunda fase de referencia | ![alt text](image-14.png) | ![alt text](imageX.png) |![alt text](imageX.png) |
| Figura X. Ejercicios mentales simples | ![alt text](image-15.png) | ![alt text](imageX.png) |![alt text](imageX.png) |
| Figura X. Ejercicios mentales complejo | ![alt text](image-16.png) | ![alt text](imageX.png) |![alt text](imageX.png) |


## Discusión de resultados



### Observaciones


## Explicación/ Discusión de resultados




## Referencias

1. 

</div>
