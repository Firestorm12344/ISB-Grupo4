import re
import matplotlib.pyplot as plt

# Abrir el archivo emg1.txt para leerlo
with open('emg1.txt', 'r') as file:
    # Leer todo el contenido del archivo
    texto = file.read()

# Utilizando expresiones regulares para extraer la séptima columna de números
columna_septima = re.findall(r'\b\d+\b', texto.split("# EndOfHeader")[1])

# Procesamiento de los valores de la séptima columna
Signal = []
k = 10
for valor in columna_septima:
    Signal.append((float(valor)/(2**k)-1/2)*3.3/1009)

# Creación de una lista de tiempos
n = [i for i in range(0, len(Signal))]
Ts = 1/1000
time = [i * Ts for i in n]

# Graficar la señal
plt.plot(time, Signal)

# Añadir etiquetas y título
plt.xlabel('Tiempo')
plt.ylabel('Señal')
plt.title('Señal de Electromiograma tomada de la actividad del bíceps')
plt.savefig('scatter_plot1.png')
# Mostrar gráfico
plt.show()

