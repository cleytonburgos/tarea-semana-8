import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# se carga archivo xls
df = pd.read_excel('set4_produccion_pisos_ceramica_florencia.xlsx')

# visualizar 
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df, 
    x='unidades_producidas', 
    y='precio_venta_usd', 
    hue='tipo_piso',
    palette='Set2',
    s=80,
    alpha=0.8
)

# etiquetas
plt.title('Relación entre Unidades Producidas y Precio de Venta por Tipo de Piso')
plt.xlabel('Unidades Producidas')
plt.ylabel('Precio de Venta (USD)')
plt.legend(title='Tipo de Piso')
plt.tight_layout()

# gráfico
plt.show()