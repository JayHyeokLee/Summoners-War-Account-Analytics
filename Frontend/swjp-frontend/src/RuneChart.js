import React from "react";
import { Line } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from "chart.js";

// Register chart components
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const RuneChart = ({ runeData }) => {
  if (!runeData || runeData.length === 0) return <p>No data available</p>;

  // Extract labels and efficiency values
  const labels = runeData.map((rune, index) => `Rune ${index + 1}`); // Use index to avoid long IDs
  const currentEfficiencies = runeData.map((rune) => rune.current_efficiency);
  const maxEfficiencies = runeData.map((rune) => rune.max_efficiency);

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
      {
        label: "Max Efficiency (%)",
        data: maxEfficiencies,
        borderColor: "rgba(255, 99, 132, 1)", // Red line
        backgroundColor: "rgba(255, 99, 132, 0.2)",
        pointBackgroundColor: "rgba(255, 99, 132, 1)",
        borderWidth: 2,
        fill: true,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { position: "top" },
      title: { display: true, text: "Rune Efficiency Trends" },
    },
    scales: {
      y: { beginAtZero: true, max: 100 },
    },
  };

  return <Line data={data} options={options} />;
};

export default RuneChart;
