import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading topic data...")
df = pd.read_csv("data/reviews_with_topics.csv")

topics = df["topic"].unique().tolist()

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

topic_embeddings = model.encode(topics)

merged_topics = {}
final_topics = []

SIMILARITY_THRESHOLD = 0.85

for i, topic in enumerate(topics):
    if topic in merged_topics:
        continue

    merged_topics[topic] = topic
    final_topics.append(topic)

    for j in range(i + 1, len(topics)):
        similarity = cosine_similarity(
            [topic_embeddings[i]],
            [topic_embeddings[j]]
        )[0][0]

        if similarity > SIMILARITY_THRESHOLD:
            merged_topics[topics[j]] = topic

df["final_topic"] = df["topic"].map(merged_topics)

df.to_csv("data/reviews_deduplicated.csv", index=False)

print("Semantic topic deduplication completed.")
print(f"Original topics: {len(topics)}")
print(f"Final topics: {len(set(df['final_topic']))}")
