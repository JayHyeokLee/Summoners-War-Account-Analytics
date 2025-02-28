import React, { useState, useEffect } from "react";
import axios from "axios";
import RuneChart from "./RuneChart";
import { useJsonData } from "../JsonContext";

const UploadForm = () => {
  const [file, setFile] = useState(null);
  const [runeData, setRuneData] = useState([]);  // All rune data
  const [filteredRunes, setFilteredRunes] = useState([]);  // Filtered rune data
  const [runeSets, setRuneSets] = useState([]);  // Available rune sets
  const [selectedSets, setSelectedSets] = useState([]);  // Selected sets for filtering
  const { setJsonData } = useJsonData();

  const runeSetNames = {
    1: 'Energy',
    2: 'Guard',
    3: 'Swift',
    4: 'Blade',
    5: 'Rage',
    6: 'Focus',
    7: 'Endure',
    8: 'Fatal',
    10: 'Despair',
    11: 'Vampire',
    13: 'Violent',
    14: 'Nemesis',
    15: 'Will',
    16: 'Shield',
    17: 'Revenge',
    18: 'Destroy',
    19: 'Fight',
    20: 'Determination',
    21: 'Enhance',
    22: 'Accuracy',
    23: 'Tolerance',
    24: 'Seal',
    25: 'Intangible'
  }

  useEffect(() => {
    // Apply filtering when selected sets change
    if (selectedSets.length > 0) {
      setFilteredRunes(runeData.filter(rune => selectedSets.includes(rune.rune_set)));
    } else {
      setFilteredRunes(runeData);
    }
  }, [selectedSets, runeData]);

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
      const response = await axios.post("http://127.0.0.1:8000/api/upload/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      const data = response.data;
      setRuneData(data);
      setFilteredRunes(data);
      setJsonData(data);
      
      //debug output
      console.log("Stored JSON Data:", response.data);

      // Extract unique set IDs from the runes
      const uniqueSets = [...new Set(data.map(rune => rune.rune_set))];
      //console.log("Unique Sets Found:", uniqueSets);  // Debugging
      setRuneSets(uniqueSets);
    } catch (err) {
      console.error("Upload failed:", err.response?.data || err.message);
    }
  };

  const handleCheckboxChange = (setId) => {
    setSelectedSets((prevSelected) =>
      prevSelected.includes(setId)
        ? prevSelected.filter((id) => id !== setId) // Remove if already selected
        : [...prevSelected, setId] // Add if not selected
    );
  };

  return (
    <div>
      <h2>Upload Rune Data</h2>
      <input type="file" accept=".json" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>

      {runeSets.length > 0 && (
        <div style={{ marginTop: "20px" }}>
          <h2>Filter by Rune Set</h2>
          {runeSets.map((setId) => (
            <label key={setId} style={{ marginRight: "10px" }}>
              <input
                type="checkbox"
                value={setId}
                onChange={() => handleCheckboxChange(setId)}
                checked={selectedSets.includes(setId)}
              />
              {runeSetNames[setId] || `Set ${setId}`}
            </label>
          ))}
        </div>
      )}

      {filteredRunes.length > 0 && (
        <>
          <RuneChart runeData={filteredRunes} />
        </>
      )}
    </div>
  );
};

export default UploadForm;