import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from mysql.connector import Error

def obtener_datos_sql(query):
    try:
        conexion = mysql.connector.connect(host="localhost", user="root", password="123456",database= "proyecto_integrador")

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
    try:    
        conexion = mysql.connector.connect(host="localhost", user="root", password="123456",database= "proyecto_integrador")
       
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


##### Ejercicio 1: Escribe una consulta para mostrar el nombre y la población de todos los países del continente europeo
consulta_sql1 = "SELECT Name as Pais, population as Poblacion FROM proyecto_integrador.country WHERE continent = 'Europe';"

data_frame1 = obtener_datos_sql(consulta_sql1)
if data_frame1 is not None:
    print(data_frame1)
    data_frame1_Top10 = data_frame1.nlargest(10, 'Poblacion')
    data_frame1_Top10 = data_frame1_Top10.sort_values(by='Poblacion', ascending=True)
    data_frame1_Top10['Poblacion_millones'] = data_frame1_Top10['Poblacion']/1000000

#Se genero tabla: Poblacion de Paises de Europa (top 10)
plt.figure(figsize=(10, 8))
barras = plt.barh(data_frame1_Top10['Pais'], data_frame1_Top10['Poblacion_millones'], color='darkviolet', edgecolor = "purple", linewidth = 2)
plt.title('Población de Países de Europa (Top 10)')
plt.xlabel('Población (millones)')
plt.ylabel('País')

# generamos las etiquetas en las barras con un bucle
for b in barras:
    xval = b.get_width() 
    plt.text(xval+0.5, b.get_y() + b.get_height()/2, f"{xval:.2f}", ha='left', va='center') 
    
plt.grid(axis='x')
plt.show()

    
##### Ejercicio 2: Escribe una consulta para mostrar los nombres y las áreas de superficie de los cinco países más grandes del mundo (en términos de área de superficie).
consulta_sql2 = "SELECT Name as Pais, SurfaceArea as Superficie_km2 FROM country ORDER BY SurfaceArea desc limit 5;"

data_frame2 = obtener_datos_sql(consulta_sql2)
if data_frame2 is not None:
    print(data_frame2)
    data_frame2['Superficie_millones_km2'] = data_frame2['Superficie_km2']/1000000
    data_frame2 = data_frame2.sort_values(by='Superficie_millones_km2', ascending=True)

    ##Se genero tabla: Superficie de Paises.
plt.figure(figsize=(10, 5))
barras = plt.barh(data_frame2['Pais'], data_frame2['Superficie_millones_km2'], color='darkviolet', edgecolor="purple", linewidth=2)
plt.title('Superficie de Países (Top 5)')
plt.xlabel('País')
plt.ylabel('Superficie (millones km²)')

# generamos las etiquetas en las barras con un bucle
for b in barras:
    xval = b.get_width() 
    plt.text(xval +0.1, b.get_y() + b.get_height()/2, f"{xval:.2f}", ha='left', va='center') 

plt.grid(axis='x')
plt.show()

##### Ejercicio 3: Escribe una consulta para calcular la población total de todos los países de cada continente y mostrar el resultado junto con el nombre del continente.
consulta_sql3 = "SELECT Continent as Continente,sum(population) as PoblacionTotal FROM country GROUP BY continent ORDER BY sum(population) DESC;"

data_frame3 = obtener_datos_sql(consulta_sql3)
if data_frame3 is not None:
    print(data_frame3)
    data_frame3['PoblacionTotal_Millones'] = data_frame3['PoblacionTotal'] / 1000000
    data_frame3 = data_frame3.sort_values(by='PoblacionTotal', ascending=True)

#Se genero tabla: Poblacion Total por Continente.
plt.figure(figsize=(10, 5))
barras = plt.barh(data_frame3['Continente'], data_frame3['PoblacionTotal_Millones'], color='darkviolet', edgecolor = "purple", linewidth = 2)
plt.title('Población Total por Continente')
plt.xlabel('Continente')
plt.ylabel('Población Total (millones)')

# generamos las etiquetas en las barras con un bucle
for b in barras:
    xval = b.get_width()
    plt.text(xval + 25, b.get_y() + b.get_height()/2, f"{xval:.2f}", ha='left', va='center')

plt.grid(axis='x')
plt.show()


##### Ejercicio 4: Escribe una consulta para mostrar el nombre de las ciudades y la población de todos los países de Europa, ordenados por población de la ciudad de manera descendente.
consulta_sql4 = "SELECT ci.name as Ciudad, ci.population as Poblacion, co.name as Pais FROM city as ci LEFT JOIN country as co ON ci.countrycode = co.code WHERE co.continent = 'Europe' ORDER BY ci.POPULATION desc"

data_frame4 = obtener_datos_sql(consulta_sql4)
if data_frame4 is not None:
    print(data_frame4)
    data_frame4_top['Poblacion_millones']=data_frame4_top['Poblacion']/1000000
    data_frame4_top = data_frame4_top.sort_values(by='Poblacion_millones', ascending=True)
    consulta_sql4_top = "SELECT ci.name as Ciudad, ci.population as Poblacion, co.name as Pais FROM city as ci LEFT JOIN country as co ON ci.countrycode = co.code WHERE co.continent = 'Europe' ORDER BY ci.POPULATION desc LIMIT 20"
 data_frame4_top['Poblacion_millones']=data_frame4_top['Poblacion']/1000000
data_frame4_top = data_frame4_top.sort_values(by='Poblacion_millones', ascending=True)

# Se genero Tabla: Ciudades mas pobladas de Europa (top 20).  
plt.figure(figsize=(10, 6))
barras = plt.barh(data_frame4_top['Ciudad'], data_frame4_top['Poblacion_millones'], color='darkviolet', edgecolor="purple", linewidth=2)
plt.title('Ciudades más pobladas de Europa (Top 20)')
plt.xlabel('Población Total (millones)')
plt.ylabel('Ciudad')

# generamos las etiquetas en las barras con un bucle
for b in barras:
    xval = b.get_width()
    plt.text(xval + 0.05, b.get_y() + b.get_height()/2, f"{xval:.2f}", ha='left', va='center') 

plt.grid(axis='x')
plt.show()

    

##### Ejercicio 5: Actualiza la población de China (código de país 'CHN') a 1500000000 (1.5 mil millones).
consulta_sql5 = "SELECT name as Pais, code as CodigoPais, population as Poblacion FROM country WHERE code = 'CHN'"

data_frame5 = obtener_datos_sql(consulta_sql5)
if data_frame5 is not None:
    print(data_frame5) 

# (La población inicial de China era de '1277558000')

update = "UPDATE country SET population = 1500000000 WHERE code = 'CHN';"

actualizar_datos_sql(update)

data_frame5 = obtener_datos_sql(consulta_sql5)
if data_frame5 is not None:
    print(data_frame5)

#Ejercicio 6: Cantidad de hablantes por idioma en Europa.
consulta_sql6 = "SELECT co.Name AS Pais, co.Continent AS Continente, cl.Language AS Idioma, cl.Percentage AS Porcentaje, ROUND(co.Population * (cl.Percentage / 100), 0) AS Hablantes_Por_Idioma FROM country co JOIN  countrylanguage cl ON co.Code = cl.CountryCode ORDER BY ROUND(co.Population * (cl.Percentage / 100), 0)  DESC;"

data_frame6 = obtener_datos_sql(consulta_sql6)
if data_frame6 is not None:
    print(data_frame6)
    data_frame6.info()
    data_frame6['Hablantes_Por_Idioma'] = pd.to_numeric(data_frame6['Hablantes_Por_Idioma'])
data_frame6['Porcentaje'] = pd.to_numeric(data_frame6['Porcentaje'])
data_frame6_mod = data_frame6[(data_frame6['Continente'] == 'Europe') &  (data_frame6['Porcentaje'] >0)]
print(data_frame6_mod)

consulta_sql_PT = "SELECT Name as Pais, Population as Poblacion FROM country WHERE Continent = 'Europe' ORDER BY Population DESC;"

Poblacion_Paises_Europa = obtener_datos_sql(consulta_sql_PT)
if Poblacion_Paises_Europa is not None:
    print(Poblacion_Paises_Europa)
    PobTotalEuropa = Poblacion_Paises_Europa['Poblacion'].sum()
    Poblacion_Por_Idioma_Europa = data_frame6_mod.groupby('Idioma')['Hablantes_Por_Idioma'].sum().reset_index()
print(Poblacion_Por_Idioma_Europa)

Poblacion_Por_Idioma_Europa = Poblacion_Por_Idioma_Europa.sort_values(by='Hablantes_Por_Idioma', ascending=True)
Poblacion_Por_Idioma_Europa['Hablantes_Por_Idioma_%'] = round((Poblacion_Por_Idioma_Europa['Hablantes_Por_Idioma']*100 / PobTotalEuropa),2)
Poblacion_Por_Idioma_Europa['Hablantes_Por_Idioma_millones'] = round(Poblacion_Por_Idioma_Europa['Hablantes_Por_Idioma']/1000000,2)
print(Poblacion_Por_Idioma_Europa)

Poblacion_Por_Idioma_Europa = Poblacion_Por_Idioma_Europa.nlargest(10, 'Hablantes_Por_Idioma_%')
Poblacion_Por_Idioma_Europa = Poblacion_Por_Idioma_Europa.nlargest(10, 'Hablantes_Por_Idioma_millones')
Poblacion_Por_Idioma_Europa = Poblacion_Por_Idioma_Europa.sort_values(by='Hablantes_Por_Idioma_millones', ascending=True)

# Se genero Tabla: Hablantes por idioma respecto del total de Europa (top 10)
plt.figure(figsize=(10, 6))
barras = plt.barh(Poblacion_Por_Idioma_Europa['Idioma'], Poblacion_Por_Idioma_Europa['Hablantes_Por_Idioma_%'], color='darkviolet', edgecolor="purple", linewidth=2)
plt.title('Hablantes por idioma respecto del total de Europa (Top 10)')
plt.xlabel('Porcentaje del total')
plt.ylabel('Idioma')

# generamos las etiquetas en las barras con un bucle
for b in barras:
    xval = b.get_width()
    plt.text(xval + 0.05, b.get_y() + b.get_height()/2, f"{xval:.2f}", ha='left', va='center') 

plt.grid(axis='x')
plt.show()

#Se genero tabla: Hablantes por idioma respecto del total de Europa (top 10)
plt.figure(figsize=(10, 6))
barras = plt.barh(Poblacion_Por_Idioma_Europa['Idioma'], Poblacion_Por_Idioma_Europa['Hablantes_Por_Idioma_%'], color='darkviolet', edgecolor="purple", linewidth=2)
plt.title('Hablantes por idioma respecto del total de Europa (Top 10)')
plt.xlabel('Porcentaje del total')
plt.ylabel('Idioma')

# generamos las etiquetas en las barras con un bucle
for b in barras:
    xval = b.get_width()
    plt.text(xval + 0.05, b.get_y() + b.get_height()/2, f"{xval:.2f}", ha='left', va='center') 

plt.grid(axis='x')
plt.show()
