# Summoners War Rune Efficiency Tool

This project is a **Django + React** web application for processing **Summoners War rune data**.  
It allows users to **upload JSON files**, calculates **rune efficiency**, and displays sorted results on an interactive graph.

---

## Features
- Upload JSON files containing rune data  
- Process runes and calculate **Current Efficiency**
- Sort runes by **Current Efficiency (descending)**  
- Display results in an **interactive line graph (Chart.js)**  
- Full **Django REST API** backend  
- **React frontend** for file upload & visualization
- **OpenAI API** to provide AI analytics and improvement suggestions

---

## Tech Stack
### **Backend (Django)**
- Django REST Framework (`djangorestframework`)
- File handling (`json`, `rest_framework`)
- **Sorting runes** on the backend for performance  

### **Frontend (React)**
- **React.js** (`create-react-app`)
- **Chart.js** (`react-chartjs-2`) for graph visualization  
- **Axios** for API requests  
