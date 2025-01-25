import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from mysql.connector import Error

def obtener_datos_sql(query):
    """Función para obtener datos de la base de datos."""
    try:
        conexion = mysql.connector.connect(host="localhost", user="root", password="123456", database="proyecto_integrador")

        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            cursor = conexion.cursor()
            cursor.execute(query)
            columnas = [i[0] for i in cursor.description]
            resultados = cursor.fetchall()
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

def actualizar_datos_sql(update):
    """Función para actualizar datos en la base de datos."""
    try:    
        conexion = mysql.connector.connect(host="localhost", user="root", password="123456", database="proyecto_integrador")
       
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            cursor = conexion.cursor()
            cursor.execute(update)
            conexion.commit()
            print("Datos actualizados")
    except Error as e:
        print(f"Ocurrió un error: {e}")
        return None

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada")

# Ejercicio 1: Población de países de Europa
consulta_sql1 = "SELECT Name as Pais, population as Poblacion FROM proyecto_integrador.country WHERE continent = 'Europe';"
data_frame1 = obtener_datos_sql(consulta_sql1)
if data_frame1 is not None:
    print(data_frame1)
    data_frame1_Top10 = data_frame1.nlargest(10, 'Poblacion').sort_values(by='Poblacion', ascending=True)
    data_frame1_Top10['Poblacion_millones'] = data_frame1_Top10['Poblacion'] / 1_000_000

    # Gráfico de barras
    plt.figure(figsize=(10, 8))
    barras = plt.barh(data_frame1_Top10['Pais'], data_frame1_Top10['Poblacion_millones'], color='darkviolet', edgecolor="purple", linewidth=2)
    plt.title('Población de Países de Europa (Top 10)')
    plt.xlabel('Población (millones)')
    plt.ylabel('País')

    for b in barras:
        xval = b.get_width() 
        plt.text(xval + 0.5, b.get_y() + b.get_height() / 2, f"{xval:.2f}", ha='left', va='center') 
    
    plt.grid(axis='x')
    plt.show()

# Ejercicio 2: Superficie de los cinco países más grandes
consulta_sql2 = "SELECT Name as Pais, SurfaceArea as Superficie_km2 FROM country ORDER BY SurfaceArea DESC LIMIT 5;"
data_frame2 = obtener_datos_sql(consulta_sql2)
if data_frame2 is not None:
    print(data_frame2)
    data_frame2['Superficie_millones_km2'] = data_frame2['Superficie_km2'] / 1_000_000
    data_frame2 = data_frame2.sort_values(by='Superficie_millones_km2', ascending=True)

    # Gráfico de barras
    plt.figure(figsize=(10, 5))
    barras = plt.barh(data_frame2['Pais'], data_frame2['Superficie_millones_km2'], color='darkviolet', edgecolor="purple", linewidth=2)
    plt.title('Superficie de Países (Top 5)')
    plt.xlabel('Superficie (millones km²)')
    plt.ylabel('País')

    for b in barras:
        xval = b.get_width() 
        plt.text(xval + 0.1, b.get_y() + b.get_height() / 2, f"{xval:.2f}", ha='left', va='center') 

    plt.grid(axis='x')

    plt.show()

# Ejercicio 3: Población total de todos los países por continente
consulta_sql3 = "SELECT Continent as Continente, SUM(population) as PoblacionTotal FROM country GROUP BY continent ORDER BY SUM(population) DESC;"
data_frame3 = obtener_datos_sql(consulta_sql3)
if data_frame3 is not None:
    print(data_frame3)
    data_frame3['PoblacionTotal_Millones'] = data_frame3['PoblacionTotal'] / 1_000_000
    data_frame3 = data_frame3.sort_values(by='PoblacionTotal', ascending=True)

    # Gráfico de barras
    plt.figure(figsize=(10, 5))
    barras = plt.barh(data_frame3['Continente'], data_frame3['PoblacionTotal_Millones'], color='darkviolet', edgecolor="purple", linewidth=2)
    plt.title('Población Total por Continente')
    plt.xlabel('Población Total (millones)')
    plt.ylabel('Continente')

    for b in barras:
        xval = b.get_width()
        plt.text(xval + 25, b.get_y() + b.get_height() / 2, f"{xval:.2f}", ha='left', va='center')

    plt.grid(axis='x')
    plt.show()

# Ejercicio 4: Población de ciudades en Europa
consulta_sql4 = """
SELECT ci.name as Ciudad, ci.population as Poblacion, co.name as Pais 
FROM city as ci 
LEFT JOIN country as co ON ci.countrycode = co.code 
WHERE co.continent = 'Europe' 
ORDER BY ci.POPULATION DESC;
"""
data_frame4 = obtener_datos_sql(consulta_sql4)
if data_frame4 is not None:
    print(data_frame4)
    data_frame4_top = data_frame4.nlargest(20, 'Poblacion')
    data_frame4_top['Poblacion_millones'] = data_frame4_top['Poblacion'] / 1_000_000
    data_frame4_top = data_frame4_top.sort_values(by='Poblacion_millones', ascending=True)

    # Gráfico de barras
    plt.figure(figsize=(10, 6))
    barras = plt.barh(data_frame4_top['Ciudad'], data_frame4_top['Poblacion_millones'], color='darkviolet', edgecolor="purple", linewidth=2)
    plt.title('Ciudades más pobladas de Europa (Top 20)')
    plt.xlabel('Población Total (millones)')
    plt.ylabel('Ciudad')

    for b in barras:
        xval = b.get_width()
        plt.text(xval + 0.05, b.get_y() + b.get_height() / 2, f"{xval:.2f}", ha='left', va='center') 

    plt.grid(axis='x')
    plt.show()

# Ejercicio 5: Actualizar la población de China
consulta_sql5 = "SELECT name as Pais, code as CodigoPais, population as Poblacion FROM country WHERE code = 'CHN'"
data_frame5 = obtener_datos_sql(consulta_sql5)
if data_frame5 is not None:
    print(data_frame5) 

# Actualizar población
update = "UPDATE country SET population = 1500000000 WHERE code = 'CHN';"
actualizar_datos_sql(update)

data_frame5 = obtener_datos_sql(consulta_sql5)
if data_frame5 is not None:
    print(data_frame5)

# Ejercicio 6: Cantidad de hablantes por idioma en Europa
consulta_sql6 = """
SELECT co.Name AS Pais, co.Continent AS Continente, cl.Language AS Idioma, 
       cl.Percentage AS Porcentaje, 
       ROUND(co.Population * (cl.Percentage / 100), 0) AS Hablantes_Por_Idioma 
FROM country co 
JOIN countrylanguage cl ON co.Code = cl.CountryCode 
ORDER BY ROUND(co.Population * (cl.Percentage / 100), 0) DESC;
"""
data_frame6 = obtener_datos_sql(consulta_sql6)
if data_frame6 is not None:
    print(data_frame6)
    data_frame6['Hablantes_Por_Idioma'] = pd.to_numeric(data_frame6['Hablantes_Por_Idioma'])
    data_frame6['Porcentaje'] = pd.to_numeric(data_frame6['Porcentaje'])
    data_frame6_mod = data_frame6[(data_frame6['Continente'] == 'Europe') & (data_frame6['Porcentaje'] > 0)]
    print(data_frame6_mod)

    consulta_sql_PT = "SELECT Name as Pais
