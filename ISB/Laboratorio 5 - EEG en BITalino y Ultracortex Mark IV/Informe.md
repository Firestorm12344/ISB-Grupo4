# Lab 4 - EEG con BiTalino y Ultracortex Mark IV

## Tabla de contenidos
- [Objetivos](#objetivos)
- [Materiales](#materiales)
- [Marco teórico](#Marco-teórico)
- [Conexión utilizada](#Conexión-utilizada)
- [Procedimiento](#Procedimiento)
- [Prueba EEG](#Prueba-EEG)
- [Explicación/ Discusión de resultados](#Explicación/-Discusión-de-resultados)
- [Ploteo de Python](#Ploteo-de-Python)
- [Referencias](#referencias)
  
##  Objetivos

- Adquirir señales biomédicas de EEG.
- Hacer una correcta configuración de BiTalino y el Ultracortex Mark IV.
- Extraer la información de las señales EEG del software OpenSignals (r)evolution y OpenBCI.

## Materiales
| Material | Cantidad |
|--------------|--------------|
| Kit BiTalino    | 1    |
| Ultracortex Mark IV | 1    |
| Laptop    | 1    |
| Electrodos    | 3    |
| Programa *Open Signal (r)evolution* | N.A |
| Programa *OpenBCI* | N.A |
| Programa *Python* | N.A | 

## Marco Teórico

XXX 

Para la práctica se utilizó 1 kit BiTalino y 1 Ultracortex Mark IV para la realización de EEG según el sistema internacional 10-20. Además, se utilizó el software OpenSignals (r)evolution y OpenBCI para la adquisición de la señal y los datos para un posterior análisis.

## Conexión utilizada


Para la obtención de EeG se utilizó la guía de "BITalino (r)evolution Lab Guide: EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS". Se utilizó la conexión en el puerto A4 en el BiTalino y se realizó la colocación de los electrodos de acuerdo a la configuración 10-20.

* Colocación del electrodo positivo en la posición FP1 (cercano a la línea media del lado izquierdo de la cabeza) y electrodo negativo en la posición FP2 (cercano a la la linea media del lado derecho de la cabeza). Por último, el electrodo de referencia se coloca en una posición neutral como el hueso detrás de la oreja izquierda. Observar figura X.

![alt text](XXX.png)
Figura X. Colocación de electrodos según el sistema internacional 10-20 (forma 1)

## Procedimiento

Se realizaron 2 mediciones de EEG. Una de ellas utilizando el BITalino y otra el Ultracortex Mark IV.

### Prueba EEG 

Para la prueba de electroencefalograma se realizaron 4 pasos secuenciales. 

1. Registro de una línea base de señal (respiración normal, sin movimientos oculares, ojos cerrados) - 30 segundos
2. Registro de cinco ciclos de "ojos abiertos - ojos cerrados" - 5 segundos por fase en un ciclo
3. Registro de una nueva fase de referencia - 30 segundos 
4. Registro realizando ejercicios mentales de acuerdo a  [https://link.springer.com/article/10.3758/s13415-019-00703-5/tables/1]

***Nota**: Para el registro realizando ejercicios mentales se leerá al usuario tres ejercicios simples y tres ejercicios complejos en voz alta y se le pedirá mantener la mirada en un punto específico y no hablar

## BITalino

| Figura X. Ejercicios realizados con el BITalino | 
| ![alt text](XXXX.png)    | 

| Estado | Señal obtenida |
|:--------------:|:--------------:|
| Figura XX. Primera fase de referencia | ![alt text](xxx.png)   |
| Figura XX. Ciclos de "ojos abiertos - ojos cerrados " | ![alt text](xxx.png)|
| Figura XX. Segunda fase de referencia | ![alt text](xxx.png)|
| Figura XX. Ejercicio mental simple 1 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental simple 2 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental simple 3 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental complejo 1 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental complejo 2 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental complejo 3 | ![alt text](xx.png)|


A su vez, por medio de Python, se logró reproducir las señales obtenidas en el programa Open Signal. Las gráficas obtenidas se muestran a continuación:

| Estado | Señal obtenida |
|:--------------:|:--------------:|
| Figura XX. Primera fase de referencia | ![alt text](xxx.png)   |
| Figura XX. Ciclos de "ojos abiertos - ojos cerrados " | ![alt text](xxx.png)|
| Figura XX. Segunda fase de referencia | ![alt text](xxx.png)|
| Figura XX. Ejercicio mental simple 1 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental simple 2 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental simple 3 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental complejo 1 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental complejo 2 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental complejo 3 | ![alt text](xx.png)|

## Ultracortex Mark IV

| Figura X. Ejercicios realizados con el Ultracortex Mark IV| 
| ![alt text](XXXX.png)    | 

| Estado | Señal obtenida |
|:--------------:|:--------------:|
| Figura XX. Primera fase de referencia | ![alt text](xxx.png)   |
| Figura XX. Ciclos de "ojos abiertos - ojos cerrados " | ![alt text](xxx.png)|
| Figura XX. Segunda fase de referencia | ![alt text](xxx.png)|
| Figura XX. Ejercicio mental simple 1 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental simple 2 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental simple 3 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental complejo 1 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental complejo 2 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental complejo 3 | ![alt text](xx.png)|


A su vez, por medio de Python, se logró reproducir las señales obtenidas en el programa Open Signal. Las gráficas obtenidas se muestran a continuación:

| Estado | Señal obtenida |
|:--------------:|:--------------:|
| Figura XX. Primera fase de referencia | ![alt text](xxx.png)   |
| Figura XX. Ciclos de "ojos abiertos - ojos cerrados " | ![alt text](xxx.png)|
| Figura XX. Segunda fase de referencia | ![alt text](xxx.png)|
| Figura XX. Ejercicio mental simple 1 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental simple 2 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental simple 3 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental complejo 1 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental complejo 2 | ![alt text](xx.png)|
| Figura XX. Ejercicio mental complejo 3 | ![alt text](xx.png)|

***NOTA**: El ploteo de las señales se realizó en intervalos distintos, para una mejor apreciación de las señales.*

### Observaciones

Durante el desarrollo de la prueba se notaron aspectos que impactaron de manera significativa en la obtención de las señales de EEG. Se observó que mientras se realizaba la toma de la señal de EEG y se acercaba un dispositivo electrónico como laptop o celular a la persona que realizaba la prueba, la señal se distorsionaba de manera significativa.

## Explicación/ Discusión de resultados

### BITalino Primera fase de referencia

### BITalino Ciclos de "Ojos abiertos - ojos cerrados"

### BITalino Segunda fase de referencia

### BITalino Ejercicios mentales

### Ultracortex Mark IV Primera fase de referencia

### Ultracortex Mark IV Ciclos de "Ojos abiertos - ojos cerrados"

### Ultracortex Mark IV Segunda fase de referencia

### Ultracortex Mark IV Ejercicios mentales


##  Ploteo de Python

Para el ploteo de las señales se utilizaron funciones (Archivo: Funciones.py) para realizar el ploteo de la señal (Archivo: Ploteo.py)

``` python



```

## Referencias

