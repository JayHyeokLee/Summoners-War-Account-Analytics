import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { JsonProvider } from "./JsonContext.js";
import {Sidebar} from "./components/sidebar";
import UploadForm from "./components/UploadForm";
import AIAnalysis from "./components/AIAnalysis";

const App = () => {

  return (
    <JsonProvider>
      <Router>
        <div className="landing">
          <div className="sidenav">
            <Sidebar></Sidebar>
          </div>

          {/* Main Content */}
          <div className="main">
            <main>
              <Routes>
                {/* Home / Upload Page */}
                <Route
                  path="/"
                  element={
                    <>
                      <h1>Welcome to Summoners War Account Analytics Tool!</h1>
                      <h2>How to Use</h2>
                      <p>
                        1. If you haven't already, <a href="https://github.com/Xzandro/sw-exporter" target="_blank" rel="noopener noreferrer">download SWEX</a> and extract your account .json file.<br/>
                        &emsp;-If you need help check out <a href="https://www.youtube.com/watch?v=vbx5qk10c3o" target="_blank" rel="noopener noreferrer">this video</a> for a guide.<br/>
                        <br/>
                        2. Upload your .json file below.<br/>
                        <br/>
                        3. Enjoy the website!<br/>
                        <br/>
                        Please let me know if there are bugs or any new features that you would like to see.
                      </p>

                      <UploadForm></UploadForm>
                      </>
                  }
                />

                {/* AI Analysis Page */}
                <Route path="/ai-analysis" element={<AIAnalysis />} />
              </Routes>
            </main>
          </div>
        </div>
      </Router>
    </JsonProvider>
    
  );
};

export default App;
