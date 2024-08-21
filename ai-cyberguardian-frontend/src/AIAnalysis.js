import React, { useState } from 'react';
import axios from 'axios';

const AIAnalysis = () => {
    const [inputText, setInputText] = useState('');
    const [result, setResult] = useState('');

    const handleInputChange = (e) => {
        setInputText(e.target.value);
    };

    const handleAnalyze = () => {
        axios.post('http://localhost:5000/ai-analysis', 
            { text: inputText }, // Data is directly passed here
            {
                headers: {
                    'Content-Type': 'application/json',
                }
            }
        )
        .then(response => {
            setResult(response.data.result);
        })
        .catch(error => {
            console.error("Error:", error);
        });
    };

    return (
        <div>
            <h1>AI Analysis</h1>
            <input
                type="text"
                value={inputText}
                onChange={handleInputChange}
                placeholder="Enter text"
            />
            <button onClick={handleAnalyze}>Analyze</button>
            <h2>Result:</h2>
            <p>{result}</p>
        </div>
    );
};

export default AIAnalysis;
