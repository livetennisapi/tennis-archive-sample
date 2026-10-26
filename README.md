---
license: cc-by-4.0
pretty_name: ATP 2015 Tour-Level Singles Results
language:
  - en
task_categories:
  - tabular-classification
  - tabular-regression
  - time-series-forecasting
tags:
  - tennis
  - sports
  - atp
  - sports-analytics
  - match-results
size_categories:
  - 1K<n<10K
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/atp_2015_results.parquet
---

# ATP 2015 Tour-Level Singles Results

A clean, ready-to-use table of **every 2015 ATP tour-level men's singles match** —
4,479 matches across 66 tournaments (Grand Slams, Masters 1000, ATP 250/500 events,
and the season-ending ATP Finals). One row per match, with tournament context, both
players' identifiers, seeding and ranking, the final score, and the match outcome.

## Who publishes this (vendor disclosure)

This dataset is published by **Live Tennis API** (<https://livetennisapi.com>), the
commercial tennis data provider that runs the API of the same name. It is a **first-party
sample** drawn from our historical archive (men's and women's professional results,
1968–2022). We are the vendor, so treat this card as vendor-authored and judge it on the
data, which you can inspect directly in the files.

## This is a sample

This release is deliberately **one ATP season of match-level results** — a taste of the
archive, not the whole thing. The full 1968–2022 archive (both tours, all levels, plus
per-match statistics, head-to-head, and point-by-point tape as separate products) is
available through the Live Tennis API:

- Product & pricing: <https://livetennisapi.com>
- API documentation: <https://docs.livetennisapi.com>
- Free keyed tier (develop-and-test): <https://livetennisapi.com/subscribe/free>

The sample contains **match results only** — it does not include point-by-point data or
in-play statistics, which are separate paid products.

## Dataset at a glance

| | |
|---|---|
| Rows (matches) | 4,479 |
| Columns | 26 |
| Tournaments | 66 |
| Tour / gender | ATP (men's) |
| Discipline | Singles |
| Season | 2015 (2015-01-04 → 2015-11-15) |
| Levels | Grand Slam (956), Masters 1000 (783), ATP 250/500 (2,725), Tour Finals (15) |
| Surfaces | hard (2,487), clay (1,423), grass (569) |
| Outcomes | completed (4,329), retired (138), walkover (12) |
| Format | CSV + Parquet |
| License | CC-BY-4.0 |

## Files

- `data/atp_2015_results.csv` — UTF-8, header row, one match per line.
- `data/atp_2015_results.parquet` — same data, typed columns (nullable integers for
  missing ranks/seeds/heights), for direct loading with pandas / `datasets`.

## Column dictionary

| Column | Type | Description |
|---|---|---|
| `tourney_name` | string | Tournament name (e.g. `Brisbane`, `Australian Open`). |
| `tourney_level` | string | Event tier: `G` = Grand Slam, `M` = Masters 1000, `A` = ATP Tour 250/500, `F` = ATP (Tour) Finals. |
| `surface` | string | Court surface: `hard`, `clay`, or `grass`. |
| `draw_size` | int | Number of players in the singles draw. |
| `tourney_date` | date | Tournament start date, `YYYY-MM-DD` (shared by all matches in that event). |
| `round` | string | Round: `R128`, `R64`, `R32`, `R16`, `QF`, `SF`, `F`, plus `RR`/`BR` for round-robin events. |
| `best_of` | int | Maximum sets (`3` or `5`). |
| `minutes` | int, nullable | Match duration in minutes (present for ~52% of 2015 matches). |
| `winner_name` | string | Match winner. |
| `winner_hand` | string | Winner's playing hand: `R`, `L`, or `U` (unknown). |
| `winner_ht` | int, nullable | Winner's height in cm. |
| `winner_ioc` | string | Winner's country (IOC 3-letter code, e.g. `SUI`). |
| `winner_age` | float, nullable | Winner's age in years at the tournament date. |
| `winner_rank` | int, nullable | Winner's ATP singles ranking at the tournament date. |
| `winner_seed` | int, nullable | Winner's tournament seed (null if unseeded). |
| `winner_entry` | string, nullable | Winner's entry type: `WC` wild card, `Q` qualifier, `LL` lucky loser, `PR` protected ranking, `SE` special exempt, `ALT` alternate; blank = direct acceptance. |
| `loser_name` | string | Match loser. |
| `loser_hand` | string | Loser's playing hand: `R`, `L`, or `U`. |
| `loser_ht` | int, nullable | Loser's height in cm. |
| `loser_ioc` | string | Loser's country (IOC 3-letter code). |
| `loser_age` | float, nullable | Loser's age in years at the tournament date. |
| `loser_rank` | int, nullable | Loser's ATP singles ranking at the tournament date. |
| `loser_seed` | int, nullable | Loser's tournament seed (null if unseeded). |
| `loser_entry` | string, nullable | Loser's entry type (see `winner_entry`). |
| `score` | string | Final score from the winner's perspective, e.g. `6-3 6-1`; tiebreak points in parentheses, e.g. `7-6(4)`. |
| `outcome` | string | `completed`, `retired` (loser retired), or `walkover`. |

Notes on missing values: `winner_rank`/`loser_rank` are null when a player had no ranking
at that date (e.g. protected-ranking or wild-card entries); `winner_seed`/`loser_seed` are
null for unseeded players; `minutes` and heights are null where the archive lacks the
value. Missing values are empty in the CSV and null (nullable-integer) in the Parquet.

## Usage

```python
from datasets import load_dataset

ds = load_dataset("livetennisapi/atp-2015-results", split="train")
print(ds[0])
```

Or straight from the Parquet with pandas:

```python
import pandas as pd

df = pd.read_parquet("data/atp_2015_results.parquet")
# Federer's 2015 matches
fed = df[(df.winner_name == "Roger Federer") | (df.loser_name == "Roger Federer")]
print(len(fed), "matches")
```

## Source & methodology

Rows are exported directly from the Live Tennis API historical archive (the same store
that backs the API's `/archive` endpoints). The scope filter is: ATP tour (men's),
singles, event levels Grand Slam / Masters 1000 / ATP 250-500 / Tour Finals, calendar year
2015. No rows are synthetic or interpolated — every match is a real recorded result. Player
ages, heights, ranks, and seeds are the archive's stored values as of each tournament date.

## License — CC-BY-4.0

This dataset is licensed under the
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
You are free to **share and adapt** the data, **including for commercial use**, provided you
give appropriate credit.

**Required attribution:**

> Data: Live Tennis API (https://livetennisapi.com), ATP 2015 Tour-Level Singles Results,
> licensed under CC-BY-4.0.

Copyright (c) Live Tennis API (https://livetennisapi.com). See the [`LICENSE`](./LICENSE) file for the full license text.

## Citation

```bibtex
@misc{livetennisapi_atp_2015,
  title  = {ATP 2015 Tour-Level Singles Results},
  author = {Live Tennis API},
  year   = {2015},
  note   = {First-party sample of the 1968--2022 tennis archive},
  url    = {https://livetennisapi.com}
}
```
