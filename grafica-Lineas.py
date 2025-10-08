#importamos la librería
import matplotlib.pyplot as plt

# Lista de los 10 nombres de los compañeros 
nombres = ['Eliseo', 'Roberto', 'Andrea', 'Alejandro', 'Ricardo','Alberto','Bryan', 'Adaly','Omar','Antonio']

#Lista con las horas que cada compañero durmió anoche
horas_dormidas = [5, 8, 7, 5, 7, 7, 4, 8, 3, 5]

# Crear gráfica de barras usando los nombres y las horas dormidas --- cada barra representa,
# cuántas horas durmió una persona
plt.bar(nombres, horas_dormidas, color='skyblue')

# Le agregar un titulo a la grafica
plt.title('¿Cuántas horas dormiste anoche?')

# Le agregamos una etiqueta al eje vertical Y
plt.ylabel('Horas dormidas')

# Mostramos la grafica 
plt.show()
