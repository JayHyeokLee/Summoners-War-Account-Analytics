import React, { useState } from "react";
import axios from "axios";
import RuneChart from "./RuneChart";

const UploadForm = () => {
  const [file, setFile] = useState(null);
  const [runeData, setRuneData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a JSON file to upload.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      setError(null);

      // Replace with actual URL later
      const response = await axios.post("http://127.0.0.1:8000/api/upload/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      setRuneData(response.data);
    } catch (err) {
      setError("Failed to upload file. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Upload Json File Here:</h1>
      <input type="file" accept=".json" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>

      {loading && <p>Processing...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}

      {runeData && (
        <>
          <h2>Rune Efficiency Graph</h2>
          <RuneChart runeData={runeData} />
        </>
      )}
    </div>
  );
};

export default UploadForm;