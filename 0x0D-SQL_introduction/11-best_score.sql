-- list all records with a score >= 10 int the table 'second_table', order by score
-- SELECT .. FROM .. WHERE .. ORDER BY .. DESC
SELECT score, name
FROM second_table
WHERE score>=10
ORDER BY score DESC;
