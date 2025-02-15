import React from "react";
import "./sidebar.css";
import logo from "../assets/logo.png";

export const Sidebar = () => {
  return(
    <div className="sidenav">
        
        <div className="toplogo">
          <img src={logo} alt="Logo"/>
        </div>

        <a href="#">About</a>
        <a href="#">Services</a>
        <a href="#">Clients</a>
        <a href="#">Contact</a>
      </div>
  );
}

export default Sidebar;
