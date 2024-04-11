# ISB-Grupo4

<div style="text-align: justify"> 
Bienvenidos al repositorio del Grupo 4 del curso de Introducción a Señales Biomédicas ...


Somos estudiantes del 7mo ciclo de la carrera de Ingeniería Biomédica, que busca proponer un proyecto para el curso con el fin de comprender la base fundamental de distintas señales biomédicas, desde su análisis y procesamiento hasta su aplicación en un contexto real.

</div>

![Señal cerebral](https://corprensa-la-prensa-prod.cdn.arcpublishing.com/resizer/C7WvY7BSXYcBWZqIoymt3WlzWzc=/fit-in/1200x1200/smart/arc-anglerfish-arc2-prod-corprensa.s3.amazonaws.com/public/2AI6JUCFTREWLDTC7LVWSH45DQ.jpg)



Figura 1. Señal cerebral. Extraído de: https://www.prensa.com/impresa/vivir/Salud-mental-genetica-factores-ambientales_0_4744775508.html

# Tabla de contenidos
- [¿Qué es una bioseñal?](#qué-es-una-bioseñal)
- [Materiales](#materiales)
- [Metodología](#metodología)
- [Temática del proyecto](#temática-del-proyecto)
- [Contenido del curso](#Contenido-del-curso)
- [Participantes](#Participantes)
- [Docentes del curso](#docentes-del-curso)

# 
# ¿Qué es una bioseñal? 


<div style="text-align: justify"> 
Una bioseñal es un tipo de señal que puede ser medida y controlada continuamente en seres biológicos, refiriéndose tanto a señales eléctricas como no eléctricas [1]. En el contexto de bioseñales eléctricas, se incluyen electroencefalogramas (EEG), magnetoencefalogramas (MEG) y electrocardiogramas (ECG o EKG); que son originadas por biopotenciales (cambios de potencial eléctrico entre las células nerviosas) [2] . Mientras que en las bioseñales no eléctricas se encuentran las señales mecánicas como la presión arterial, la temperatura corporal o señales acústicas. Además, existen otras formas de bioseñales no eléctricas, como las imágenes médicas obtenidas mediante resonancia magnética (IRM) y tomografía computarizada (TC), que proporcionan información estructural y funcional del cuerpo humano. Estas bioseñales son fundamentales en la medicina y la investigación biomédica, ya que proporcionan información valiosa sobre la salud y el funcionamiento del organismo [1].

[1] “Procesamiento y Clasificación de Bioseñales con Inteligencia Computacional”, Smia.mx. [En línea]. Disponible en: https://smia.mx/comia/2017/index.php?Itemid=127&id=12&option=com_content&view=article. [Consultado: 23-mar-2024].

[2] J. F. Guerrero Martínez, “Tema 2 Bioseñales”. Disponible en: http://ocw.uv.es/ingenieria-y-arquitectura/1-5/ib_material/IB_T2_OCW.pdf. [Consultado: 23-mar-2024].
</div>


# Materiales



# Metodología
## Distribución de carpetas

- Entregable 1 - Problemática

    1. Identificación de la problemática: Introducción, Contexto, Definición de la Problemática
    2. Estado del Arte: Artículos científicos para la detección de arritmias por señales de ECG
    3. Propuesta de Solución: Características Generales, Modo de Uso, Propósito, Características Específicas

- Propuesta de Solución: Otros Entregables

- Laboratorios: Experiencias de laboratorio e Informes
    1. Laboratorio 2
    2. Laboratorio X 


# Contenido del curso
## UNIDAD 1: Introducción y adquisición de las señales EMG, ECG Y EEG

En la primera unidad, se establece una sólida base al presentar las señales más utilizadas en el ámbito biomédico, desde el electromiograma (EMG) hasta el electrocardiograma (ECG) y el electroencefalograma (EEG). Además, se exploran conceptos cruciales como la adquisición de señales y el uso de herramientas como Git y GitHub para el control de versiones y la colaboración en proyectos.

## UNIDAD 2: Procesamiento y análisis de señales ECG, EMG Y EEG
La segunda unidad se adentra en el procesamiento y análisis de estas señales, destacando la importancia de los filtros digitales y proporcionando técnicas específicas para el tratamiento de señales EMG, ECG y EEG. Estos incluyen desde la detección de actividad muscular hasta el análisis de ritmos cerebrales y la variabilidad de la frecuencia cardíaca.

## UNIDAD 3: Introducción al análisis de datos estructurados e inteligencia artificial

La tercera unidad introduce a los estudiantes en el mundo del análisis de datos estructurados y la inteligencia artificial aplicada a la medicina. Se enfoca en la creación de datasets de señales biomédicas y en el desarrollo de modelos de machine learning utilizando herramientas como TinyML y Edgeimpulse.

![Señal ECG](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwbuBMwCDsVsAleXOzzyMK9-O-LyJu6Bvo-A&s)

Figure 2. Señal de ECG. Extraída de: https://www.bmhvt.org/practice/cardiology/electrocardiogram/

<div style="text-align: justify">

# Temática del Proyecto

El proyecto consistirá en el diseño de un dispositivo __wearable__ capaz de adquirir señales ECG por medio de electrdos ...



# Participantes
 - De Moura Mendoza, John Marshello (Colaborador) | john.de.moura@upch.pe

    About me: 


 - Espinoza Quispe, Ana Lucía (Colaborador) | ana.espinoza.q@upch.pe

    About me: 



 - Flores Pérez, María Alejandra (Colaborador) |  maria.flores.perez@upch.pe

    About me: Estudiante de Ingeniería Biomédica de 7mo ciclo, 




 - Zavaleta Cavero, Juan Arturo (Colaborador) | juan.zavaleta@upch.pe

    About me: Estudiante de Ingeniería Biomédica de 7mo ciclo, interesado en el Deep Learning aplicado a las Señales e Imágenes Médicas, y desarrollo de sistemas biomecánicos automatizados para miembros anatómicos y fisiológicos. Asimismo, me consideron entusiasta de IoT y sistemas embebidos para telemonitoreo y telecomunicación entre dispositivos. 

# Docentes del curso
- De la Cruz Rodriguez, Umbert Lewis
- Meza Rodríguez, Moisés Stevend
- Cáceres del Águila, José Alonso

</div>


## Introducción

Las arritmias se definen como cualquier alteración en el ritmo natural de bombeo del corazón, sean latidos con frecuencia mayor (taquicardias o taquiarritmias) o latidos con menor recurrencia (bradicardia o bradiarritmias); sin embargo, estas pueden ser eventuales (paroxísticas) o permanentes (crónicas) [1, 2]. 

Para la detección de patrones anormales en el ciclo eléctrico cardíaco o ritmo cardíaco, comúnmente, se lleva a cabo un examen de electrocardiograma (ECG) durante un prueba de esfuerzo, con el objetivo de evaluar el corazón en su máxima actividad [3]. Sin embargo, también se pueden aplicar otro tipo de pruebas como exámenes de sangre, monitoreo para registro prolongado, estudios electrofisiológicos (EEF), etc [3]. 

A pesar de que, comúnmente, las arritmias suelen ser identificadas por los ECGs, los electrocardiógrafos no son dispositivos del todo precisos [4];  pues las señales eléctricas que estos capturan durante la prueba no son del todo precisas, debido a la interferencia de artefactos originados en el mismo cuerpo, como los artefactos musculares (de 2 a 1000 Hz), pero también la interferencia del ruido electromagnético de dispositivos próximos (50 a 60 Hz) o de la red eléctrica de potencia (60 Hz y armónicos) [5, 6].


## Contexto 

Las arritmias cardiacas son una de las principales y frecuentes complicaciones en pacientes postoperatorios de cirugías cardíacas, con una prevalencia entre el 35% y 50% [7]. Las arritmias pueden ocurrir en cualquier momento, pero la mayoría se concentra en la primera semana postoperatoria con alta incidencia en el segundo (37%) y tercer día, debido a una reacción inflamatoria sistémica y sobrecarga auricular posquirúrgica [B]. Entre las operaciones cardiacas que conducen a una mayor prevalencia de arritmias en postoperatorio se encuentran la cirugía coronaria aislada (5–95%), cirugía valvular (33–50%), cirugía combinada valvularcoronaria (36–63%) [8] y cirugía de derivación coronaria (89%) [9]. 

En general, las arritmias que se presentan luego de 72 horas tras la cirugía suelen ser de tipo transitoria, pero provocan inestabilidad hemodinámica, prolongan el soporte inotrópico y tratamientos invasivos, por lo que deben ser constantemente monitoreados por el personal encargado [9].  

No obstante, el cuidado de pacientes postoperatorios en nuestro país es deficiente. De acuerdo a investigaciones en hospitales regionales [10], solo se cuenta con 5 enfermeras o licenciadas para el cuidado de 18 pacientes postoperatorios. El personal médico brinda una atención y cuidado limitado debido a falta de tiempo y sobrecarga laboral, lo que revela la deficiencia en el monitoreo constante de los pacientes [11]. Además, debido al carácter transitorio de las arritmias postoperatorias, estas no pueden ser monitoreadas en estado de reposo en un tiempo corto de grabación dentro del mismo centro médico, pero la mayoria centros de salud de zonas rurales no cuentan con equipos tradicionales de monitoreo como el dispositivo Holter [12].

Por parte de los pacientes de zonas rurales, muchos de ellos no pueden permanecer en los centros de salud debido a los costos de cuidado y tampoco reciben un seguimiento adecuado, debido a la lejanía del centro médico [12].



Debido a ello, las arritmias en pacientes postoperatorios no son detectadas a tiempo, lo que conlleva al desarrollo de patologías cardiacas más severas, estancias prolongadas e inversiones monetarias más fuertes en las familias del paciente.

## Problemática

A partir de lo anteriormente expuesto, se propone la siguiente problemática: En las áreas rurales, hay una marcada deficiencia en el monitoreo adecuado de arritmias cardíacas en pacientes postoperatorios, lo cual no solo aumenta el riesgo de pasar por alto otras posibles complicaciones cardíacas graves, sino que también retrasa su detección, lo cual conlleva a una atención médica menos efectiva y a un mayor riesgo para la salud del paciente.

## Referencias 
[1] “Arritmia cardíaca: qué es, síntomas, tipos y tratamiento. CUN”, https://www.cun.es. [En línea]. Disponible en: https://www.cun.es/enfermedades-tratamientos/enfermedades/arritmias-cardiacas. [Consultado: 03-abr-2024].

[2] “What is an arrhythmia?”, NHLBI, NIH. [En línea]. Disponible en: https://www.nhlbi.nih.gov/health/arrhythmias. [Consultado: 03-abr-2024].

[3] “Diagnóstico de arritmias”, NHLBI, NIH. [En línea]. Disponible en: https://www.nhlbi.nih.gov/es/salud/arritmias/diagnostico. [Consultado: 03-abr-2024].

[4] M. de Merck, ECG: lectura de las ondas (animación). 2024. Disponible en: https://www.merckmanuals.com/es-us/hogar/trastornos-del-coraz%C3%B3n-y-los-vasos-sangu%C3%ADneos/arritmias/introducci%C3%B3n-a-las-arritmias. [Consultado: 03-abr-2024].

[5]Z. F. Mohd Apandi, R. Ikeura, S. Hayakawa, y S. Tsutsumi, “An analysis of the effects of noisy electrocardiogram signal on heartbeat detection performance”, Bioengineering (Basel), vol. 7, núm. 2, p. 53, 2020.

[6]  J. Doe, "Calculation of R-wave Detection Threshold in Cardiac Complexes," Journal of Cardiology, vol. 15, no. 3, pp. 112-125, April 2024.

[7] G. O. González Kadashinskaia, L. M. Bello Carrasco, y D. A. Anchundia Alvia, “Cirugía cardíaca, complicaciones inmediatas post operatorias”, Universidad y Sociedad, vol. 12, núm. 2, pp. 293–300, 2020. 

[8] F. Enríquez y A. Jiménez, “Taquiarritmias postoperatorias en la cirugía cardíaca del adulto. Profilaxis”, Cir. Cardiovasc., vol. 17, núm. 3, pp. 259–274, 2019. 

[9] A. R. Alconero Camarero, M. Carrera López, C. Muñoz García, I. Novo Robledo, y G. Saiz Fernández, “Análisis de las arritmias en el postoperatorio inmediato de cirugía cardiovascular”, Enferm. Intensiva, vol. 16, núm. 3, pp. 110–118, 2021.

[10] S. D. Panta Barandiarán y B. Y. Zavaleta Uceda, “Cuidado Enfermero a personas post operadas en el Servicio de Cirugía en un Hospital de Chiclayo 2016”, 2018.

[11] J. G. Cobeñas, “CUIDADO DE ENFERMERIA AL PACIENTE POSTOPERADO INMEDIATO”, Universidad Peruana Cayetano Heredia, Lima, Perú, 2021.

[12] R. E. Smith Colás, R. Cobo Alea, y C. R. Vázquez Seisdedos, “Diseño de un sistema inalámbrico de monitorización electrocardiográfica para dispositivos Android”, Ing. Electron. Autom. Comun., vol. 41, núm. 2, pp. 63–79, 2020.


# Estado del Arte

## Artículo 1
*Effect of continuous electrocardiogram monitoring on detection of undiagnosed atrial fibrillation after hospitalization for cardiac surgery: A randomized clinical trial*

El estudio investigó si el monitoreo continuo del ritmo cardíaco mejora la detección de la fibrilación auricular (FA) después de la cirugía cardíaca en comparación con la atención habitual. Se llevó a cabo un ensayo clínico aleatorizado en 10 centros canadienses, donde se asignaron al azar pacientes postoperatorios de cirugía cardíaca a recibir monitoreo continuo con monitores portátiles o a recibir atención habitual sin monitoreo protocolizado. Se incluyeron pacientes con alto riesgo de FA, sin antecedentes de FA preoperatoria y episodios de FA de menos de 24 horas durante la hospitalización. El monitoreo continuo mostró una mayor detección de FA en comparación con la atención habitual, con una incidencia significativamente mayor de FA después del alta en el grupo de monitoreo (19.6% vs. 1.7% en el grupo de atención habitual). Los resultados sugieren que la FA después de la cirugía cardíaca no se limita al período de hospitalización y que el monitoreo continuo es crucial para detectar eventos arrítmicos subclínicos  [1].

## Artículo 2
*Wireless single-lead ECG monitoring to detect new-onset postoperative atrial fibrillation in patients after major noncardiac surgery: A prospective observational study*

El estudio utilizó tres dispositivos inalámbricos para monitorear continuamente a los pacientes después de la cirugía mayor de cáncer gastrointestinal, centrándose en la adquisición y procesamiento de señales del electrocardiograma (ECG). El sensor de ECG de un solo plomo Isansys LifeTouch se colocó en el tórax del paciente y registró continuamente las señales de ECG, permitiendo el muestreo repetido de la frecuencia cardíaca, el ritmo cardíaco y la frecuencia respiratoria. Los datos del sensor Isansys LifeTouch y el oxímetro de pulso Nonin se transmitieron automáticamente en tiempo real a una tablet, mientras que los datos del monitor de presión arterial se transfirieron manualmente al servidor diariamente. Se utilizó un algoritmo de procesamiento de señales computarizado para detectar la fibrilación auricular postoperatoria (POAF) basado en los intervalos de picos de la onda R en los registros de ECG. Las desviaciones de los signos vitales se evaluaron utilizando umbrales predefinidos, y se analizó la asociación entre estas desviaciones y el desarrollo de POAF. Los datos se analizaron estadísticamente utilizando pruebas de asociación y modelos de regresión, ajustados por diversas variables clínicas. Este enfoque de monitoreo continuo y detección automática de POAF presenta una alternativa prometedora para mejorar la atención postoperatoria de los pacientes y detectar complicaciones cardíacas de manera temprana y precisa [2].

## Artículo 3
*Deep learning of ECG for the prediction of postoperative atrial fibrillation*

El estudio se centró en el desarrollo de un enfoque de aprendizaje profundo para predecir la fibrilación auricular postoperatoria (POAF) utilizando el electrocardiograma (ECG) preoperatorio. Se analizaron 43,980 ECG preoperatorios de 27,564 pacientes sin fibrilación auricular. Para la validación interna, la incidencia de POAF fue del 3.6%. Se lograron métricas clínicas razonables a los 7 días después de la operación, con una sensibilidad del 79.9%, especificidad del 73.5%, valor predictivo positivo del 10.2%, y valor predictivo negativo del 99.0%. Además, se evaluaron las regiones del ECG que contribuyeron al rendimiento predictivo mediante mapas de saliencia, revelando un enfoque en la onda P de baja voltaje y las regiones de ST, particularmente en aVF, V1, V2, V5 y V6 entre los 12 derivaciones del ECG. Los resultados mostraron que el modelo de aprendizaje profundo podría predecir eficazmente POAF con alta precisión. Aunque la baja incidencia de POAF podría haber contribuido a un bajo valor predictivo positivo, la alta precisión negativa es crucial para la detección temprana y el tratamiento oportuno de los pacientes de alto riesgo. Este modelo podría ser útil como herramienta de cribado inicial para identificar pacientes de alto riesgo de POAF, permitiendo una detección temprana y un tratamiento oportuno, y potencialmente previniendo eventos adversos relacionados y la aparición de fibrilación auricular espontánea en el futuro. Sin embargo, se reconoce que el estudio fue retrospectivo, lo que podría haber afectado la detección insuficiente de POAF, y se sugiere que futuras investigaciones utilicen datos prospectivos para refinar el modelo [3].

## Artículo 4
*Classification of De novo post-operative and persistent atrial fibrillation using multi-channel ECG recordings*

El artículo aborda la clasificación de la fibrilación auricular (FA), una arritmia cardíaca común, en dos categorías específicas: la FA de novo postoperatoria (POAF) y la FA persistente. La detección temprana de la FA es crucial, pero actualmente es difícil distinguir entre diferentes etapas de desarrollo de la FA utilizando el electrocardiograma (ECG) convencional. El estudio propone un método de detección de la gravedad de la FA basado en características discriminativas extraídas de datos de ECG de varios canales. Se centra en la diferenciación entre POAF de novo y FA persistente, ya que el primero es menos grave y puede proporcionar información sobre los cambios eléctricos en la aurícula [4]. El estudio destaca la importancia de detectar la FA en etapas tempranas y propone un enfoque novedoso para diferenciar entre diferentes etapas de desarrollo de la enfermedad utilizando datos de ECG de múltiples canales  [4]. 

El proceso se divide en varias etapas  [4]:

- Adquisición de datos: Se recopilaron datos de ECG de 151 pacientes, con 99 pacientes clasificados como POAF de novo y 52 como FA persistente.


- Preprocesamiento de datos: Se filtraron los datos de ECG para eliminar ruido y artefactos, y se realizaron correcciones para segmentos de baja calidad. Se aplicó un algoritmo para detectar los picos R en cada ciclo cardíaco.


- Características basadas en el ritmo: Se extrajeron características relacionadas con la irregularidad de los intervalos RR y se utilizaron gráficos de Poincaré para visualizar la estructura de correlación en las series de tiempo de los intervalos RR.


- Características basadas en el vectocardiograma (VCG): Se exploraron aspectos espaciales de las señales de ECG utilizando el VCG, que proporciona información sobre la actividad eléctrica del corazón en tres planos corporales ortogonales.

- Características basadas en la frecuencia: Se analizaron los cambios en la frecuencia de la actividad auricular durante los episodios de FA.

- Selección de características y clasificación: Se utilizó un clasificador de bosques aleatorios (RF) después de una etapa de selección de características para diferenciar entre POAF de novo y FA persistente.

- Resultados: Se logró una precisión del 89.07% en la clasificación de POAF de novo y FA persistente. Se observaron diferencias significativas en las características extraídas entre los dos grupos, lo que proporciona información sobre la fisiopatología subyacente de la FA.


## Artículo 5
*Smartphone ECG monitoring system helps lower emergency room and clinic visits in post–atrial fibrillation ablation patients*

El artículo evaluó la efectividad de un dispositivo de monitoreo de electrocardiografía (ECG) basado en smartphone (ECG Check) en la frecuencia de visitas a clínicas o salas de emergencia en pacientes sometidos a ablación de fibrilación auricular (FA). Se compararon dos grupos de pacientes: el grupo de monitoreo convencional (CM) recibió monitoreo convencional, mientras que el grupo ECG Check (EC) recibió el dispositivo ECG Check además del monitoreo convencional. Se observó que el uso del dispositivo ECG Check resultó en una reducción significativa en las visitas relacionadas con FA en comparación con el grupo de cuidados estándar. El dispositivo demostró ser sensible y específico en la detección de arritmias auriculares en el periodo postablación [5].

## Artículo 6 : 
*Enhanced detection of cardiac arrhythmias utilizing 14-day continuous ECG patch monitoring*

El artículo describe un estudio prospectivo clínico que evalúa el rendimiento de un parche de ECG continuo de 14 días para la detección de arritmias en comparación con el monitoreo convencional de 24 horas. Se reclutaron 158 pacientes sospechosos de arritmias pero no diagnosticados por ECG de 12 derivaciones. Cada paciente se sometió simultáneamente a un Holter de 24 horas y al parche de ECG de 14 días. Se identificaron siete tipos de arritmias y se encontró que el parche de 14 días detectaba más arritmias en general (59.5% vs. 19.0% del Holter de 24 horas). Además, hasta el 87.2% de las arritmias registradas con el parche de 14 días no estaban asociadas con síntomas. Se observó una mayor tasa de detección de arritmias con el parche de 14 días en pacientes con diferentes tipos de arritmias, incluyendo SVT, SVT irregular sin onda P, FA/FL y arritmias críticas. El parche de 14 días también detectó más de dos tipos de arritmias en el 5.1% de los pacientes. No se reportaron eventos adversos graves en pacientes que usaron el parche de 14 días. En conclusión, el estudio encontró que el parche de ECG de 14 días superó al Holter de 24 horas en la detección de arritmias en términos de tasa de detección general, asintomática, crítica y múltiple, y se considera una opción segura y efectiva para el monitoreo prolongado de arritmias [6].

[1] A. C. T. Ha et al., “Effect of continuous electrocardiogram monitoring on detection of undiagnosed atrial fibrillation after hospitalization for cardiac surgery: A randomized clinical trial”, JAMA Netw. Open, vol. 4, núm. 8, p. e2121867, 2021.

[2] J. D. V. Jokinen et al., “Wireless single-lead ECG monitoring to detect new-onset postoperative atrial fibrillation in patients after major noncardiac surgery: A prospective observational study”, Anesth. Analg., vol. 135, núm. 1, pp. 100–109, 2022.

[3]T. Tohyama et al., “Deep learning of ECG for the prediction of postoperative atrial fibrillation”, Circ. Arrhythm. Electrophysiol., vol. 16, núm. 2, 2023.

[4] H. Moghaddasi, R. C. Hendriks, A.-J. van der Veen, N. M. S. de Groot, y B. Hunyadi, “Classification of De novo post-operative and persistent atrial fibrillation using multi-channel ECG recordings”, Comput. Biol. Med., vol. 143, núm. 105270, p. 105270, 2022.

[5] M. Aljuaid et al., “Smartphone ECG monitoring system helps lower emergency room and clinic visits in post–atrial fibrillation ablation patients”, Clin. Med. Insights Cardiol., vol. 14, p. 117954682090150, 2020.

[6] C.-M. Liu et al., “Enhanced detection of cardiac arrhythmias utilizing 14-day continuous ECG patch monitoring”, Int. J. Cardiol., vol. 332, pp. 78–84, 2021.

# Características Generales

Dispositivo wearable que cuente con electrodos estratégicamente ubicados que sea capaz de adquirir las señales eléctricas del corazón para la detección de arritmias, y la emisión de alarmas al personal médico.  

# Modo de Uso

El modo de uso del dispositivo consiste en la portabilidad contínua por parte del paciente durante el periodo de recuperación (sea en casa o en el hospital). Se busca que el dispositivo sea ergonómico y ligero para garantizar la comodidad del usuario durante todo el día, permitiéndole realizar sus actividades diarias con normalidad mientras se monitorea su corazón de manera constante y precisa.

# Propósito 

El objetivo del dispositivo es realizar un monitoreo continuo de la actividad cardíaca, con el fin de prevenir cardiopatías futuras como infartos y/o arritmias de mayor gravedad, para que el paciente pueda recibir los cuidados y atenciones necesarias para dichas eventualidades.  

# Características Específicas

La obtención de la señal se realizaría mediante electrodos (sensores), los cuales serían acondicionados posteriormente. Este proceso consta de una etapa de amplificación y filtrado, en la que la última etapa se refiere al aislamiento de la señal cardíaca del ruido eléctrico ambiental y los artefactos musculares, a través de filtros analógicos. Posteriormente, la señal sería muestreada y sometida a otro proceso de filtrado utilizando filtros digitales, para finalmente analizar la presencia de arritmias.

La detección de arritmias se dará mediante machine learning, ya que estos modelos pueden aprender patrones complejos y sutiles de la señal en los datos de ECG que podrían no ser fácilmente identificables por métodos tradicionales (observación del médico). Se buscaría analizar irregularidades en la forma de las ondas QRS, duración del intervalo PR, intervalo QT, etc.

El sistema de envío de alrmas consiste en la emisión de una alerta sonora en del dispositivo, que permitirá que el paciente o sus familiares estén prevenidos ante una cardiopatía. En caso el paciente se encuentr en el centro hospitalario, la alarma permitíra que el personal médico sea alertado de una eventualidad cardíaca inminente. 

# Boceto de la Propuesta

![alt text](image.png)
