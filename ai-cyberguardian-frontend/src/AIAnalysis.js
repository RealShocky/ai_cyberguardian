import React, { useState } from 'react';
import api from './services/api';

function AIAnalysis() {
  const [input, setInput] = useState('');
  const [result, setResult] = useState('');

  const handleAnalysis = async () => {
    try {
      const token = localStorage.getItem('token');
      const response = await api.post('/ai-analysis', { input }, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setResult(response.data.result);
    } catch (error) {
      console.error('AI Analysis failed', error);
    }
  };

  return (
    <div>
      <h2>AI Analysis</h2>
      <textarea value={input} onChange={(e) => setInput(e.target.value)} placeholder="Enter text for analysis"></textarea>
      <button onClick={handleAnalysis}>Analyze</button>
      <div>
        <h3>Result:</h3>
        <p>{result}</p>
      </div>
    </div>
  );
}

export default AIAnalysis;
