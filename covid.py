import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = "covidexl.csv"
df = pd.read_csv(file)  # Muestra mi dataframe

# Calculo la positividad de los ultimos 14 dias
positividad = round(df["Positividad"].mean(),2)

# Eliminar datos perdidos
df.dropna(axis=0)  # filas
df.dropna(axis=1)  # columna
print(df)
x = np.array(df.Positividad)
x = x[::-1]
print(x)
fechas = np.array(["7-mayo","8-mayo","9-mayo","10-mayo","11-mayo","12-mayo","13-mayo","14-mayo","15-mayo","16-mayo","17-mayo","18-mayo","19-mayo","20-mayo"])
print(fechas)

fig = plt.figure()
plt.plot(fechas, x, label="Positividad", color="purple")
plt.title("""La MEDIA de Positividad en los ultimos 14 dias es del """ + str(positividad) + """%""")
plt.xlabel("Dias")
plt.ylabel("Porcentaje de Positividad")
plt.legend()
plt.show()


