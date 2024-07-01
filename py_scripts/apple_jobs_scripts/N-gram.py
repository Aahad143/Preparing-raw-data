import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('clean_data/apple_jobs_clean.csv')

# Extract the job responsibilities column
texts = df['education&experience'].dropna().tolist()

# Function to generate N-grams
def generate_ngrams(texts, n=2):
    vectorizer = CountVectorizer(ngram_range=(n, n))
    X = vectorizer.fit_transform(texts)
    ngram_counts = X.toarray().sum(axis=0)
    ngram_features = vectorizer.get_feature_names_out()
    return dict(zip(ngram_features, ngram_counts))

# Generate bigrams (2-grams)
bigrams = generate_ngrams(texts, 5)

# Sort the bigrams by frequency
sorted_bigrams = sorted(bigrams.items(), key=lambda x: x[1], reverse=True)

# Display the top 10 bigrams
print(sorted_bigrams[:10])

print(bigrams)

# Function to plot the N-grams
def plot_ngrams(ngram_dict, n=10):
    top_ngrams = dict(sorted(ngram_dict.items(), key=lambda x: x[1], reverse=True)[:n])
    plt.figure(figsize=(10, 6))
    plt.barh(list(top_ngrams.keys()), list(top_ngrams.values()), color='skyblue')
    plt.xlabel('Frequency')
    plt.title(f'Top {n} N-grams')
    plt.gca().invert_yaxis()
    plt.gcf().subplots_adjust(left=0.35)  # Adjust the left padding
    plt.show()

# Plot the top 10 bigrams
plot_ngrams(bigrams, n=10)
