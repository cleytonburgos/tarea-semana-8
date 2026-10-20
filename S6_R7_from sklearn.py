from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
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

# división de datos
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# modelo árbol de decisión
modelo_arbol = DecisionTreeClassifier(random_state=42, max_depth=3)
modelo_arbol.fit(X_train, y_train)

# modelo random forest
modelo_rf = RandomForestClassifier(random_state=42, n_estimators=100)
modelo_rf.fit(X_train, y_train)

# predicciones para ambos modelos
pred_arbol = modelo_arbol.predict(X_test)
pred_rf = modelo_rf.predict(X_test)

# métrica común: exactitud
exactitud_arbol = accuracy_score(y_test, pred_arbol)
exactitud_rf = accuracy_score(y_test, pred_rf)

# gráfico comparativo
modelos = ['Árbol de Decisión', 'Random Forest']
puntuaciones = [exactitud_arbol, exactitud_rf]

plt.figure(figsize=(7, 5))
sns.barplot(x=modelos, y=puntuaciones, palette='Set2')
plt.title('Comparación de Desempeño: Árbol de Decisión vs Random Forest')
plt.ylabel('Exactitud (Accuracy)')
plt.ylim(0, 1.1)

for i, v in enumerate(puntuaciones):
    plt.text(i, v + 0.02, f'{v:.3f}', ha='center', fontweight='bold')

plt.tight_layout()
plt.show()