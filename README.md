#  **Análisis de Datos Mundiales** 🌎📊

El tema principal que explora este proyecto es "la integración y manipulación de bases de datos relacionales (MySQL) con aplicaciones desarrolladas en Python". Este tema abarca múltiples aspectos del desarrollo de software.
---

## 📑 **Índice**

1. [📚 **Descripción del Proyecto**](#descripción-del-proyecto)
2. [⚙️ **Configuración del Entorno**](#configuración-del-entorno)
3. [🗄️** Importación de la Base de Datos**](#importacion_de_datos)
   💻 Conexión de Python con MySQL
 - Configuración de la conexión 🔗
 - Consultas SQL desde Python 📑
 - Población de países europeos 🌍
 - Cinco países más grandes por superficie 🌏
 - Población total por continente 🧮
 - Ciudades más pobladas de Europa 🏙️
 - Actualización de datos en la base 🖊️
📈 Análisis y Visualizaciones
 - Distribución de la población por continente 🌎
 - Comparación de superficie de países 🗺️
 - Población de países europeos 📊
 - Ciudades más pobladas de Europa 🏛️ 
 - Impacto de la actualización en China 🇨🇳
4. [📌 **Conclusiones**](#conclusiones)
5. [🚀 **Cómo Ejecutar**](#cómo-ejecutar)
6. [📂 **Estructura del Proyecto**](#estructura-del-proyecto)

---

## 📚 **Descripción del Proyecto**

Analizamos un dataset ........

- **Continente.
-   **Paises**.
-   **Populacion**.
-   **Lenguaje**.
-   **Expectativa de vida**.

Este análisis responde preguntas como:

-   Muestra el nombre y la población de todos los países del continente europeo.
-   Muestra los nombres y las áreas de superficie de los cinco países más grandes del mundo (en términos de área de superficie).
-   Calculo de la población total de todos los países de cada continente y muestra el resultado junto con el nombre del continente.

---

## ⚙️ **Configuración del Entorno**

### 1️⃣ Clona el repositorio:

```bash
git clone https://github.com/
```

### 2️⃣ Instala las dependencias:

```bash
pip install 
```

### 3️⃣ Ejecuta el script principal:

```bash
python main.py
```

---

## 📈 **Análisis y Visualizaciones**

### Distribución de la población por continente 🌎

Exploramos cómo se distribuyen las puntuaciones en matemáticas, lectura y escritura.

```python
consulta_sql1 = "SELECT Name, population FROM proyecto_integrador.country WHERE continent = 'Europe';"  # Cambia esto a tu consulta deseada

# Llamamos a la función y mostramos el DataFrame
data_frame = obtener_datos_sql(consulta_sql1)
if data_frame is not None:
    print(data_frame)
```

💡 Observaciones:

-   Notamos que Russian Federation-Germany-United Kingdom-France-Italy. Son los 5 paises europeos con MAYOR poblacion.
-   Matemáticas muestra mayor dispersión comparada con lectura y escritura.

## 🔗 2. Matriz de Correlación

Evaluamos la relación entre las puntuaciones.

```python
import plotly.graph_objects as go

fig = go.Figure(data=go.Heatmap(
    z=correlation_matrix.values,
    x=correlation_matrix.columns,
    y=correlation_matrix.columns,
    colorscale="Viridis"
))
fig.update_layout(title="Matriz de Correlación")
fig.show()
```

💡 Observaciones:

-   Lectura y escritura tienen una alta correlación (~0.9).
-   Matemáticas tiene una correlación moderada (~0.6) con las otras dos materias.

## 🧑‍🎓 3. Comparación por Preparación

Analizamos el impacto de un curso de preparación en las puntuaciones.

```python
sns.boxplot(data=melted_df, x="test_prep_course", y="score", hue="subject")
plt.title("Impacto del Curso de Preparación en Puntuaciones")
plt.show()
```

💡 Observaciones:

-   Los estudiantes que completaron el curso tienen un rendimiento significativamente mejor, especialmente en matemáticas.

## 🏅 4. Estudiantes Destacados

Identificamos a los estudiantes con mejores puntuaciones.

```python
threshold = df["avg_score"].quantile(0.9)
plt.axvline(threshold, color="red", linestyle="--")
plt.hist(df["avg_score"], bins=10, edgecolor="black")
plt.title("Distribución de Promedios (Percentil 90)")
plt.show()
```

💡 Observaciones:

-   Los estudiantes destacados tienen un promedio de puntuaciones superior a 90.

## 📊 5. Visualización Combinada

Creamos un gráfico interactivo con múltiples visualizaciones.

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].hist(df["math_score"], bins=10, color="blue", edgecolor="black")
axes[0, 1].boxplot([df["math_score"], df["reading_score"], df["writing_score"]])
axes[1, 0].scatter(df["math_score"], df["reading_score"], alpha=0.6, color="green")
plt.tight_layout()
plt.show()
```

💡 Observaciones:

-   Las puntuaciones de matemáticas y lectura tienen una relación lineal positiva.
-   Las puntuaciones de escritura tienden a ser más altas que las de lectura.

---

## 📌 **Conclusiones**

1. Distribución de Puntuaciones:
    - Las puntuaciones en lectura y escritura son consistentes.
    - Matemáticas presenta mayor dispersión.
2. Matriz de Correlaciones:
    - Fuerte relación entre lectura y escritura (~0.9).
3. Impacto del Curso de Preparación:
    - Los estudiantes que completaron el curso obtuvieron mejores resultados.
4. Estudiantes Destacados:
    - El percentil 90 es un buen umbral para identificar alto rendimiento (~85 puntos).

---

## 🚀 **Cómo Ejecutar**

1. Ejecución de los análisis:

```bash
python analysis/interactive_distribution.py
```

2. Visualización de la matriz de correlación:

```bash
python analysis/interactive_correlation.py
```

3. Relaciones y comparaciones:

```bash
python analysis/score_relationship.py
```

4. Visualización combinada:

```bash
python analysis/combined_visualizations.py
```

---

## 📂 **Estructura del Proyecto**

```
 ┣ 📂 mike
 ┃ ┣ 📂 redes vs rendimiento
 ┃ ┃ ┣ 📂 analysis
 ┃ ┃ ┃ ┣ 📜 combined_visualizations.py
 ┃ ┃ ┃ ┣ 📜 ethnicity_analysis.py
 ┃ ┃ ┃ ┣ 📜 exploratory_analysis.py
 ┃ ┃ ┃ ┣ 📜 interactive_correlation.py
 ┃ ┃ ┃ ┣ 📜 interactive_distribution.py
 ┃ ┃ ┃ ┣ 📜 prediction_model.py
 ┃ ┃ ┃ ┣ 📜 score_relationship.py
 ┃ ┃ ┃ ┗ 📜 top_students.py
 ┃ ┃ ┣ 📂 data
 ┃ ┃ ┣ 📂 db
 ┃ ┃ ┃ ┣ 📜 basic_queries.py
 ┃ ┃ ┃ ┣ 📜 data_loader.py
 ┃ ┃ ┃ ┣ 📜 database_setup.py
 ┃ ┃ ┃ ┣ 📜 initial_setup.py
 ┃ ┃ ┃ ┗ 📜 __init__.py
 ┃ ┃ ┣ 📂 exports
 ┃ ┃ ┣ 📂 procedures
 ┃ ┃ ┃ ┣ 📜 advanced_queries.py
 ┃ ┃ ┃ ┣ 📜 procedures.py
 ┃ ┃ ┃ ┗ 📜 __init__.py
 ┃ ┃ ┣ 📂 script
 ┃ ┃ ┣ 📂 venv
 ┃ ┃ ┣ 📂 views
 ┃ ┃ ┃ ┣ 📜 create_views.py
 ┃ ┃ ┃ ┣ 📜 views.py
 ┃ ┃ ┃ ┗ 📜 __init__.py
 ┃ ┃ ┣ 📜 main.py
 ┃ ┃ ┗ 📜 README.md
 ┣ 📜 README.md
 ┗ 📜 requirements.txt
```

📜 Script

`main.py`: Script principal para ejecutar la exportación de datos.
📤 Exports

En esta carpeta se encuentran los archivos generados por los scripts en formato .csv.

---

👨‍💻 **Equipo de Desarrollo:**

-   [**Miguel Sarmiento**](https://www.linkedin.com/in/miguel-sarmiento-levy/)
