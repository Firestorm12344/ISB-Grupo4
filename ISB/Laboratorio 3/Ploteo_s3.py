import re
with open("emg3.txt", "r") as file:
    texto = file.read()

columna_sexta = re.findall(r'\b\d+\b', texto.split("# EndOfHeader")[1])
Signal3 = []

k = 10
for valor in columna_sexta:
    Signal3.append((float(valor)/(2^k)-1/2)*3.3/1009)
n = [i for i in range(0,len(Signal3))]
Ts = 1/1000
time3 = [i*Ts for i in n]
print(len(time3))
print(len(Signal3))
import matplotlib.pyplot as plt

plt.plot(time3, Signal3)
plt.xlabel('Time')
plt.ylabel('Signal')
plt.title('Electromiogram Signal taken from Soleum activity')
plt.legend()
plt.savefig('scatter_plot3.png')
plt.show()