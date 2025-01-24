#  ** Proyecto Integrador: Análisis de Datos Mundiales** 🌎📊

Este proyecto es parte del bootcamp de análisis de datos en Unicorn Academy 🎓. Hemos explorado la población y el tamaño geográfico de los países a nivel mundial, utilizando SQL para el análisis de datos y Python para la manipulación y visualización. Todo el proceso está documentado en GitHub.
---


## 📚 **Contenido**

- [Instalacion](#Instalacion)
- [Variables de Entorno](#Variable-de-entorno)
- [Utilizacion](#Utilizacion)
- [Resultados](#resultados)
- [Visualizaciones](#Visualizaciones)
- [Consideraciones Importantes](#Consideraciones-Importantes)
- [Licencia](#Licencia)
- [Informacion Util](#Informacion-util).
---

## ⚙️ **Configuración del Entorno**

### 1️⃣ Clona el repositorio:

```bash
git clone https://github.com/your-username/.......git
```

### 2️⃣ Instala las dependencias:

```bash
pip install mysql-connector-python
```

### 3️⃣ Ejecuta el script principal:

```bash
python main.py
```
#### Asegúrese de tener instalado Python 3.10.13 o superior.
### 4️⃣ Instalar Jupyter Notebook
```bash
pip install notebook
```

---
## Variables de Entorno:
```
#### Crea un archivo .env en la raíz del proyecto y define las siguientes variables de entorno:
* DB_HOST=localhost
* DB_USER=tu_usuario
* DB_PASSWORD=tu_contraseña
* DB_NAME=proyecto_integrador

##### Asegúrate de reemplazar tu_usuario y tu_contraseña con tus credenciales de MySQL.


## Utilizacion:

1. Importación de Datos: Utiliza los scripts en formato .sql para importar la base de datos World en MySQL a través de MySQL Workbench.

2. Conexión a MySQL: La función obtener_datos_sql(query) permite realizar consultas SQL a la base de datos. Asegúrate de definir la consulta SQL que deseas ejecutar.

# consulta_sql1 = "SELECT Name as Pais, population as Poblacion FROM proyecto_integrador.country WHERE continent = 'Europe';"
data_frame1 = obtener_datos_sql(consulta_sql1)

3. Actualización de Datos: Para actualizar datos en la base de datos, utiliza la función actualizar_datos_sql(update) con un comando SQL de tipo UPDATE

update = "UPDATE country SET population = 1500000000 WHERE code = 'CHN';"
actualizar_datos_sql(update)
```
**Resultados**
Los resultados de las consultas se almacenan en DataFrames de pandas y se pueden visualizar utilizando matplotlib. Por ejemplo, para mostrar la población de los países europeos:

plt.figure(figsize=(10, 8))
plt.barh(data_frame1['Pais'], data_frame1['Poblacion'], color='darkviolet', edgecolor="purple", linewidth=1)
plt.title('Población de Países en Europa')
plt.xlabel('Población')
plt.ylabel('País')
plt.grid(axis='x')
plt.show()

```
**Visualizacion **

Se generan diversas visualizaciones a partir de las consultas realizadas. Algunos ejemplos incluyen:

Gráficos de barras que muestran la población de los países europeos.
Gráficos que representan la superficie de los cinco países más grandes del mundo.
Visualizaciones de la población total por continente y las ciudades más pobladas de Europa.

---
```

```

## 💡 Informacion Util


Pregunta 1: ¿Cómo configuro la base de datos MySQL para este proyecto?
Respuesta: Para configurar la base de datos MySQL, primero debes crear una nueva base de datos. Luego, ajusta la configuración de conexión en el archivo .env, siguiendo las instrucciones detalladas en la sección Variables de Entorno.

Pregunta 2: ¿Qué versión de Python se requiere para ejecutar este proyecto?
Respuesta: Este proyecto requiere Python versión 3.10.13 o posterior. Asegúrate de tener instalada la versión adecuada para evitar problemas de compatibilidad.

Pregunta 3: ¿Cómo instalo las dependencias necesarias?
Respuesta: Para instalar las dependencias necesarias, sigue las instrucciones de instalación proporcionadas en la sección Instalación. Utiliza pip para instalar los paquetes requeridos.

Pregunta 4: ¿Cómo puedo ejecutar las consultas SQL proporcionadas?
Respuesta: Las consultas SQL se encuentran en el directorio /sql. Puedes ejecutar estas consultas directamente en tu base de datos MySQL utilizando un cliente MySQL o una interfaz de línea de comandos. Asegúrate de ajustar la configuración de conexión en el archivo .env antes de ejecutar las consultas.

Pregunta 5: ¿Qué debo hacer si falla la conexión a la base de datos?
Respuesta: Si experimentas problemas de conexión, verifica que tu archivo .env contenga las credenciales correctas para la base de datos. Además, asegúrate de que tu servidor MySQL esté en funcionamiento. Si el problema persiste, revisa la configuración del firewall para asegurarte de que no esté bloqueando la conexión a la base de datos.

Pregunta 6: ¿Puedo utilizar este proyecto con una base de datos que no sea MySQL?
Respuesta: Actualmente, este proyecto está diseñado para funcionar específicamente con MySQL. Sin embargo, puedes modificar la configuración de conexión en el código para adaptarlo a otras bases de datos relacionales, como PostgreSQL o SQLite.
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






