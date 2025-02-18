import React, { useState } from "react";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import annotationPlugin from "chartjs-plugin-annotation";

// Register Chart.js components
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend, annotationPlugin);

const RuneChart = ({ runeData }) => {
  const [displayCount, setDisplayCount] = useState(100); // Default to Top 100

  if (!runeData || runeData.length === 0) return <p>No data available</p>;

  // Sort runes by efficiency (descending) and limit based on slider value
  const sortedRunes = [...runeData].sort((a, b) => b.current_efficiency - a.current_efficiency);
  const filteredRunes = sortedRunes.slice(0, displayCount);

  // Extract labels and efficiency values
  const labels = filteredRunes.map((rune, index) => `Rune ${index + 1}`);
  const currentEfficiencies = filteredRunes.map((rune) => parseFloat(rune.current_efficiency));

  // Calculate average efficiency of displayed runes
  const avgEfficiency =
    currentEfficiencies.reduce((sum, value) => sum + value, 0) / currentEfficiencies.length;

  // Chart.js configuration
  const data = {
    labels,
    datasets: [
      {
        label: "Current Efficiency (%)",
        data: currentEfficiencies,
        borderColor: "rgba(54, 162, 235, 1)", // Blue line
        backgroundColor: "rgba(54, 162, 235, 0.2)",
        pointBackgroundColor: "rgba(54, 162, 235, 1)",
        borderWidth: 2,
        fill: true,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { position: "top" },
      title: { display: true, text: `Top ${displayCount} Rune Efficiency Graph` },
      tooltip: {
        enabled: true,
        callbacks: {
          label: (tooltipItem) => `${tooltipItem.raw.toFixed(2)}% Efficiency`,
        },
      },
      annotation: {
        annotations: {
          averageLine: {
            type: "line",
            yMin: avgEfficiency,
            yMax: avgEfficiency,
            borderColor: "red",
            borderWidth: 2,
            borderDash: [5, 5], // Dotted Line
            label: {
              content: `Avg: ${avgEfficiency.toFixed(2)}%`,
              enabled: true,
              position: "end",
              backgroundColor: "rgba(255, 99, 132, 0.8)",
              padding: 5,
              font: { weight: "bold" },
              display: "auto",
            },
          },
        },
      },
    },
    scales: {
      y: { beginAtZero: true, max: 150 },
    },
  };

  return (
    <div>
      {/* Slider to choose the number of runes */}
      <div className="slider-container">
        <label>Show Top {displayCount} Runes</label>
        <input
          type="range"
          min="10"
          max="1000"
          step="10"
          value={displayCount}
          onChange={(e) => setDisplayCount(Number(e.target.value))}
        />
      </div>

      {/* Chart */}
      <Line data={data} options={options} />
    </div>
  );
};

export default RuneChart;
