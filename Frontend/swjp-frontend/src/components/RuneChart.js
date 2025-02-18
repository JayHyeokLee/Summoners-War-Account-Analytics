import React from "react";
import { Line } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from "chart.js";
import annotationPlugin from "chartjs-plugin-annotation";

// Register chart components
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend, annotationPlugin);

const RuneChart = ({ runeData }) => {
  if (!runeData || runeData.length === 0) return <p>No data available</p>;

  // Extract labels and efficiency values
  const labels = runeData.map((rune, index) => `Rune ${index + 1}`); // Use index to avoid long IDs
  const currentEfficiencies = runeData.map((rune) => rune.current_efficiency);
  const avgEfficiency = currentEfficiencies.reduce((sum, value) => sum + value, 0) / currentEfficiencies.length;

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
      title: { display: true, text: "Rune Efficiency Graph" },
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
              display: "auto", // ✅ Show tooltip only on hover
            },
            hoverBackgroundColor: "rgba(255, 99, 132, 0.8)", // ✅ Highlight when hovered
            display: true,
          },
        },
      },
    },
    scales: {
      y: { beginAtZero: true, max: 150 },
    },
  };

  return <Line data={data} options={options} />;
};

export default RuneChart;