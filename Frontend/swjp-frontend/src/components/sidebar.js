import React from "react";
import logo from "../assets/logo.png";
import { Link } from "react-router-dom";
import "./Sidebar.css";

export const Sidebar = () => {
  return (
    <div className="sidebar">
      <img src={logo} alt="Logo" className="sidebar-logo" />
      <nav className="sidebar-menu">
        <Link to="/" className="sidebar-item">Home</Link>
        <Link to="/ai-analysis" className="sidebar-item">AI Analysis</Link>
      </nav>
    </div>
  );
};