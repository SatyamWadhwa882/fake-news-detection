// src/components/FakeNewsDetector.js
import React, { useState } from 'react';
import './FakeNewsDetector.css';

const FakeNewsDetector = () => {
  const [inputText, setInputText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);

    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputText }),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await response.json();
      setResult(data.result);
    } catch (error) {
      console.error("Error:", error);
      setResult("Error in detection. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="detector-container">
      <h2>Enter Text to Detect Fake News</h2>
      <form onSubmit={handleSubmit} className="detector-form">
        <textarea
          placeholder="Enter the news content here..."
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          rows="6"
          required
        ></textarea>
        <button type="submit" disabled={loading} className="detect-button">
          {loading ? 'Detecting...' : 'Detect Fake News'}
        </button>
      </form>
      {result && (
        <div className={`result ${result === 'Fake News' ? 'fake' : 'real'}`}>
          {result}
        </div>
      )}
    </div>
  );
};

export default FakeNewsDetector;
