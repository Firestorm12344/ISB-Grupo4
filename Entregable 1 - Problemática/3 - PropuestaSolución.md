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