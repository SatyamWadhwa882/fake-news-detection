from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
import traceback  # Added for error tracing

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load the pre-trained model and vectorizer
model_path = 'models/logistic_regression.pkl'
vectorizer_path = 'models/tfidf_vectorizer.pkl'

# Check if model and vectorizer exist before loading
if os.path.exists(model_path) and os.path.exists(vectorizer_path):
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
else:
    raise FileNotFoundError("Model or vectorizer file not found in the specified path.")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        text = data.get('text')
        

        if text:
            # Vectorize the input text
            vectorized_text = vectorizer.transform([text])
            # Predict using the logistic regression model
            prediction = model.predict(vectorized_text)[0]
            # Send a response indicating "Fake News" or "Not Fake News"
            result = "Fake News" if prediction == 0 else "Not Fake News"
            return jsonify({"result": result})
        
        return jsonify({"error": "No text provided"}), 400

    except Exception as e:
        
        # Print full stack trace to the console for debugging
        traceback.print_exc()
        return jsonify({"error": "Error in detection. Please try again.", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
