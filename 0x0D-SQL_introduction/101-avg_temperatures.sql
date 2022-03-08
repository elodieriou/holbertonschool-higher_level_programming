-- displays the average temperature by city ordered by temperature
-- SELECT .. AS .. FROM .. GROUP BY .. ORDER BY ..
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
