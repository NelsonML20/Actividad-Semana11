import matplotlib.pyplot as plt

categorias = ["Instagram","TikTok","WhatsApp","Facebook"]
porcentajes = [3,4,2,1]
colores = ["#E1306C","#D3D3D3", "#25D366", "#1877F2"]

plt.pie(
    porcentajes,
    labels=categorias,
    colors=colores,
    autopct="%1.1f%%",
    startangle=140,
    shadow=True
)

plt.title("¿Qué red social usas más?", fontsize=14, fontweight='bold')
plt.show()