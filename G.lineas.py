import matplotlib.pyplot as plt
import numpy as np

# Días de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Tazas de café por persona (picos en martes y miércoles)
roberto = [1, 3, 4, 3, 4, 2, 2]
eliseo  = [1, 4, 5, 3, 3, 2, 1]
nelson  = [2, 5, 4, 1, 3, 2, 2]

x = np.arange(len(dias))
ancho = 0.25  # ancho de cada barra

plt.figure(figsize=(10,6))

# Barras agrupadas
plt.bar(x - ancho, roberto, width=ancho, color="#42A5F5", label="Roberto", alpha=0.9)
plt.bar(x,         eliseo,  width=ancho, color="#66BB6A", label="Eliseo",  alpha=0.9)
plt.bar(x + ancho, nelson,  width=ancho, color="#FFCA28", label="Nelson",  alpha=0.9)

# Títulos y ejes
plt.title("Tazas de café consumidas por día", fontsize=15, fontweight="bold")
plt.ylabel("Número de tazas", fontsize=12)
plt.xlabel("Días de la semana", fontsize=12)
plt.xticks(x, dias, fontsize=10)

# Etiquetas de valores
for i in range(len(dias)):
    plt.text(x[i] - ancho, roberto[i] + 0.1, f"{roberto[i]}", ha="center", fontsize=9, color="#0D47A1")
    plt.text(x[i],          eliseo[i]  + 0.1, f"{eliseo[i]}",  ha="center", fontsize=9, color="#1B5E20")
    plt.text(x[i] + ancho,  nelson[i]  + 0.1, f"{nelson[i]}",  ha="center", fontsize=9, color="#F57F17")

# Resalta visualmente martes y miércoles
plt.axvspan(0.5, 2.5, color="gray", alpha=0.08)  # sombreado suave sobre Mar y Mié

plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.legend(title="Personas", fontsize=10)
plt.tight_layout()
plt.show()

