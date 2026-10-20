#analisis_principal.py
import pandas as pd
import joblib


def detectar_anomalias_latencia(df, columna='latencia_ms'):
	"""Devuelve las filas con latencias atípicamente altas (regla IQR)."""
	q1 = df[columna].quantile(0.25)
	q3 = df[columna].quantile(0.75)
	limite = q3 + 1.5 * (q3 - q1)
	return df[df[columna] > limite]


def guardar_datos(datos, ruta):
	"""Guarda los datos serializados con Joblib."""
	joblib.dump(datos, ruta)

# 1. Cargar el dataset
df = pd.read_excel('dataset_set_D_telecomunicaciones.xlsx')

# 2. Aplicar la función modular de análisis de anomalías
anomalias = detectar_anomalias_latencia(df, columna='latencia_ms')
print(f"Se detectaron {len(anomalias)} registros con latencia crítica.")

# 3. Guardar los resultados procesados con Joblib
guardar_datos(anomalias, 'alertas_latencia.pkl')