import React, { useState, useEffect } from "react";
import axios from "axios";
import RuneChart from "./RuneChart";

const AIAnalysis = () => {
  const [runeData, setRuneData] = useState([]);
  const [aiInsight, setAIInsight] = useState("");

  useEffect(() => {
    // Fetch rune data when the component loads
    const fetchRuneData = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/runes/");
        setRuneData(response.data);
      } catch (error) {
        console.error("Error fetching rune data:", error);
      }
    };

    fetchRuneData();
  }, []);

  const handleAIAnalysis = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/ai-insight/", runeData, {
        headers: {
          "Content-Type": "application/json",
        },
      });
      setAIInsight(response.data.insight);
    } catch (error) {
      console.error("AI Request Error:", error);
      setAIInsight("Error getting AI insight.");
    }
  };

  return (
    <div>
      <h2>AI Analysis</h2>
      <RuneChart runeData={runeData} />
      <button onClick={handleAIAnalysis} className="ai-button">
        Get AI Insights
      </button>
      {aiInsight && (
        <div className="ai-insight">
          <h4>AI Insights:</h4>
          <p>{aiInsight}</p>
        </div>
      )}
    </div>
  );
};

export default AIAnalysis;
