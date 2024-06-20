# Lab 10 - Procesamiento EEG

## Tabla de contenidos
- [Objetivos](#objetivos)
- [Materiales](#materiales)
- [Introducción](#introducción)
- [Metolodogía](#metodología)
- [Resultados](#resultados)
- [Discusión de resultados](#Discusión-de-resultados)
- [Referencias](#referencias)


##  Objetivos
- Aplicar el filtro más adecuado para la señal EEG
- Realizar la normalización de la señal de EEG
- Discutir las características extraídas de la señal EEG 

## Materiales
| Material | Cantidad |
|:--------------:|:--------------:|
| Programa *Python* | N.A | 

## Introducción

<p align="justify">
En la práctica, las señales EEG suelen estar contaminadas por artefactos biológicos y ambientales [1]. Los artefactos biológicos provienen de fuentes no cerebrales dentro del cuerpo humano, como el corazón, los ojos o los músculos [1]. Dichas fuentes originan variables como los latidos del corazón, movimientos oculares y parpadeos, la respiración, entre otros [2]. En contraste, los artefactos ambientales se originan fuera del cuerpo humano debido al movimiento de los electrodos o a la interferencia de dispositivos externos como motores eléctricos o la corriente alterna [1]. Ambos tipos de artefactos deterioran las señales EEG, complicando el diagnóstico clínico y las aplicaciones de BCI al distorsionar el espectro de potencia [1]. Esto se debe a que los artefactos pueden imitar actividad cognitiva o patológica y, por lo tanto, sesgar la interpretación de la señal. Por ende, se requiere un procesamiento de datos de ingeniería del EEG [2]. 
</p>

<p align="justify">
La práctica clínica común es cortar todo el segmento de datos afectado por los artefactos, lo cual también lleva a una pérdida de información importante [2]. Asimismo, descartar segmentos de datos no es viable si el objetivo es procesar los datos en tiempo real: en este caso, la extracción manual de artefactos no se puede realizar y una limitante está en automatizar el procedimiento de separación de artefactos [2]. Otros métodos tradicionales para eliminar artefactos de las señales EEG utilizan filtros lineales o regresiones basadas en el momento de aparición o en el rango de frecuencia de los artefactos [1]. Sin embargo, filtrar en los dominios de tiempo o frecuencia puede resultar en una pérdida significativa de la actividad cerebral debido a la superposición espectral entre la actividad neurológica y los artefactos [1]. Se ha encontrado que el análisis multirresolución con transformada wavelet discreta (DWT) es más efectivo para eliminar artefactos específicos, preservando mejor la señal EEG en los dominios de tiempo y frecuencia [1]. Por otro lado, el análisis de componentes independientes (ICA) es útil para separar artefactos específicos en un componente independiente mediante la separación ciega de fuentes [1]. La combinación de métodos wavelet e ICA ha mostrado resultados favorables en aplicaciones prácticas [1].
</p>

<p align="justify">
La aplicación del método combinado wavelet-ICA para eliminar artefactos puede requerir una inspección visual de la grabación EEG o la aplicación de un umbral definido manualmente o arbitrariamente para identificar y separar los componentes artefactuales [1]. Este umbral puede no capturar artefactos cercanos a los límites arbitrarios definidos para las señales EEG [1]. Además, el uso de un umbral manual para identificar artefactos puede incrementar la tasa de falsos positivos [1]. Dependiendo del conjunto de datos evaluado, el valor del umbral calculado puede no ser adecuado para distinguir múltiples artefactos en señales ruidosas registradas en varios canales, como ocurre a menudo con EEG multicanal ruidosos [1].
</p>

<p align="justify">

</p>

## Metodología
<p align="justify">
El procesamiento de una señal de EEG seguirá tres pasos fundamentales: el filtrado de la señal en base a un filtro wavelet-ICA, un preprocesamiento de la señal basado en su normalización y alineamiento, y finalmente la extracción de características. 
En experiencias previas de laboratorio, solo se logró obtener la señal de EEG utilizando BiTalino (solo un canal), por lo que se utilizará una señal extraída de Physionet.
</p>

A continuación, se decribe el proceso seguido en cada paso del procesamiento de la señal: 

### Diseño del Filtro EEG

<p align="justify">

</p>

### Preprocesamiento (normalización)
<p align="justify">

</p>

### Extracción de características
<p align="justify">

</p>

## Resultados

***NOTA**: El ploteo de las señales se realizó en intervalos distintos, para una mejor apreciación de las señales. Asimismo, la frecuencia de muestreo fue de 1000 Hz.*


## Código en Python




## Discusión de resultados



## Referencias
1. Sai CY, Mokhtar N, Arof H, Cumming P, Iwahashi M. Automated Classification and Removal of EEG Artifacts With SVM and Wavelet-ICA. IEEE J Biomed Health Inform [Internet]. Mayo de 2018 [consultado el 19 de junio de 2024];22(3):664-70. Disponible en: https://doi.org/10.1109/jbhi.2017.2723420.
2. Mammone N, La Foresta F, Morabito FC. Automatic Artifact Rejection From Multichannel Scalp EEG by Wavelet ICA. IEEE Sens J [Internet]. Marzo de 2012 [consultado el 19 de junio de 2024];12(3):533-42. Disponible en: https://doi.org/10.1109/jsen.2011.2115236

