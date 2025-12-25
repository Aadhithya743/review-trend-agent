import pandas as pd
from datetime import timedelta

print("Loading deduplicated data...")
df = pd.read_csv("data/reviews_deduplicated.csv")

df["date"] = pd.to_datetime(df["date"])

T = df["date"].max()
start_date = T - timedelta(days=30)

print(f"Generating trend from {start_date.date()} to {T.date()}")

filtered_df = df[(df["date"] >= start_date) & (df["date"] <= T)]

trend_table = pd.crosstab(
    filtered_df["final_topic"],
    filtered_df["date"].dt.date
)

trend_table.to_csv("output/trend_report.csv")

print("Trend report generated successfully: output/trend_report.csv")
