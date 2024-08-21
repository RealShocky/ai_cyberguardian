import React from 'react';
import { useHistory } from 'react-router-dom';

function Dashboard() {
  const history = useHistory();

  const handleAIAnalysis = () => {
    history.push('/ai-analysis');
  };

  return (
    <div>
      <h2>Dashboard</h2>
      <button onClick={handleAIAnalysis}>Run AI Analysis</button>
    </div>
  );
}

export default Dashboard;
