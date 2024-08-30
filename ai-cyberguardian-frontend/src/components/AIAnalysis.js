import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import { TextField, Button, Typography, Alert, CircularProgress } from '@mui/material';

const AIAnalysis = () => {
    const [text, setText] = useState('');
    const [result, setResult] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);
    const [feedback, setFeedback] = useState('');
    const lastRequestTimeRef = useRef(null);
    const requestDelay = 3000; // 3 seconds delay between requests

    const handleSubmit = async (event) => {
        event.preventDefault();

        if (!text || text.trim() === '') {
            setError("Input text cannot be empty.");
            return;
        }

        const now = Date.now();
        if (lastRequestTimeRef.current && (now - lastRequestTimeRef.current < requestDelay)) {
            setError("You are submitting requests too quickly. Please wait a moment.");
            return;
        }
        lastRequestTimeRef.current = now;

        setLoading(true);
        setError(null);
        setResult(null);

        try {
            console.log(`Sending request to server: ${text}`);
            const response = await axios.post('http://localhost:5000/ai-analysis', {
                text: text.trim()
            });

            setResult(response.data.result);
            console.log(`Received result from server: ${response.data.result}`);
        } catch (error) {
            setError("An error occurred during analysis.");
            console.error("There was an error!", error);
        } finally {
            setLoading(false);
        }
    };

    const handleTextChange = (e) => {
        const value = e.target.value;
        setText(value);

        if (value.trim().length < 10) {
            setFeedback("Input too short, please provide more text.");
        } else {
            setFeedback("");
        }
    };

    useEffect(() => {
        if (error) {
            console.log(`Error: ${error}`);
        }
    }, [error]);

    return (
        <div>
            <Typography variant="h5">AI Cyber Analysis</Typography>
            {error && <Alert severity="error">{error}</Alert>}
            <form onSubmit={handleSubmit}>
                <TextField
                    label="Enter text to analyze"
                    variant="outlined"
                    fullWidth
                    multiline
                    rows={4}
                    value={text}
                    onChange={handleTextChange}
                    error={!!feedback}
                    helperText={feedback}
                    style={{ marginBottom: '20px' }}
                />
                <Button variant="contained" color="primary" type="submit" disabled={loading}>
                    {loading ? <CircularProgress size={24} /> : 'Analyze'}
                </Button>
            </form>
            {result && (
                <Typography variant="h6" style={{ marginTop: '20px' }}>
                    Analysis Result: {result}
                </Typography>
            )}
        </div>
    );
};

export default AIAnalysis;
