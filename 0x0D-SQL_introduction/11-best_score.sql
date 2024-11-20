-- Lists all records from second_table with score >= 10, ordered by a score descending
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
