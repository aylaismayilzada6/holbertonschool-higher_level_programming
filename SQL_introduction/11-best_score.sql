-- Lists all records with a score >= 10 in second_table
-- Results display score and name, ordered by score (top first)
SELECT score, table  FROM second_table WHERE score >= 10 ORDER BY score DESC;
