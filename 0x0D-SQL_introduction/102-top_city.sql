-- Display the top 3 cities with the highest average temperatures in July and August
SELECT city, 
	ROUND(AVG(temperature), 4) AS avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
