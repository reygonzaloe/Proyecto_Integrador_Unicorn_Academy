#  ** Proyecto Integrador: Análisis de Datos Mundiales** 🌎📊

Este proyecto forma parte del bootcamp de análisis de datos en Unicorn Academy 🎓. Aquí exploraremos diversos aspectos relacionados con la población y el tamaño geográfico de los países a nivel mundial, utilizando herramientas como SQL para el análisis y GitHub para la documentación.
---


## 📚 **Contenido**

- [Instalacion](#instalacion)
- [Variables de Entorno](#Variable-de-entorno)
- [Utilizacion](#Utilizacion)
- [Resultados](#resultados)
- [Importacion de Datos](#Importacion-de-datos)



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




