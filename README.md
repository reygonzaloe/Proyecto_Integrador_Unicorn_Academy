#  ** Proyecto Integrador: Análisis de Datos Mundiales** 🌎📊

Este proyecto forma parte del bootcamp de análisis de datos en Unicorn Academy 🎓. Aquí exploraremos diversos aspectos relacionados con la población y el tamaño geográfico de los países a nivel mundial, utilizando herramientas como SQL para el análisis y GitHub para la documentación.
---

🚀 Objetivos

Organizar y estructurar la base de datos: Crear un esquema bien estructurado para almacenar los datos relacionados con los patrones de sueño de los estudiantes. Esto incluye dividir la información en varias tablas para facilitar el análisis y mejorar el rendimiento de las consultas.

Aplicar las mejores prácticas de SQL: Utilizar comandos SQL eficientes y organizar el código en archivos específicos para cada paso (selección del esquema, creación de tablas, popular las tablas, verificación de datos y limpieza).

Facilitar el análisis de datos: Organizar las tablas de forma que sea fácil realizar análisis y visualizaciones en herramientas externas. Utilizar las relaciones entre las tablas para facilitar las consultas complejas, demostrando un uso avanzado de SQL, incluyendo el uso de JOIN.

Limpieza de datos: Detectar y manejar los valores nulos, duplicados y cualquier inconsistencia en los datos, utilizando técnicas de limpieza para asegurar que los datos sean precisos y confiables para el análisis.

Diseñar vistas SQL avanzadas: La finalidad es analizar y resumir datos clave, como hábitos de sueño, actividad física y tiempo frente a pantallas, permitiendo una interpretación rápida y eficiente de los resultados.

Implementar stored procedures personalizados: Automatizar consultas complejas, generar reportes dinámicos y comparar datos, optimizando el análisis y destacando habilidades avanzadas en SQL.

Documentar y explicar el proceso: Documentar cada paso del proyecto de forma detallada, explicando el propósito de cada consulta SQL, para que el proyecto sea fácilmente entendible para otros usuarios. Además, presentar los scripts de SQL bien organizados en la carpeta sql del repositorio.

Demostrar habilidades en SQL: Mostrar el dominio de funciones avanzadas de SQL (como JOIN, GROUP BY, HAVING, etc.) y la capacidad para manejar grandes cantidades de datos de forma eficiente.

Crear un repositorio bien organizado: Mantener un repositorio de GitHub limpio y bien estructurado con una documentación clara y accesible. Proporcionar un índice interactivo al principio del README.md para facilitar la navegación por los scripts SQL.

Optimizar la base de datos para futuras visualizaciones: Organizar las tablas de forma que los datos sean fácilmente exportables a herramientas de visualización de datos, como Power BI o Tableau, permitiendo un análisis visual efectivo en el futuro.

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

Exploramos cómo se distribuye la poblacion entre los continentes

```python
consulta_sql3 = "SELECT ci.name as City, ci.population as Population, co.name as Country FROM city as ci LEFT JOIN country as co ON ci.countrycode = co.code WHERE co.continent = 'Europe' ORDER BY ci.POPULATION desc;"  # Cambia esto a tu consulta deseada

# Llamamos a la función y mostramos el DataFrame
data_frame = obtener_datos_sql(consulta_sql3)
if data_frame is not None:
    print(data_frame)



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
