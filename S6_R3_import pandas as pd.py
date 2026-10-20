import pandas as pd

# se carga archivo xls
df = pd.read_excel('set4_produccion_pisos_ceramica_florencia.xlsx')

# cálculo costo y precio
correlacion = df['costo_unitario_usd'].corr(df['precio_venta_usd'])
print(f"La correlación entre costo unitario y precio de venta es: {correlacion:.3f}")