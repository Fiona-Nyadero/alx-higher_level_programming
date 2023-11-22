-- List the number of records with the same score in a db table in my MySQL server
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC, score;
