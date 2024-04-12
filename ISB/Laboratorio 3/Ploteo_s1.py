import re

# Abrir el archivo emg1.txt para leerlo
with open('emg1.txt', 'r') as file:
    # Leer todo el contenido del archivo
    texto = file.read()

# Utilizando expresiones regulares para extraer la sexta columna de números
columna_sexta = re.findall(r'\b\d+\b', texto.split("# EndOfHeader")[1])
Signal = []
k = 10
# Imprimir la sexta columna de números
for valor in columna_sexta:
    Signal.append((float(valor)/(2^k)-1/2)*3.3/1009)

n = [i for i in range(0,len(Signal))]
Ts = 1/1000
time = [i*Ts for i in n]

import matplotlib.pyplot as plt

plt.plot(time, Signal)
# Añadir etiquetas y título
plt.xlabel('Time')
plt.ylabel('Signal')
plt.title('Electromiogram Signal taken from biceps activity')
# Mostrar leyenda
plt.legend()
plt.savefig('scatter_plot1.png')
plt.show()

