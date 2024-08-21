import React from 'react';
import { useNavigate } from 'react-router-dom';

function Dashboard() {
  const navigate = useNavigate();

  const handleAIAnalysis = () => {
    navigate('/ai-analysis');
  };

  return (
    <div>
      <h2>Dashboard</h2>
      <button onClick={handleAIAnalysis}>Run AI Analysis</button>
    </div>
  );
}

export default Dashboard;
