from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression

texts = [
    "I loved the movie, it was amazing!",
    "Fantastic film with a great story.",
    "Terrible movie, I hated it.",
    "The plot was boring and predictable.",
    "What a wonderful experience!",
    "Worst movie I've seen in years.",
    "That was a very enjoyable movie!",
    "The suspense in the film was thrilling.",
    "Not a single exciting moment in it.",
    "Enjoyable and full of surprises."
]
labels = ['pos', 'pos', 'neg', 'neg', 'pos', 'neg', 'pos', 'pos', 'neg', 'pos']

model = make_pipeline(TfidfVectorizer(), LogisticRegression())
model.fit(texts, labels)

test_text = "Terrible movie, I hated it."
prediction = model.predict([test_text])

print("Predicted sentiment:", prediction[0])
