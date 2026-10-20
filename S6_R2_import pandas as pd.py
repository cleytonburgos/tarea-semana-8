from pathlib import Path

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# se cargará archivo xls 
archivo = Path(__file__).resolve().with_name('set4_produccion_pisos_ceramica_florencia.xlsx')
df = pd.read_excel(archivo)

# se configura el dashboard (1 fila, 2 columnas)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Dashboard Exploratorio: Desempeño Productivo por Planta', fontsize=14, fontweight='bold')

# Gráfico 1: Promedio de Unidades Producidas por Planta
sns.barplot(data=df, x='planta', y='unidades_producidas', ax=axes[0], palette='Blues', errorbar=None)
axes[0].set_title('Volumen de Producción Promedio')
axes[0].set_xlabel('Planta')
axes[0].set_ylabel('Unidades Producidas')

# Gráfico 2: Costo Unitario Promedio por Planta
sns.barplot(data=df, x='planta', y='costo_unitario_usd', ax=axes[1], palette='Reds', errorbar=None)
axes[1].set_title('Costo Unitario Promedio')
axes[1].set_xlabel('Planta')
axes[1].set_ylabel('Costo (USD)')

# Ajustar los espacios y mostrar
plt.tight_layout()
plt.show()