import pandas as pd

INT_COLS = ["draw_size","best_of","minutes","winner_ht","winner_rank","winner_seed",
            "loser_ht","loser_rank","loser_seed"]
FLOAT_COLS = ["winner_age","loser_age"]

df = pd.read_csv("data/atp_2015_results.csv")
# nullable integer dtype so missing values stay clean (no float coercion)
for c in INT_COLS:
    df[c] = df[c].astype("Int64")
for c in FLOAT_COLS:
    df[c] = df[c].astype("float64")
df.to_parquet("data/atp_2015_results.parquet", engine="pyarrow", index=False)

print("rows:", len(df), "cols:", len(df.columns))
print("columns:", list(df.columns))
print("tournaments:", df.tourney_name.nunique())
print("levels:", df.tourney_level.value_counts().to_dict())
print("surfaces:", df.surface.value_counts().to_dict())
print("outcomes:", df.outcome.value_counts().to_dict())
print("date range:", df.tourney_date.min(), "->", df.tourney_date.max())
