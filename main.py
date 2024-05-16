import pandas as pd
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Define your stop words and positive/negative word lists (this is a placeholder)
stop_words = set(stopwords.words('english'))
positive_words = set(["good", "great", "excellent", "positive"])  # Load from your MasterDictionary
negative_words = set(["bad", "worst", "negative", "poor"])  # Load from your MasterDictionary

def clean_text(text):
    tokens = word_tokenize(text)
    tokens = [word.lower() for word in tokens if word.isalpha()]
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

def calculate_scores(text):
    words = clean_text(text)
    pos_score = sum(1 for word in words if word in positive_words)
    neg_score = sum(1 for word in words if word in negative_words)
    polarity_score = (pos_score - neg_score) / ((pos_score + neg_score) + 0.000001)
    subjectivity_score = (pos_score + neg_score) / (len(words) + 0.000001)
    return pos_score, neg_score, polarity_score, subjectivity_score

def scrape_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    article = soup.find('article')
    if article:
        return article.text.strip()
    return ""

# Load the input Excel file with URLs
data = pd.read_excel('Input.xlsx')

# Prepare a DataFrame to store results
results = []

for index, row in data.iterrows():
    url_id = row['URL_ID']  # Assuming there is a column 'URL_ID'
    url = row['URL']        # Assuming there is a column 'URL'
    text = scrape_text(url)
    pos_score, neg_score, polarity_score, subjectivity_score = calculate_scores(text)
    results.append({
        'URL_ID': url_id,
        'URL': url,
        'Positive Score': pos_score,
        'Negative Score': neg_score,
        'Polarity Score': polarity_score,
        'Subjectivity Score': subjectivity_score
    })

# Convert results to a DataFrame
results_df = pd.DataFrame(results)

# Save the results to an Excel file
results_df.to_excel('Output Data Structure.xlsx', index=False)

print("Data extraction and analysis complete. Results saved to 'Output Data Structure.xlsx'.")
