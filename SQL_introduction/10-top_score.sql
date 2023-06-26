-- script that lists all records of the table second_table
-- each name's top score, and the name to the right of it
-- name as well.
-- in order of highest score at top; lowest at bottom.
SELECT score, name FROM second_table ORDER BY score DESC
