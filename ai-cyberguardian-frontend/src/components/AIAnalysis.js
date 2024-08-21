// src/components/AIAnalysis.js
import React, { useState } from 'react';
import axios from 'axios';

const AIAnalysis = () => {
    const [text, setText] = useState('');
    const [result, setResult] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:5000/ai-analysis', { text });
            setResult(response.data.result);
        } catch (error) {
            console.error("There was an error!", error);
        }
    };

    return (
        <div>
            <h2>AI Cyber Analysis</h2>
            <form onSubmit={handleSubmit}>
                <textarea
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                    placeholder="Enter text to analyze"
                />
                <button type="submit">Analyze</button>
            </form>
            {result && (
                <div>
                    <h3>Analysis Result</h3>
                    <p>{result}</p>
                </div>
            )}
        </div>
    );
};

export default AIAnalysis;
