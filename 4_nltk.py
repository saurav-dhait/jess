import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

def process_text(text):
    tokens = word_tokenize(text.lower())
    print(tokens)
    stopwords_list = set(stopwords.words('english'))
    print(stopwords_list)
    tokens = [word for word in tokens if word.isalnum() and word not in stopwords_list]
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    return stemmed_tokens

# Example usage:
text = "NLTK is a leading platform for building Python programs to work with human language data."
processed_tokens = process_text(text)
print("\nProcessed Tokens:")
print(processed_tokens)