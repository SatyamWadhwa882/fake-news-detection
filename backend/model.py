import os
import pandas as pd
import joblib
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load and preprocess data
# Assuming the data files Fake.csv and True.csv are in the same directory
data_fake = pd.read_csv(r'C:\Users\LENOVO\Downloads\Fake-News-Detection-main\Datasets\datasets\Fake.csv')
data_true = pd.read_csv(r'C:\Users\LENOVO\Downloads\Fake-News-Detection-main\Datasets\datasets\True.csv')

# Assign labels: 0 for fake news, 1 for true news
data_fake["class"] = 0
data_true["class"] = 1

# Combine the datasets
data = pd.concat([data_fake, data_true], axis=0)
data = data.sample(frac=1).reset_index(drop=True)  # Shuffle the data

# Text preprocessing function
def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W", " ", text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

# Apply preprocessing to the text data
data['text'] = data['text'].apply(wordopt)

# Split data into features and labels
X = data['text']
y = data['class']

# Split into training and test sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Vectorize text using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
xv_train = vectorizer.fit_transform(x_train)

# Train Logistic Regression model
LR = LogisticRegression()
LR.fit(xv_train, y_train)

# Ensure the models directory exists
os.makedirs('models', exist_ok=True)

# Save the trained model and vectorizer
joblib.dump(LR, 'models/logistic_regression.pkl')
joblib.dump(vectorizer, 'models/tfidf_vectorizer.pkl')

print("Model and vectorizer saved successfully.")
