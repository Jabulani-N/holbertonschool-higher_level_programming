-- script that lists all records of the table second_table
-- score, name associated with it.
-- in order of highest score at top; lowest at bottom.
-- ignore entries without a name
SELECT score, name
FROM second_table
WHERE EXISTS
(SELECT name FROM second_table) AND name IS NOT NULL
ORDER BY score DESC;
