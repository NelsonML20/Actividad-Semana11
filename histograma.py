import matplotlib.pyplot as plt

tiempos = [10, 15, 20, 25, 30, 15, 40, 35, 20, 25]

# Crear el histograma
plt.hist(tiempos, bins=5, color='skyblue', edgecolor='black')

# Agregar títulos y etiquetas
plt.title('Tiempo que tardan los estudiantes en llegar a la universidad')
plt.xlabel('Minutos')
plt.ylabel('Frecuencia')

# Mostrar el gráfico
plt.show()
