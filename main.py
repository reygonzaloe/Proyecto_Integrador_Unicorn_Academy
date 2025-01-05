import mysql.connector
import pandas as pd
from mysql.connector import Error

def obtener_datos_sql(query):
    try:
        # Establecemos la conexión a la base de datos
        conexion = mysql.connector.connect(host="localhost", user="root", password='123456',database= 'proyecto_integrador')

        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")

            # Creamos un cursor
            cursor = conexion.cursor()

            # Ejecutamos la consulta SQL
            cursor.execute(query)

            # Obtenemos los nombres de las columnas
            columnas = [i[0] for i in cursor.description]

            # Obtenemos todos los resultados
            resultados = cursor.fetchall()

            # Creamos un DataFrame de pandas
            df = pd.DataFrame(resultados, columns=columnas)

            return df

    except Error as e:
        print(f"Ocurrió un error: {e}")
        return None

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada")


# Consulta SQL genérica
consulta_sql = "select distinct(continent) from country;"  # Cambia esto a tu consulta deseada

# Llamamos a la función y mostramos el DataFrame
data_frame = obtener_datos_sql(consulta_sql)
if data_frame is not None:
    print(data_frame)

##### Ejercicio 1: Escribe una consulta para mostrar el nombre y la población de todos los países del continente europeo
consulta_sql1 = "SELECT Name, population FROM proyecto_integrador.country WHERE continent = 'Europe';"  # Cambia esto a tu consulta deseada

# Llamamos a la función y mostramos el DataFrame
data_frame = obtener_datos_sql(consulta_sql1)
if data_frame is not None:
    print(data_frame)

##### Ejercicio 2: Escribe una consulta para mostrar los nombres y las áreas de superficie de los cinco países más grandes del mundo (en términos de área de superficie).
consulta_sql2 = "SELECT Name, SurfaceArea FROM country ORDER BY SurfaceArea desc limit 5;"  # Cambia esto a tu consulta deseada

# Llamamos a la función y mostramos el DataFrame
data_frame = obtener_datos_sql(consulta_sql2)
if data_frame is not None:
    print(data_frame)

##### Ejercicio 3: Escribe una consulta para calcular la población total de todos los países de cada continente y mostrar el resultado junto con el nombre del continente.
consulta_sql3 = "SELECT ci.name as City, ci.population as Population, co.name as Country FROM city as ci LEFT JOIN country as co ON ci.countrycode = co.code WHERE co.continent = 'Europe' ORDER BY ci.POPULATION desc;"  # Cambia esto a tu consulta deseada

# Llamamos a la función y mostramos el DataFrame
data_frame = obtener_datos_sql(consulta_sql3)
if data_frame is not None:
    print(data_frame)

##### Ejercicio 4: Escribe una consulta para mostrar el nombre de las ciudades y la población de todos los países de Europa, ordenados por población de la ciudad de manera descendente.
  consulta_sql4 = "SELECT ci.name as City, ci.population as Population, co.name as Country FROM city as ci LEFT JOIN country as co ON ci.countrycode = co.code WHERE co.continent = 'Europe' ORDER BY ci.POPULATION desc"  # Cambia esto a tu consulta deseada

# Llamamos a la función y mostramos el DataFrame
data_frame = obtener_datos_sql(consulta_sql4)
if data_frame is not None:
    print(data_frame)

##### Ejercicio 5: Actualiza la población de China (código de país 'CHN') a 1500000000 (1.5 mil millones).
  


  



