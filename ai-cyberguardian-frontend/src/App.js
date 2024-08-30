import React, { useState } from 'react';
import { Container, Typography, TextField, Button, CircularProgress, Snackbar } from '@mui/material';
import Alert from '@mui/material/Alert';
import axios from 'axios';

const App = () => {
  const [text, setText] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(''); // Ensure result is a string
  const [error, setError] = useState('');
  const [open, setOpen] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    setError('');
    setResult(''); // Clear previous results
    try {
      const response = await axios.post('http://localhost:5000/ai-analysis', { text });

      if (response.data && response.data.result) {
        setResult(response.data.result); // Set the result directly as a string
      } else {
        setError('No result returned from analysis.');
      }
    } catch (err) {
      setError('Error occurred while processing your request.');
    } finally {
      setLoading(false);
      setOpen(true);
    }
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <Container maxWidth="md">
      <Typography variant="h4" component="h1" gutterBottom>
        AI Cyberguardian Dashboard
      </Typography>
      <Typography variant="h6" gutterBottom>
        AI Cyber Analysis
      </Typography>
      <TextField
        fullWidth
        label="Enter text to analyze"
        variant="outlined"
        value={text}
        onChange={(e) => setText(e.target.value)}
        multiline
        rows={4}
      />
      <Button
        variant="contained"
        color="primary"
        onClick={handleSubmit}
        disabled={loading}
        style={{ marginTop: '20px' }}
      >
        {loading ? <CircularProgress size={24} /> : 'Analyze'}
      </Button>
      <Typography variant="h6" style={{ marginTop: '20px' }}>
        Analysis Result
      </Typography>
      {result && (
        <Typography component="p">
          {result} {/* Displaying the result directly */}
        </Typography>
      )}

      <Snackbar open={open} autoHideDuration={6000} onClose={handleClose}>
        <Alert onClose={handleClose} severity={error ? "error" : "success"}>
          {error ? error : "Analysis completed successfully!"}
        </Alert>
      </Snackbar>
    </Container>
  );
};

export default App;
