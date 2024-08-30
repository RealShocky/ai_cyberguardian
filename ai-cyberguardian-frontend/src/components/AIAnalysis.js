import React, { useState } from 'react';
import { Typography, Container, TextField, Button, CircularProgress, Alert } from '@mui/material';

const AIAnalysis = () => {
    const [inputText, setInputText] = useState('');
    const [result, setResult] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [isValid, setIsValid] = useState(true);

    const validateInput = (text) => {
        return text && text.length > 10; // Simple validation check
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);

        if (!validateInput(inputText)) {
            setIsValid(false);
            setError('Input must be at least 10 characters long.');
            return;
        }

        setLoading(true);
        setIsValid(true);

        try {
            const response = await fetch('http://localhost:5000/ai-analysis', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: inputText }),
            });

            if (!response.ok) {
                throw new Error('Error occurred while processing your request.');
            }

            const data = await response.json();

            if (data && data.choices && data.choices.length > 0 && typeof data.choices[0].message.content === 'string') {
                setResult(data.choices[0].message.content);
            } else {
                setError('Unexpected response structure.');
            }
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    const handleInputChange = (e) => {
        const value = e.target.value;
        setInputText(value);
        setIsValid(validateInput(value));
        if (isValid) {
            setError(null);  // Clear error if input is valid
        }
    };

    return (
        <Container>
            <Typography variant="h4" component="h1" gutterBottom>
                AI Cyber Analysis
            </Typography>
            <form onSubmit={handleSubmit}>
                <TextField
                    label="Enter text to analyze"
                    variant="outlined"
                    fullWidth
                    value={inputText}
                    onChange={handleInputChange}
                    multiline
                    rows={4}
                    error={!isValid}
                    helperText={!isValid ? 'Input must be at least 10 characters long.' : ''}
                />
                <Button variant="contained" color="primary" type="submit" disabled={loading}>
                    {loading ? <CircularProgress size={24} /> : 'Analyze'}
                </Button>
            </form>
            {error && <Alert severity="error" sx={{ mt: 2 }}>{error}</Alert>}
            {result && (
                <Typography variant="h6" component="div" sx={{ mt: 2 }}>
                    Analysis Result
                </Typography>
            )}
            {result && (
                <Typography variant="body1" component="p">
                    {result}
                </Typography>
            )}
        </Container>
    );
};

export default AIAnalysis;
