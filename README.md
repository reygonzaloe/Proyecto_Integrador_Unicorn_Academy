#  ** Proyecto Integrador: Análisis de Datos Mundiales** 🌎📊

#### Este proyecto es parte del bootcamp de análisis de datos en Unicorn Academy 🎓. 
#### Hemos explorado la población y el tamaño geográfico de los países a nivel mundial, utilizando SQL para el análisis de datos y Python para la manipulación y visualización. Todo el proceso está documentado en GitHub.
---


## 📚 Contenido
1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Tecnologías Utilizadas](#tecnologías-utilizadas)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Ejemplos de Consultas](#ejemplos-de-consultas)
5. [Visualizaciones](#visualizaciones)
6. [Instrucciones para Ejecutar el Proyecto](#instrucciones-para-ejecutar-el-proyecto)
7. [Contribuciones](#contribuciones)
8. [Licencia](#licencia)

## **Descripción del Proyecto**
Este proyecto integra el uso de SQL y Python para analizar datos mundiales relacionados con la población, superficie y lenguas habladas en diferentes países. Utiliza una base de datos MySQL para almacenar y consultar información sobre países y ciudades, y emplea la biblioteca Pandas para el manejo de datos y Matplotlib para la visualización gráfica.

## **Tecnologías Utilizadas**
- **Python**: Lenguaje de programación utilizado para el análisis de datos.
- **MySQL**: Sistema de gestión de bases de datos utilizado para almacenar la información.
- **Pandas**: Biblioteca de Python para la manipulación y análisis de datos.
- **Matplotlib**: Biblioteca de Python para la creación de gráficos y visualizaciones.

## **Estructura del Proyecto**
El archivo `proyecto_integrador.py` contiene las siguientes secciones:

1. **Carga de Bibliotecas**: Importación de las bibliotecas necesarias para el proyecto.
2. **Funciones**:
   - `obtener_datos_sql(query)`: Función para obtener datos de la base de datos mediante una consulta SQL.
   - `actualizar_datos_sql(update)`: Función para actualizar datos en la base de datos.
3. **Consultas SQL**: Ejecución de diversas consultas para obtener información sobre:
   - Población de países en Europa.
   - Superficie de los cinco países más grandes del mundo.
   - Población total por continente.
   - Población de ciudades en Europa.
   - Actualización de la población de China.
   - Cantidad de hablantes por idioma en Europa.

## **Ejemplos de Consultas**
- **Consulta 1**: Muestra el nombre y la población de todos los países del continente europeo.
- **Consulta 2**: Muestra los nombres y las áreas de superficie de los cinco países más grandes del mundo.
- **Consulta 3**: Calcula la población total de todos los países de cada continente.
- **Consulta 4**: Muestra el nombre de las ciudades y la población de todos los países de Europa, ordenados por población de manera descendente.
- **Consulta 5**: Actualiza la población de China a 1.5 mil millones.
- **Consulta 6**: Muestra la cantidad de hablantes por idioma en Europa.

## **Visualizaciones**
El proyecto incluye gráficos que representan:
- La población de los países de Europa (Top 10).
- La superficie de los países (Top 5).
- La población total por continente.
- Las ciudades más pobladas de Europa (Top 20).
- Hablantes por idioma en Europa.

## **Instrucciones para Ejecutar el Proyecto**
1. **Instalar Dependencias**:
   - Asegúrate de tener Python y MySQL instalados en tu sistema.
   - Instala las bibliotecas necesarias ejecutando:
     ```bash
     pip install mysql-connector-python pandas matplotlib
     ```

2. **Configurar la Base de Datos**:
   - Crea una base de datos en MySQL llamada `proyecto_integrador`, siguiendo los pasos detallos en la guia adjunta 
     en la carpeta Anexos.
   - Importa los datos necesarios en las tablas `country`, `city` y `countrylanguage`. 


3. **Ejecutar el Script**:
   - Ejecuta el archivo `proyecto_integrador.py` en tu entorno de Python.
   - Antes de ejecutar el codigo, asegurate de cambiar USER por tu usuario y PASSWORD por tu contraseña correspondiente a tu Local Host de MySQL workbench
    ---  
   ```sql   
      mysql.connector.connect(host="localhost", user="USER", passwd=¨PASSWORD")

## **Contribuciones**
Las contribuciones son bienvenidas. Si deseas colaborar, por favor abre un issue o envía un pull request.

## **Licencia**
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
