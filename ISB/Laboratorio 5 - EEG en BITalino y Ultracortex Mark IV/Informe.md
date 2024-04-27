# Lab 5 - EEG con BiTalino y Ultracortex Mark IV

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


Para la obtención de EEG se utilizó la guía 3 de "BITalino (r)evolution Lab Guide: EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS". Se utilizó la conexión en el puerto A4 en el BiTalino y se realizó la colocación de los electrodos de acuerdo a la configuración del sistema internacional 10-20.

* Colocación del electrodo positivo en la posición FP1 (cercano a la línea media del lado izquierdo de la cabeza) y electrodo negativo en la posición FP2 (cercano a la la linea media del lado derecho de la cabeza). Por último, el electrodo de referencia se coloca en una posición neutral como el hueso detrás de la oreja izquierda. Observar figura 1.

![alt text](image.png)
Figura 1. Colocación de electrodos. En la izquierda la colocación de electrodos positivo y negativo. A la derecha la colocación del electrodo de referencia.

![alt text](image-1.png)
Figura 2. Colocación electrodos

## Procedimiento

Se utilizó BiTalino para la adquisión de señales de la actividad cerebral al realizar distintos procesos cognitivos. Se tuvo las siguientes consideraciones para la realización del EEG:
- El sujeto de prueba debió suprimir cualquier activación muscular mientras se realiza la adquisición: movimientos en área facial (movimientos oculares y parpadeo), movimientos del cuello y la mandíbula (apretar/masticar).
- Eliminación de artefactos de interferencia o distracciones. Se buscó que el sujeto mire a un punto fijo al tener los ojos abiertos.
- No se utilizaron artefactos metálicos por parte del sujeto de prueba como lentes, aretes, piercings u otros, para no interferir con la adquisión de las señales.

### Prueba EEG 

Para la prueba de electroencefalograma se realizaron 4 pasos secuenciales. 

1. Registro de una línea base de señal (respiración normal, sin movimientos oculares, ojos cerrados) - 30 segundos
![alt text](image-8.png)
Figura 3. Fase base inicial

2. Registro de cinco ciclos de "ojos abiertos - ojos cerrados" - 5 segundos por fase en un ciclo
![alt text](image-9.png)
Figura 4. Ojos cerrados a la izquierda, ojos abiertos a la derecha.

3. Registro de una nueva fase de referencia - 30 segundos 
![alt text](image-10.png)
Figura 5. Segunda fase base

4. Registro realizando ejercicios mentales de acuerdo a  [https://link.springer.com/article/10.3758/s13415-019-00703-5/tables/1]
![alt text](image-11.png)
Figura 6. Ejercicios mentales simples y complejos

***Nota**: Para el registro realizando ejercicios mentales se leerá al usuario tres ejercicios simples y tres ejercicios complejos en voz alta y se le pedirá mantener la mirada en un punto específico y no hablar.

## BITalino

A continuación, se muestran las señales obtenidas en cada una de las fases anteriormnete descritas. 

| Estado | Señal obtenida |
|:--------------:|:--------------:|
| Figura 7. Primera fase de referencia | ![alt text](image-2.png)  |
| Figura 8. Fase 2 - Ciclo de "ojos cerrados " | ![alt text](image-3.png)|
| Figura 9. Fase 2 - Ciclo de "ojos abiertos" | ![alt text](image-4.png)|
| Figura 10. Segunda fase de referencia | ![alt text](image-5.png)|
| Figura 11. Ejercicios mentales simples | ![alt text](image-6.png)|
| Figura 12. Ejercicios mentales complejo | ![alt text](image-7.png)|


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

### BITalino Ejercicios mentales fáciles

### BITalino Ejercicios mentales complejos



##  Ploteo de Python

Para el ploteo de las señales se utilizaron funciones (Archivo: Funciones.py) para realizar el ploteo de la señal (Archivo: Ploteo.py)

``` python
def get_values(path):
  df = pd.read_csv(path, sep='\t', skiprows=3)  # saltar las dos primeras filas (encabezado)
  novena_columna = df.iloc[:, 8].values
  n = [i/1000 for i in range(0, len(novena_columna))]
  signal = [(float(valor)/(2**10)-1/2)*3.3/1009*1000*1000 for valor in novena_columna]
  return n, signal

```
``` python
def plot_values(n, y, label, ini, fin):
  plt.plot(n[ini:fin], y[ini:fin])

  # Etiquetas y título
  plt.xlabel('Tiempo (s)')
  plt.ylabel('Voltaje (uv)')
  plt.title(label)

  # Mostrar el gráfico
  plt.show()
```
``` python
path = "url"
[n, y] = get_values(path)
label = "Título"
plot_values(n, y, label, valor_inicial, valor_final)
```

## Referencias

