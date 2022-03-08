-- lists all records of the table 'second_table'
-- SELECT .. FROM .. WHERE .. ORDER BY ..
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
