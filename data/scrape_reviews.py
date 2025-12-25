from google_play_scraper import reviews, Sort
import pandas as pd
from datetime import datetime

APP_ID = "in.swiggy.android"
START_DATE = datetime(2024, 6, 1)
MAX_BATCHES = 10

all_reviews = []
continuation_token = None
batch_count = 0

print("Starting review scraping (safe mode)...")

while batch_count < MAX_BATCHES:
    batch_count += 1
    print(f"Fetching batch {batch_count}...")

    result, continuation_token = reviews(
        APP_ID,
        lang="en",
        country="in",
        sort=Sort.NEWEST,
        count=200,
        continuation_token=continuation_token
    )

    for r in result:
        review_date = r["at"]
        if review_date < START_DATE:
            break

        all_reviews.append({
            "date": review_date.date(),
            "review": r["content"],
            "rating": r["score"]
        })

    if continuation_token is None:
        break

df = pd.DataFrame(all_reviews)
df.to_csv("data/reviews_raw.csv", index=False)

print(f"Scraping finished. Saved {len(df)} reviews")
