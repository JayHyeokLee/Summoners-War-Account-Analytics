import React, { useState, useEffect } from "react";
import axios from "axios";
import RuneChart from "./RuneChart";
import { useJsonData } from "../JsonContext";

const AIAnalysis = () => {
  const { jsonData } = useJsonData();
  const [aiInsight, setAIInsight] = useState("");

  useEffect(() => {
    if (jsonData) {
      console.log("Using Stored JSON Data:", jsonData);
    } else {
      console.log("No JSON data found. Please upload a file first.");
    }
  }, [jsonData]);

  const handleAIAnalysis = async () => {
    if (!jsonData) {
      alert("No JSON data available. Please upload a file first.");
      return;
    }

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/ai-insight/", jsonData, {
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
      <RuneChart runeData={jsonData?.runes || []} />
      <button onClick={handleAIAnalysis} className="ai-button">
        Get AI Insights
      </button>
      {aiInsight && (
        <div className="ai-insight">
          <h4>AI Insights:</h4>
          <pre>{aiInsight}</pre>
        </div>
      )}
    </div>
  );
};

export default AIAnalysis;
