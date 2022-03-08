-- display the max temperature of each state
-- SELECT .. AS .. FROM .. GROUP BY .. ORDER BY ..
SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY state
ORDER BY state;
