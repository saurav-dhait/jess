from sklearn.feature_extraction.text import CountVectorizer

texts = [
    "I love machine learning.",
    "Machine learning is amazing.",
    "I love coding in Python."
]


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

print("Feature Names:", vectorizer.get_feature_names_out(), "\n")

print("BoW Matrix:\n", X.toarray(), "\n")

word_freq = X.toarray().sum(axis=0)
features = vectorizer.get_feature_names_out()
for word, freq in zip(features, word_freq):
    print(f"{word}: {freq}")