// src/App.js
import React from 'react';
import './App.css';
import FakeNewsDetector from './components/FakeNewsDetector';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Fake News Detection System</h1>
        <p>Identify whether the news content is real or fake instantly</p>
      </header>
      <main>
        <FakeNewsDetector />
      </main>
      <footer>
        <p>Built for educational purposes </p>
      </footer>
    </div>
  );
}

export default App;
