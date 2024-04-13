
import re
with open('emg2.txt', 'r') as file:
    # Leer todo el contenido del archivo
    texto = file.read()

# Utilizando expresiones regulares para extraer la sexta columna de números
columna_sexta = re.findall(r'\b\d+\b', texto.split("# EndOfHeader")[1])
Signal2 = []
# Imprimir la sexta columna de números
k = 10
for valor in columna_sexta:
    Signal2.append((float(valor)/(2^k)-1/2)*3.3/1009)
n = [i for i in range(0,len(Signal2))]
Ts = 1/1000
time2 = [i*Ts for i in n]
print(len(time2))
print(len(Signal2))
import matplotlib.pyplot as plt

plt.plot(time2, Signal2)
# Añadir etiquetas y título
plt.xlabel('Time')
plt.ylabel('Signal')
plt.title('Electromiogram Signal taken from "Pollicis brevis abductor" activity')
# Mostrar leyenda
plt.legend()
plt.savefig('scatter_plot2.png')
plt.show()