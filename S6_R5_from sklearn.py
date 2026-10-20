from pathlib import Path

import pandas as pd
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.tree import DecisionTreeClassifier

# carga archivo xls
archivo = Path(__file__).resolve().with_name('set4_produccion_pisos_ceramica_florencia.xlsx')
df = pd.read_excel(archivo)

# predictor (X) y variable objetivo (y)
columnas_predictoras = ['planta', 'tipo_piso', 'costo_unitario_usd', 'precio_venta_usd', 'turno_produccion']
X = df[columnas_predictoras]
y = df['produccion_alta']

# variables categóricas a numéricas
X_encoded = pd.get_dummies(X, drop_first=True)

# división de datos para entrenar y evaluar
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# entrenamiento del modelo
modelo_arbol = DecisionTreeClassifier(random_state=42, max_depth=3)
modelo_arbol.fit(X_train, y_train)

# validación cruzada (folds)
puntuaciones_cv = cross_val_score(modelo_arbol, X_encoded, y, cv=5, scoring='accuracy')

# cálculo de metricas
print(f"Exactitud en cada una de las 5 particiones: {puntuaciones_cv}")
print(f"Exactitud promedio general del modelo: {puntuaciones_cv.mean():.3f}")
print(f"Desviación estándar (estabilidad): {puntuaciones_cv.std():.3f}")