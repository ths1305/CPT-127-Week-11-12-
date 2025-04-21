# Import libraries
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Downloads and runs lexicon library for analysis
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Scrapes from National Geographic
url = "https://www.nationalgeographic.com/pages/topic/latest-stories"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# Looks for the link element shared by all headlines on the page
head_elements = soup.find_all("a")

# Ensures there will be no repeated headlines in the analysis
headlines = []
seen = set()
for tag in head_elements:
    text = tag.get_text(strip=True)
    if text not in seen and len(text.split()) > 3:
        seen.add(text)
        headlines.append(text)

headlines = list(set(headlines))

# Deciding the math for sentiment analysis
def label_sentiment(compound):
    if compound >= 0.01:
        return "Positive"
    elif compound <= -0.01:
        return "Negative"
    else:
        return "Neutral"

# Records the amount of headlines that pertain to each sentiment    
positive_head = 0
negative_head = 0
neutral_head = 0

# Prints the number of articles analyzed   
print(f"An Analysis of {len(headlines)} National Geographic Pages:")

# Determines the whether the sentiment of a given headline is positive or negative
for headline in headlines:
    score = sia.polarity_scores(headline)
    label = label_sentiment(score["compound"])
    if label == "Positive":
        positive_head += 1
    elif label == "Negative":
        negative_head += 1
    else:
        neutral_head += 1
# Displays important data allowing us to tell which articles have what compound scores and labels
    print(f"Article Headline: {headline}")
    print(f"Score: {score}")
    print(f"Label: {label}")

# Prints the outputs of the individual sentiment scores
print("\nSentiment Scores:")
print(f"Positive Articles: {positive_head}")
print(f"Negative Articles: {negative_head}")
print(f"Neutral Articles: {neutral_head}")