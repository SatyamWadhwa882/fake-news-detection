# Fake News Detection

A machine learning project to detect fake news using NLP and logistic regression.

## Features

- Flask backend API for predictions
- Pre-trained model and TF-IDF vectorizer
- CORS enabled for frontend integration

## Installation

```sh
git clone https://github.com/SatyamWadhwa882/fake-news-detection.git
cd "fake news"
pip install -r requirements.txt
```

## Usage

Start the Flask server:
```sh
python backend/app.py
```
Send a POST request to `/predict` with JSON:
```json
{ "text": "Your news text here" }
```

## Project Structure

```
fake news/
├── backend/
│   └── app.py
├── models/
│   ├── logistic_regression.pkl
│   └── tfidf_vectorizer.pkl
├── requirements.txt
└── README.md
```

## License

MIT