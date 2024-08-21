// src/api.js
import axios from 'axios';

export const analyzeText = async (text) => {
    try {
        const response = await axios.post('http://localhost:5000/ai-analysis', { text });
        return response.data.result;
    } catch (error) {
        console.error('Error in API call', error);
        throw error;
    }
};
