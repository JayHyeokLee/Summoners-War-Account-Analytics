import React from "react";
import "./sidebar.css";
import logo from "../assets/logo.png";

export const Sidebar = () => {
  return(
    <div className="sidenav">
        
        <img src={logo} alt="Logo" className="sidebar-logo"/>

        <a href="home">Home</a>
        <a href="#">Coming soon...</a>
        <a href="#">Coming soon...</a>
        <a href="#">Coming soon...</a>
      </div>
  );
}

export default Sidebar;
