# SQL + Python + AI: Learning Path to an NFL Betting Model

Five levels, from zero to building and honestly evaluating your own NFL model. Don't skip levels. Each one sets up the next, and the stuff that feels boring early (data types, joins, checking your work) is exactly what saves you from a model that looks profitable but isn't.

## Before you start: your toolkit

You need four things. Python 3.12 or newer. VS Code as your editor. DuckDB as your database (free, runs locally, speaks normal SQL, and reads CSV and Parquet files directly, so there's no server to set up). And an AI assistant like Claude.

Your data source for the whole journey is **nflverse**. It's free and has play-by-play back to 1999, schedules with final scores, and closing spreads, totals, and moneylines. In Python you get it with the `nflreadpy` package. You can also download the raw files from github.com/nflverse/nflverse-data/releases.

### The AI rule that applies at every level

AI is a tutor and a pair programmer, not a replacement for your brain. The test is simple: **if you can't explain every line of code AI wrote for you, you don't get to use it yet.** Ask it to explain, ask it to quiz you, ask it why. How you use AI changes as you level up, and each level below spells out how.

---

## Level 1: Complete Beginner

**1. Level name:** Complete Beginner. You're learning what code and databases even are.

**2. What you should understand at this stage**

A database is a set of tables, and a table is rows and columns, like a spreadsheet with strict rules. Every column has a type (number, text, date) and SQL is how you ask the database questions. Python is a general-purpose language: it can do math, make decisions, repeat things, read files, and eventually talk to your database. You don't need to understand pandas, models, or statistics yet. You need to be comfortable with the idea that a computer does exactly what you tell it, nothing more.

**3. What mastery looks like**

You can open a terminal, run a Python file, and fix a simple error by reading the message. You can write a SQL query that pulls specific columns from a table, filters rows, and sorts the result, without looking it up. You can also explain the difference between `=` and `==` in Python.

**4. Most important concepts and skills**

For SQL: `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `LIMIT`, plus `AND`/`OR` and comparison operators. For Python: variables, the basic types (int, float, string, bool), `print`, `if/elif/else`, `for` loops, lists, and dictionaries. Also learn to read an error message top to bottom, because the last line usually tells you what broke. For AI, use it only as a patient explainer. Good prompts at this stage look like "Explain what this line does like I'm new to programming" or "I got this error, explain what it means but don't fix it for me."

**5. Milestone that proves you're ready to move on**

Load the nflverse schedules CSV into DuckDB and, from memory, write a query that shows every game your favorite team played last season with the date, opponent, and both scores, sorted by week.

**6. Hands-on exercise: "My Team's Season"**

Part A (SQL): In DuckDB, run `CREATE TABLE games AS SELECT * FROM 'games.csv';` using the nflverse schedule file. Then answer three questions with queries: which games did your team play at home, which games were decided by 3 points or fewer, and which games had a total score over 50.

Part B (Python): Without pandas, write a script with a list of your team's final scores as dictionaries, like `{"week": 1, "us": 24, "them": 20}`. Loop through it and print the record (wins and losses), the average points scored, and the biggest win.

**7. Common mistakes at this level**

Copy-pasting code you don't understand because it ran. Rushing to "build the model" before you can write a basic query. Ignoring error messages instead of reading them. Using Excel brain in SQL (expecting to click on things instead of describing what you want). And letting AI write everything, which feels fast and leaves you knowing nothing a week later.

**8. Self-check before moving on**

Without running it, what does this return?

```sql
SELECT home_team, away_team, home_score
FROM games
WHERE season = 2024 AND home_score > 30
ORDER BY home_score DESC
LIMIT 5;
```

If you can say "the five highest-scoring home performances from 2024 where the home team scored more than 30, showing who played and the home score," you're ready.

---

## Level 2: Basic Understanding

**1. Level name:** Basic Understanding. You start summarizing data instead of just looking at it.

**2. What you should understand at this stage**

Raw rows aren't insights. Insights come from grouping and aggregating ("average points per game by team") and from combining tables ("join game results with team info"). In Python you move from loose scripts to functions, and you start using pandas, which is basically SQL-style thinking inside Python. You should also understand what a point spread actually is: if the Chiefs are -6.5, they need to win by 7 or more to "cover."

**3. What mastery looks like**

You can answer most "per team" or "per season" questions with `GROUP BY`. You can join two tables and explain why the row count changed. You can write a Python function that takes inputs and returns a value, and you can load a CSV into a pandas DataFrame, filter it, and group it.

**4. Most important concepts and skills**

For SQL: aggregate functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`), `GROUP BY`, `HAVING` vs `WHERE`, `INNER JOIN` vs `LEFT JOIN`, `CASE WHEN`, and handling `NULL`. For Python: writing functions, `import`, installing packages with pip, virtual environments (`python -m venv .venv`), and pandas basics (`read_csv`, selecting columns, filtering, `groupby`, `merge`). For betting basics: spreads, totals (over/under), moneylines, and how to convert American odds to implied probability. For AI, start asking it to generate practice problems and review your code: "Here's my query, is it correct? Don't rewrite it, just tell me what's wrong."

**5. Milestone that proves you're ready to move on**

Write one SQL query that returns every team's against-the-spread (ATS) record for a season: wins, losses, and pushes. Then reproduce the exact same numbers in pandas. If the two disagree, figure out why.

**6. Hands-on exercise: "ATS Leaderboard"**

Using the schedules table (it has `spread_line`, `home_score`, `away_score`), add a column with `CASE WHEN` that labels each game as home cover, away cover, or push. Heads up: nflverse's `spread_line` is from the home team's perspective as a positive number when home is favored, so check the docs and sanity-check a few games by hand before trusting your logic. Then group by team to build the leaderboard. Note that each team appears as home in some games and away in others, so you'll need to handle both (a `UNION ALL` of home rows and away rows is the clean way). Finally, write a Python function `american_to_prob(odds)` that turns -110 into about 0.524 and +150 into 0.40.

**7. Common mistakes at this level**

Getting the spread sign backwards, which silently flips every result. Joining tables and not noticing that rows got duplicated or dropped. Putting aggregate conditions in `WHERE` instead of `HAVING`. Skipping virtual environments and ending up with package chaos. Trusting a number without spot-checking it against a game you can look up.

**8. Self-check before moving on**

You join a `games` table (285 rows) to a `team_info` table on `home_team` and get 270 rows back with an `INNER JOIN`. What probably happened, and what would a `LEFT JOIN` show you? (Answer: some team abbreviations don't match, like old franchise codes such as OAK vs LV or SD vs LAC. A `LEFT JOIN` keeps all 285 games and shows `NULL`s where the match failed, which tells you exactly which ones.)

---

## Level 3: Practical User

**1. Level name:** Practical User. You build a real data pipeline and start doing actual football analysis.

**2. What you should understand at this stage**

Real analysis is a pipeline: get data, clean it, store it, transform it, analyze it. Play-by-play data is huge (about 50,000 plays per season), so you summarize it into team-level stats per game. You should understand why efficiency stats like EPA per play (expected points added) tell you more than yards or points. You also need to understand **time**: a stat for Week 10 can only use information from Weeks 1 through 9. That idea becomes life or death for your model later.

**3. What mastery looks like**

You have a script that pulls multiple seasons of nflverse data and loads it into a DuckDB file. You can write multi-step SQL using CTEs that's still readable a month later. You can build rolling averages with window functions. You make basic charts in Python to check whether your numbers look sane.

**4. Most important concepts and skills**

For SQL: CTEs (`WITH ... AS`), window functions (`ROW_NUMBER`, `LAG`, `AVG() OVER (PARTITION BY ... ORDER BY ... ROWS BETWEEN ...)`), and creating your own tables and views. For Python: connecting Python to DuckDB (`duckdb.connect`, then `.df()` to get a DataFrame), organizing code into multiple files, reading and writing Parquet, and plotting with matplotlib. Also start using git so you can undo mistakes and see your progress. For football: EPA, success rate, pass rate over expected, and why turnovers are noisy. For AI, it becomes a pair programmer now. Write the plan yourself, then let it help with syntax: "I want a 4-game rolling average of offensive EPA per play for each team, excluding the current game. Here's my table schema. Write the window function and explain each part."

**5. Milestone that proves you're ready to move on**

Build a table with one row per team per game containing that team's offensive and defensive EPA per play **using only games before that one**. Pick any game and verify by hand that the numbers don't include that game's own data.

**6. Hands-on exercise: "Team Power Ratings"**

Write `load_data.py` that pulls play-by-play and schedules for 2018 through the latest season into `nfl.duckdb`. Then write SQL that turns play-by-play into a `team_game_stats` table (offensive EPA/play, defensive EPA/play, success rate, plays). Add rolling season-to-date averages with window functions, shifted so the current game is excluded. Rank teams by net EPA (offense minus defense) going into Week 10 of last season. Make a scatter plot of offensive vs defensive EPA. Then compare your rankings to the betting market: do teams you rank high tend to be favored? They should, mostly. If they aren't, look for a bug.

**7. Common mistakes at this level**

**Lookahead leakage**: using a full-season average to describe a Week 5 game. This is the number one mistake in sports modeling and it makes everything look amazing in backtests. Forgetting to filter play-by-play down to real plays (exclude kneels, spikes, penalties with no play, and so on, depending on your goal). Writing one 400-line query instead of breaking it into CTEs. Not saving the raw data, so every run re-downloads everything. And asking AI to "build me an NFL model" and getting a pile of code you can't debug.

**8. Self-check before moving on**

Your rolling average uses `ROWS BETWEEN 3 PRECEDING AND CURRENT ROW`. Why is that wrong for predicting the current game, and how do you fix it? (Answer: it includes the game you're trying to predict. Use `ROWS BETWEEN 4 PRECEDING AND 1 PRECEDING`, or calculate it and then `LAG` it by one game.)

---

## Level 4: Problem Solver

**1. Level name:** Problem Solver. You build your first actual model and learn to test it honestly.

**2. What you should understand at this stage**

A model takes features (things you know before kickoff) and predicts a target (point margin, cover or not, total points). The key question isn't "is my model accurate?" It's **"is my model better than the closing line?"** The market is very efficient. Betting -110 on both sides means you need to win about 52.4% of bets just to break even. You need to understand train/test splits done by time, why random splits are cheating with time series data, and what overfitting looks like.

**3. What mastery looks like**

You can build a feature table, train a simple model (linear regression for margin, logistic regression for win/cover probability), backtest it on seasons it never saw, and report results honestly: ATS win rate, sample size, and ROI at -110. You can debug your own pipeline when results look too good. You can read AI-generated code critically and catch when it's wrong.

**4. Most important concepts and skills**

For Python: scikit-learn (`LinearRegression`, `LogisticRegression`, `train_test_split` and why you shouldn't use its default shuffle here), evaluation metrics (mean absolute error for margins, log loss and Brier score for probabilities), and walk-forward backtesting (train on 2018 to 2021, test on 2022; then train on 2018 to 2022, test on 2023; and so on). For SQL: building a clean final "model input" view that joins features for both teams in each game. For stats: baselines, variance, sample size, and why 30 bets proves nothing. For betting: closing line value (CLV), vig, and expected value. For AI, use it as a reviewer and a skeptic: "Here's my backtest code. Look specifically for lookahead bias or data leakage." Or "My model hits 61% ATS. List every reason this might be fake."

**5. Milestone that proves you're ready to move on**

A walk-forward backtest over at least three held-out seasons that compares your predicted margin to the closing spread, with a written one-page summary of results, including the honest admission if it doesn't beat the market. Most first models don't. That's normal and still counts as passing.

**6. Hands-on exercise: "Model v1 vs the Closing Line"**

Build a `model_input` view: one row per game, with home and away rolling EPA stats, rest days, home field, and the closing spread. Target: actual home margin. Train a linear regression on 2018 through 2021. Predict 2022. For each game, compare your predicted margin to the spread. When your model disagrees with the line by 3 or more points, record a "bet" on your side. Calculate win rate and ROI at -110. Then do the same walk-forward for 2023 and 2024. Finally, check the simplest possible baseline: how does "always bet the home team" or "always take the underdog" do? If your model can't beat those, that's important information.

**7. Common mistakes at this level**

Random train/test splits (future games leak into training). Tuning the model over and over on the same test season until it looks good, which is just overfitting with extra steps. Celebrating a hot small sample. Using closing-line-derived features to bet at opening numbers (or vice versa) without accounting for it. Ignoring vig in ROI math. Adding 80 features because more must be better. And trusting AI's confident explanation of why your model works when it's actually picking up a leak.

**8. Self-check before moving on**

Your model went 58-42 ATS in its test season. Is it a winning model? (Answer: not proven. 100 bets at a true 52.4% rate will land at 58% or better by pure luck a decent fraction of the time. You'd want multiple seasons, a larger sample, and ideally evidence you beat the closing line, not just the scoreboard. Ask AI to help you compute a confidence interval or run a quick simulation, then make sure you understand the result.)

---

## Level 5: Confident Practitioner

**1. Level name:** Confident Practitioner. You run a maintainable system, make good decisions with uncertainty, and use AI as a force multiplier rather than a crutch.

**2. What you should understand at this stage**

A model is a product, not a script. It needs fresh data every week, reproducible results, monitoring, and a betting process with discipline around it. You understand that edge in NFL sides and totals is small and fragile, that player-level info (QB injuries especially) moves lines more than almost anything, and that bet sizing matters as much as picks. You know when a model is genuinely telling you something and when it's noise.

**3. What mastery looks like**

Every Tuesday, one command refreshes your data, rebuilds features, retrains if needed, and spits out next week's predictions next to the current lines. You track every bet with the line you got and the closing line, so you can measure CLV. You can explain your model's logic to someone else, defend its weaknesses, and improve it without breaking it. You use AI to move faster on things you already understand, and you can tell when its output is wrong.

**4. Most important concepts and skills**

For engineering: project structure (`data/`, `src/`, `sql/`, `notebooks/`), config files instead of hardcoded values, logging, simple tests on your data (no duplicate games, no `NULL` spreads, every team has the right number of games), and git with meaningful commits. For modeling: probability calibration, ensembles of simple models, QB-adjusted ratings, regression to the mean early in the season, and comparing against market-implied probabilities. For betting: Kelly criterion (and fractional Kelly, because full Kelly is brutal), bankroll management, and line shopping. For SQL: query performance on larger data, and data quality checks written as SQL. For AI: delegating whole well-specified tasks ("Write pytest tests for this feature function covering a bye week and a team's first game of the season"), using it for code review before you commit, and asking it to argue against your conclusions.

**5. Milestone that proves you've arrived**

Run your full system live (on paper or small stakes) for a stretch of the season: predictions logged before kickoff, every bet recorded with your line and the closing line. At the end, write an honest review covering record, ROI, CLV, what broke, and what you'd change. Beating the closing line on average is the real signal, more than win rate.

**6. Hands-on project: "The Weekly Machine"**

Build `run_week.py` that does the full loop: pull the latest nflverse data, run data quality checks (and stop loudly if they fail), rebuild features in DuckDB, generate predictions for upcoming games, compare to current lines (entered manually or from a source you're allowed to use), flag games where your edge clears a threshold you picked during backtesting, and write a clean report. Add a `bets` table in DuckDB where you log each bet, then a query that computes your running ROI and average CLV. Add one meaningful upgrade to the model, like a QB adjustment for injuries or early-season regression toward last year's rating, and prove with a backtest that it helped.

**7. Common mistakes at this level**

Constantly tweaking the model mid-season based on last week's results. Overbetting because the backtest looked good. Measuring success by win/loss record instead of CLV and long-run ROI. Letting the codebase become a mess of `final_v2_REAL.py` files (you've done this before with the mortgage calculator commits, so you know the feeling). Letting AI make large changes you don't review. And forgetting that real money is at stake: never bet more than you can afford to lose, and remember that most bettors, including most model bettors, lose long term.

**8. Self-check: are you truly there?**

Your model loves the Bears +4 this week. The line was +6 when the week opened and it's now +4. What does that tell you, and what do you do? (Answer: the market moved toward your side, meaning other sharp money likely agrees, but you've also lost 2 points of value. Bet it only if your edge still clears your threshold at +4. Then log it, and check later whether it closed at +3.5 or lower, which would mean you got positive CLV even at +4.) If you can reason through that calmly, with numbers, you're a confident practitioner.

---

## Rough timeline

Assuming 5 to 7 hours a week: Level 1 takes about 2 to 4 weeks, Level 2 about 4 to 6 weeks, Level 3 about 6 to 8 weeks, Level 4 about 2 to 3 months, and Level 5 is ongoing. Starting now (late October) means you'll be building Level 3 and 4 work during the offseason with plenty of historical data, which is honestly the ideal time, and you can go live with Level 5 next September.
