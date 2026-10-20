from pathlib import Path

import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# cargar archivo xls desde la carpeta del proyecto
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

# entrenar modelo
modelo_arbol = DecisionTreeClassifier(random_state=42, max_depth=3)
modelo_arbol.fit(X_train, y_train)

# predicciones del modelo sobre el conjunto de prueba
y_pred = modelo_arbol.predict(X_test)

# reporte de clasificación
print("--- Reporte de Clasificación ---")
print(classification_report(y_test, y_pred))

# matriz de confusión
print("\n--- Matriz de Confusión ---")
print(confusion_matrix(y_test, y_pred))