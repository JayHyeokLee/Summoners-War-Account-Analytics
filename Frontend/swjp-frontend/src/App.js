import React, { useState } from "react";
import { Sidebar, SidebarItem } from "./components/Sidebar";
import { UploadForm } from "./components/UploadForm";
import { Moon, Sun } from "lucide-react";
import logo from "./assets/logo.png"; // placeholder for logo

const App = () => {
  const [darkMode, setDarkMode] = useState(true);

  return (
    <div className={`${darkMode ? "bg-gray-900 text-white" : "bg-gray-100 text-black"} h-screen flex`}> 
      {/* Sidebar */}
      <Sidebar>
        <div className="p-4 flex items-center">
          <img src={logo} alt="Logo" className="h-10 w-10 mr-2" />
          <h1 className="text-xl font-bold">Rune Tool</h1>
        </div>
        <SidebarItem label="Dashboard" />
        <SidebarItem label="Upload Runes" active />
        <SidebarItem label="Settings" />
      </Sidebar>

      {/* Main Content */}
      <div className="flex-1 flex flex-col p-6">
        {/* Header */}
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-2xl font-semibold">Upload Runes</h2>
          <div className="flex items-center space-x-4">
            <button
              className="p-2 rounded-lg bg-gray-800 hover:bg-gray-700"
              onClick={() => setDarkMode(!darkMode)}
            >
              {darkMode ? <Sun size={20} /> : <Moon size={20} />}
            </button>
            <UploadForm />
          </div>
        </div>
        
        {/* For future features */}
      </div>
    </div>
  );
};

export default App;
