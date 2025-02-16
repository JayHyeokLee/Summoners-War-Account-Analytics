import React, { useState } from "react";
import Sidebar from "./components/sidebar";
import UploadForm from "./components/UploadForm";
import { Moon, Sun } from "lucide-react";

const App = () => {
  const [darkMode, setDarkMode] = useState(true);

  return (
    <div className="landing">
      <div className="sidenav">
        <Sidebar></Sidebar>
      </div>

      {/* Main Content */}
      <div className="main">
        <main>
          <h1>Rune Graph</h1>
          <UploadForm></UploadForm>
        </main>
      </div>
    </div>
  );
};

export default App;
