from Funciones import *

"""## RESPIRACIÓN"""

path = "/content/drive/MyDrive/PUCP/7mo ciclo/Instruducción a Señales Biomédicas/Laboratorios/ECG/RESPIRACION.txt"
[n, y] = get_values(path)
label = "ECG durante respiración"
plot_values(n, y, label)

"""## POST-EJERCICIO"""

path = "/content/drive/MyDrive/PUCP/7mo ciclo/Instruducción a Señales Biomédicas/Laboratorios/ECG/POS EJERCICIO.txt"
[n, y] = get_values(path)
label = "ECG Post-Ejercicio"
plot_values(n, y, label)

"""## HIPERVENTILACIÓN"""

path = "/content/drive/MyDrive/PUCP/7mo ciclo/Instruducción a Señales Biomédicas/Laboratorios/ECG/HIPER.txt"
[n, y] = get_values(path)
label = "ECG Durante Hiperventilación"
plot_values(n, y, label)

"""## ESTADO BASAL: REPOSO"""

path = "/content/drive/MyDrive/PUCP/7mo ciclo/Instruducción a Señales Biomédicas/Laboratorios/ECG/J1.txt"
[n, y] = get_values(path)
label = "ECG en Estado Basal: Resposo"
inicio = 2600
fin = 4200
plot_Customvalues(n, y, label, inicio, fin)

path = "/content/drive/MyDrive/PUCP/7mo ciclo/Instruducción a Señales Biomédicas/Laboratorios/ECG/fase 2.txt"
[n, y] = get_values(path)
label = "ECG Fase 2: Simulación"
plot_values(n, y, label)

path = "/content/drive/MyDrive/PUCP/7mo ciclo/Instruducción a Señales Biomédicas/Laboratorios/ECG/fase 3.txt"
[n, y] = get_values(path)
label = "ECG Fase 3: Simulación"
plot_Customvalues(n, y, label, 20000, 23000)

path = "/content/drive/MyDrive/PUCP/7mo ciclo/Instruducción a Señales Biomédicas/Laboratorios/ECG/fase 4 5 y 6.txt"
[n, y] = get_values(path)
label = "ECG Fase 4: Simulación"
plot_Customvalues(n, y, label, 500, 3000)

path = "/content/drive/MyDrive/PUCP/7mo ciclo/Instruducción a Señales Biomédicas/Laboratorios/ECG/fase 4 5 y 6.txt"
[n, y] = get_values(path)
label = "ECG Fase 5: Simulación"
plot_Customvalues(n, y, label, 14000, 16000)

path = "/content/drive/MyDrive/PUCP/7mo ciclo/Instruducción a Señales Biomédicas/Laboratorios/ECG/fase 4 5 y 6.txt"
[n, y] = get_values(path)
label = "ECG Fase 6: Simulación"
plot_Customvalues(n, y, label, 41500, 45000)

