# Ejercicio 1: Escribe una consulta para mostrar el nombre y la población de todos los países del continente europeo

SELECT Name as Nombre, Continent as Continente, Population as Población
FROM country
WHERE Continent = 'Europe';



# Ejercicio 2: Escribe una consulta para mostrar los nombres y las áreas de superficie de los cinco países más grandes 
# del mundo (en términos de área de superficie).

SELECT Name as Nombre, SurfaceArea as Superficie
FROM country
ORDER BY SurfaceArea desc
LIMIT 5;


# Ejercicio 3: Escribe una consulta para calcular la población total de todos los países de cada continente y mostrar el 
# resultado junto con el nombre del continente.

SELECT Continent,FORMAT(sum(population), 0, "de_DE") as PoblaciónTotal
FROM country
GROUP BY continent
ORDER BY sum(population) DESC;


# Ejercicio 4: Escribe una consulta para mostrar el nombre de las ciudades y la población de todos los países de Europa, 
# ordenados por población de la ciudad de manera descendente.

SELECT ci.name as City, ci.population as Population, co.name as Country
FROM city as ci
LEFT JOIN country as co ON ci.countrycode = co.code
WHERE co.continent = 'Europe'
ORDER BY ci.POPULATION desc; 


# Ejercicio 5: Actualiza la población de China (código de país 'CHN') a 1500000000 (1.5 mil millones).

SELECT name, code, population 
FROM country
WHERE code = 'CHN';

UPDATE country
SET population = 1500000000
WHERE code = 'CHN';