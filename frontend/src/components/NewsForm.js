// frontend/src/components/NewsForm.js
import React, { useState } from 'react';
import axios from 'axios';

function NewsForm() {
  const [newsText, setNewsText] = useState('');
  const [prediction, setPrediction] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/predict', {
        news_text: newsText,
      });
      setPrediction(response.data.prediction);
    } catch (error) {
      setPrediction("Error detecting news");
      console.error(error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <textarea
          value={newsText}
          onChange={(e) => setNewsText(e.target.value)}
          placeholder="Enter news text here"
          rows="5"
          cols="50"
        />
        <button type="submit">Check News</button>
      </form>
      
      {prediction && (
        <div>
          <h3>Prediction:</h3>
          <p>{prediction}</p>
        </div>
      )}
    </div>
  );
}

export default NewsForm;
