-- List all records with a name value in a db table on my MySQL server
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
