import pandas as pd

def extract_topic(review):
    review = str(review).lower()

    if any(word in review for word in ["rude", "impolite", "behave badly", "bad behavior"]):
        return "Delivery partner rude"

    if any(word in review for word in ["late", "delay", "delayed"]):
        return "Delivery delay"

    if any(word in review for word in ["cold", "stale", "spoiled"]):
        return "Food quality issue"

    if "refund" in review or "money back" in review:
        return "Refund issue"

    if any(word in review for word in ["crash", "not working", "bug", "error"]):
        return "App technical issue"

    return "Other feedback"


print("Loading reviews...")
df = pd.read_csv("data/reviews_raw.csv")

df["topic"] = df["review"].apply(extract_topic)

df.to_csv("data/reviews_with_topics.csv", index=False)

print("Topic extraction completed. Saved reviews_with_topics.csv")
