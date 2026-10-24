-- Level 1, Part A: My Team's Season (SQL)
--
-- Run these inside the DuckDB prompt (duckdb nfl.duckdb from the level1 folder).
-- Once a query works, paste it under its question so you have a record.

-- Step 0: load the CSV into a table. Type this one yourself, don't paste it.
--   CREATE TABLE games AS SELECT * FROM 'games.csv';
-- Then look around:
--   DESCRIBE games;
--   SELECT * FROM games LIMIT 5;

-- My team's abbreviation:
-- Season I'm looking at: 2025


-- Q1. Which games did my team play at home in 2025?
--     Show the week, date, opponent, and both scores. Sort by week.



-- Q2. Which of my team's 2025 games were decided by 3 points or fewer?
--     Hint: your team could be home OR away, so you'll need OR,
--     and parentheses matter when you mix AND with OR.



-- Q3. Which of my team's 2025 games had a total score over 50?



-- Bonus (no peeking at the hints for this one):
-- Q4. Across ALL teams in 2025, list the 10 highest-scoring regular season games.



-- Q5. Every 2025 game where the road team scored 40 or more.
