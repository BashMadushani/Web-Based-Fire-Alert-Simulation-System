🔥 Web-Based Fire Alert Simulation System
(AI & IoT-Based Smart Fire Detection System)

📌 Project Overview

The Web-Based Fire Alert Simulation System is a smart safety solution designed to detect, simulate, and visualize fire incidents in industrial or building environments.
It uses a Streamlit-based frontend for real-time monitoring and a FastAPI backend for fire risk analysis and alert processing.

This project is suitable for:

Final year undergraduate projects

IoT & AI-based safety systems

Smart factory / smart building simulations

🎯 Key Features

🔥 Fire detection simulation (LOW / MEDIUM / HIGH severity)

📊 Real-time dashboard UI using Streamlit

🚨 Fire alerts with evacuation instructions

🎨 Modern dark-themed UI with custom CSS

🔌 Backend API for fire risk analysis

🧠 Scalable for IoT sensor & AI model integration

🧭 System Architecture

+----------------+        HTTP        +----------------+
|  Streamlit UI  |  <------------->  |   FastAPI API  |
|  (Frontend)    |                   |  (Backend)     |
|  app.py        |                   |  backend.py    |
+----------------+                   +----------------+
        |                                  |
        | Fire Simulation / Input          | Fire Risk Analysis
        v                                  v
   UI State Handling                  Logic & Rules
   (Dashboard Alerts)                 (Severity Decision)

📂 Project Structure
 Fire interface/
│
├─ app.py
│   ├─ Streamlit UI Layout
│   ├─ Custom CSS Styling
│   ├─ Fire Status Display
│   └─ User Interaction Logic
│
├─ backend.py
│   ├─ FastAPI Server
│   ├─ Fire Detection Logic
│   ├─ Severity Classification
│   └─ Alert Response Handling
│
└─ Communication Flow
    └─ app.py  →  backend.py (HTTP API calls)



🧩 Module Description
🔹 Frontend (Streamlit – app.py)

Dashboard layout

Fire status panel (right side)

Alarm and evacuation messages

Custom CSS styling

User interaction & visualization

🔹 Backend (FastAPI – backend.py)

Fire severity logic

API endpoints

Fire risk calculation

Extendable for IoT sensors / AI models

🛠️ Tools & Technologies.

| Category        | Technology     |
| --------------- | -------------- |
| Frontend        | Streamlit      |
| Backend         | FastAPI        |
| Language        | Python         |
| UI Styling      | CSS (embedded) |
| API             | REST           |
| Version Control | Git & GitHub   |




