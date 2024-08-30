import React from 'react';
import AIAnalysis from './AIAnalysis';
import RealTimeNotifications from './RealTimeNotifications';
import { Container, Typography } from '@mui/material';

function App() {
    return (
        <Container>
            <Typography variant="h4" style={{ marginBottom: '20px' }}>
                AI Cyberguardian Dashboard
            </Typography>
            <AIAnalysis />
            <Typography variant="h5" style={{ marginTop: '40px' }}>
                Real-Time Notifications
            </Typography>
            <RealTimeNotifications />
        </Container>
    );
}

export default App;
