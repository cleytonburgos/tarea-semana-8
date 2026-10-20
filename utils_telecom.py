#utils_telecom.py
import numpy as np
from scipy import stats
import joblib

def detectar_anomalias_latencia(df, columna='latencia_ms', umbral_z=3.0):
    """Detecta latencias anómalas usando Z-score con SciPy y NumPy."""
    # Se calculan los puntajes Z para identificar valores atípicos
    z_scores = np.abs(stats.zscore(df[columna].dropna()))
    df_anomalias = df.loc[df[columna].dropna().index][z_scores > umbral_z]
    return df_anomalias

def guardar_datos(df, nombre_archivo):
    """Guarda un DataFrame procesado de forma eficiente usando Joblib."""
    joblib.dump(df, nombre_archivo)
    print(f"Datos exportados exitosamente como {nombre_archivo}")