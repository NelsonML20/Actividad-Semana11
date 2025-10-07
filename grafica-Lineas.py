import matplotlib.pyplot as plt

# Datos
nombres = ['Eliseo', 'Roberto', 'Andrea', 'Alejandro', 'Ricardo','Alberto','Bryan', 'Adaly','Omar','Antonio']
horas_dormidas = [5, 8, 7, 5, 7, 7, 4, 8, 3, 5]

# Crear gráfica de barras
plt.bar(nombres, horas_dormidas, color='skyblue')

# Título y etiquetas
plt.title('¿Cuántas horas dormiste anoche?')
plt.ylabel('Horas dormidas')

# Mostrar gráfica
plt.show()
