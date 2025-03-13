import React from "react";
import logo from "../assets/logo.png";
import { Link } from "react-router-dom";
import "../bootstrap.css";

export const Sidebar = () => {
  return (
    <div className="sidebar">
      <div class="container-l">
        <nav class="navbar navbar-dark bg-dark rounded">
          <a class="navbar-brand" href="#">
            <img src={logo} alt="Logo" className="sidebar-logo" width="80" height="40"/>
          </a>
          <ul class="nav nav-pills">
            <li class="nav-item active">
              <a class="nav-link" href="/">Rune Chart</a>
            </li>
            <li class="nav-item active">
              <a class="nav-link" href="/ai-analysis">AI Analysis</a>
            </li>
          </ul>          
        </nav>
      </div>
      
    </div>
  );
};