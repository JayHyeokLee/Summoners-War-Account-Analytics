import React, { createContext, useState, useContext } from "react";

const JsonContext = createContext();

export const JsonProvider = ({ children }) => {
  const [jsonData, setJsonData] = useState(null);

  return (
    <JsonContext.Provider value={{ jsonData, setJsonData }}>
      {children}
    </JsonContext.Provider>
  );
};

export const useJsonData = () => {
  const context = useContext(JsonContext);
  if (!context) {
    throw new Error("useJsonData must be used within a JsonProvider");
  }
  return context;
};