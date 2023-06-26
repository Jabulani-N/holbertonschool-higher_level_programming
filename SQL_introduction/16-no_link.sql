-- script that lists all records with a score >= 10 in the table second_table
-- score, name associated with it.
-- in order of highest score at top; lowest at bottom.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC; -- not changed from task11 yet
