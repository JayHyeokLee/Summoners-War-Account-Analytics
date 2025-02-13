/* Sidebar.js */
import React from "react";

export const Sidebar = ({ children }) => {
  return (
    <div className="w-64 bg-gray-800 h-screen p-4 flex flex-col space-y-4">
      {children}
    </div>
  );
};

export const SidebarItem = ({ label, active }) => {
  return (
    <div
      className={`p-3 rounded-lg cursor-pointer ${
        active ? "bg-gray-700 text-white" : "text-gray-400 hover:bg-gray-700"
      }`}
    >
      {label}
    </div>
  );
};

/* UploadForm.js */
import React, { useState } from "react";

export const UploadForm = () => {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = () => {
    if (!file) {
      alert("Please select a file.");
      return;
    }
    console.log("Uploading file:", file.name);
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} className="hidden" id="file-upload" />
      <label htmlFor="file-upload" className="px-4 py-2 bg-blue-500 text-white rounded-lg cursor-pointer hover:bg-blue-600">
        Choose File
      </label>
      {file && <span className="ml-2 text-sm">{file.name}</span>}
      <button onClick={handleUpload} className="ml-4 px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600">
        Upload
      </button>
    </div>
  );
};
