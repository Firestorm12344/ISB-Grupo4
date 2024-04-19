from Funciones import *

path = "/content/drive/MyDrive/PUCP/7mo ciclo/Instruducción a Señales Biomédicas/Laboratorios/ECG/RESPIRACION.txt"
[n, y] = get_values(path)
label = "ECG durante respiración"
plot_values(n, y, label)

path = "/content/drive/MyDrive/PUCP/7mo ciclo/Instruducción a Señales Biomédicas/Laboratorios/ECG/POS EJERCICIO.txt"
[n, y] = get_values(path)
label = "ECG Post-Ejercicio"
plot_values(n, y, label)

path = "/content/drive/MyDrive/PUCP/7mo ciclo/Instruducción a Señales Biomédicas/Laboratorios/ECG/HIPER.txt"
[n, y] = get_values(path)
label = "ECG Durante Hiperventilación"
plot_values(n, y, label)

path = "/content/drive/MyDrive/PUCP/7mo ciclo/Instruducción a Señales Biomédicas/Laboratorios/ECG/J1.txt"
[n, y] = get_values(path)
label = "ECG en Estado Basal: Resposo"
inicio = 2600
fin = 4200
plot_Customvalues(n, y, label, inicio, fin)

