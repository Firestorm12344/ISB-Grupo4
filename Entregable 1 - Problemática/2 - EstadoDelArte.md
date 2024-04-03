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