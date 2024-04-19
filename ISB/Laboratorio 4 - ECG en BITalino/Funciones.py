import pandas as pd
import matplotlib.pyplot as plt

def get_values(path):
  df = pd.read_csv(path, sep='\t', skiprows=3)  # saltar las dos primeras filas (encabezado)
  novena_columna = df.iloc[:, 6].values
  n = [i/1000 for i in range(0, len(novena_columna))]
  return n, novena_columna

def plot_values(n, y, label):
  plt.plot(n[1:3000], y[1:3000])

  # Etiquetas y título
  plt.xlabel('Índice')
  plt.ylabel('Valor')
  plt.title(label)

  # Mostrar el gráfico
  plt.show()
  plt.savefig(label+".png")
  
def plot_Customvalues(n, y, label, ini, fin):
  plt.plot(n[ini:fin], y[ini:fin])

  # Etiquetas y título
  plt.xlabel('Índice')
  plt.ylabel('Valor')
  plt.title(label)

  # Mostrar el gráfico
  plt.show()
  plt.savefig(label+".png")
  
