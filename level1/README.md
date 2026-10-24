# Level 1: Complete Beginner

Goal: get comfortable running code, reading errors, and writing basic SQL. Nothing in this folder has the answers filled in. That's on purpose.

## What's in here

| File | What it's for |
|---|---|
| `games.csv` | nflverse schedule file, every game 1999 through the current 2026 schedule (7,548 rows) |
| `warmup_errors.py` | A broken script. Fix it by reading the error messages, one at a time |
| `part_a.sql` | SQL questions for "My Team's Season" with blank spots for your queries |
| `part_b.py` | Python skeleton for "My Team's Season" with TODOs |

## One-time setup (on your computer)

1. Install Python 3.12+ from python.org (on Windows, tick "Add python.exe to PATH" in the installer).
2. Install VS Code and its Python extension.
3. Install the DuckDB command line tool:
   - Windows: `winget install DuckDB.cli`
   - Mac: `brew install duckdb`
4. Pull this branch, open the `wjd` folder in VS Code, and open a terminal (Terminal > New Terminal).
5. Check it all works:
   ```
   python --version
   duckdb --version
   ```

## Order to do things in

**Step 1: warm-up.** Run `python level1/warmup_errors.py`. It will crash. Read the error from the top down, find the line number, fix that one thing, run it again. Repeat until it runs clean. Don't ask AI to fix it. You're allowed to ask AI "what does this error message mean?"

**Step 2: Part A (SQL).** From the `level1` folder:

```
cd level1
duckdb nfl.duckdb
```

That opens a DuckDB prompt and creates a database file called `nfl.duckdb`. Type the `CREATE TABLE` line from the top of `part_a.sql` yourself, then work through the questions. Type each query into the prompt, and once it works, paste it into `part_a.sql` under the matching question. Type `.quit` to leave. Next time you run `duckdb nfl.duckdb` the `games` table will still be there.

Useful commands inside the DuckDB prompt:

```
DESCRIBE games;              -- every column and its type
SELECT * FROM games LIMIT 5; -- peek at a few rows
```

**Step 3: Part B (Python).** Fill in `part_b.py` and run it with `python level1/part_b.py`.

**Step 4: the milestone.** Close everything. From memory, with no notes, write the query that shows every game your team played in the 2025 season with date, opponent, and both scores, sorted by week. If you can do it cold, you've passed Level 1.

## Column cheat sheet for `games`

| Column | Meaning |
|---|---|
| `season` | Year the season started (the 2025 season includes Jan/Feb 2026 playoff games) |
| `game_type` | `REG` for regular season, `WC`, `DIV`, `CON`, `SB` for playoffs |
| `week` | Week number |
| `gameday` | Date of the game |
| `home_team`, `away_team` | Team abbreviations like `KC`, `PHI`, `LA` (Rams), `LAC`, `LV` |
| `home_score`, `away_score` | Final scores. Empty (`NULL`) for games not played yet |
| `result` | home_score minus away_score |
| `total` | home_score plus away_score |

Heads up: the 2026 season is in progress, so 2026 games that haven't happened yet have no scores. Stick to 2025 for "last season."

## The AI rule for Level 1

AI is a patient explainer only. Good: "Explain what `WHERE` does like I'm new to this." "I got this error, explain what it means but don't fix it." Not okay: "Write the query for question 2."

## Self-check before Level 2

Without running it, what does this return?

```sql
SELECT home_team, away_team, home_score
FROM games
WHERE season = 2024 AND home_score > 30
ORDER BY home_score DESC
LIMIT 5;
```

Write your answer in plain English below, then run it to check yourself.

> My answer:

Also answer in your own words: what's the difference between `=` and `==` in Python?

> My answer:
