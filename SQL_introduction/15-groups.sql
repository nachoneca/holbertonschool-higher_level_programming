-- Count and order scores in a new field called number from a table and groups all the scores repited
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;