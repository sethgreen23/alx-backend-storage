-- rank countries by fans count

SELECT origin, COUNT(fans) AS nb_fans FROM metal_bands GROUP BY origin  ORDER BY nb_fans DESC;
