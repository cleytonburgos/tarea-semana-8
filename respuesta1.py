import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# carga datos
df = pd.read_excel("dataset_set_D_telecomunicaciones.xlsx")

# archivo soporte tecnico
df_soporte = df[['fecha_registro', 'region', 'tipo_servicio', 'incidencias_reportadas', 'tickets_soporte', 'tiempo_resolucion_hr']]
df_soporte.to_excel("reporte_soporte_tecnico.xlsx", index=False)

# 3. Garchivo exp de cliente
df_experiencia = df[['fecha_registro', 'tipo_servicio', 'clientes_afectados', 'latencia_ms', 'cumplimiento_sla']]
df_experiencia.to_excel("reporte_experiencia_clientes.xlsx", index=False)

# 4. dashboard exploratorio
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Dashboard Exploratorio: RedConecta Telecom', fontweight='bold')

# Gráfico A: Tiempo de resolución por región
sns.barplot(data=df, x='region', y='tiempo_resolucion_hr', ax=axes[0], palette='Blues', errorbar=None)
axes[0].set_title('Tiempo Medio de Resolución por Región')
axes[0].set_ylabel('Horas')

# Gráfico B: Cumplimiento SLA por Tipo de Servicio
sns.countplot(data=df, x='tipo_servicio', hue='cumplimiento_sla', ax=axes[1], palette='Set2')
axes[1].set_title('Cumplimiento de SLA por Servicio')
axes[1].set_ylabel('Cantidad de Registros')

plt.tight_layout()
plt.show()