import streamlit as st
import cv2
import numpy as np
import pandas as pd
import requests
from datetime import datetime

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Smart Fire Detection System", layout="wide")

# -------------------------------
# Global CSS Styling (Dark Theme + Custom)
# -------------------------------
st.markdown("""
<style>
body {
  font-family: Arial, Helvetica, sans-serif;
  background: #e86f8d;
  color: #e5e7eb;
  margin: 0;
  padding: 20px;
}
h1, h2, h3, h4 {
  color: #f87171;  /* light red headings */
}
.stButton>button {
  background-color: #f87171;
  color: white;
  font-weight: bold;
}
.fire-card {
    padding: 20px;
    border-radius: 15px;
    color: white;
    font-size: 18px;
    font-weight: bold;
}
.high { background-color: #d32f2f; }       /* Red */
.medium { background-color: #f57c00; }     /* Orange */
.low { background-color: #388e3c; }        /* Green */
.safe { background-color: #1976d2; }       /* Blue */
.stMetric>div>div>div {
    color: #e5e7eb !important;  /* Sensor card text color for dark theme */
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Title
# -------------------------------
st.title("🔥 AI & IoT Based Smart Fire Detection System")

# -------------------------------
# Sidebar - Sensor Inputs
# -------------------------------
st.sidebar.header("📡 Sensor Inputs")
temperature = st.sidebar.slider("Temperature (°C)", 20, 150, 30)
smoke = st.sidebar.slider("Smoke Level (%)", 0, 100, 10)
gas = st.sidebar.slider("Gas Level (ppm)", 0, 1000, 100)

st.sidebar.subheader("Sensor Levels")
st.sidebar.progress(min(int(smoke), 100))
st.sidebar.progress(min(int(temperature/1.5), 100))
st.sidebar.progress(min(int(gas/10), 100))

# -------------------------------
# Sensor History
# -------------------------------
if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=["Time","Temperature","Smoke","Gas"])

new_data = pd.DataFrame({
    "Time": [datetime.now().strftime("%H:%M:%S")],
    "Temperature": [temperature],
    "Smoke": [smoke],
    "Gas": [gas]
})
st.session_state.history = pd.concat([st.session_state.history, new_data], ignore_index=True)
st.session_state.history = st.session_state.history.tail(20)

# -------------------------------
# Layout: Camera Left + Fire Status Right
# -------------------------------
col_camera, col_status = st.columns([2, 1])  # Camera takes more space, Fire Status on right

# -------------------------------
# Camera Input
# -------------------------------
with col_camera:
    st.subheader("📷 Camera Input")
    uploaded_file = st.file_uploader("Upload Camera Image", type=["jpg", "png"])
    if uploaded_file:
        image = np.array(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(image, cv2.IMREAD_COLOR)
        # Optional demo rectangle to highlight fire
        cv2.rectangle(img, (50,50), (200,200), (0,0,255), 3)
        st.image(img, channels="BGR", caption="Camera Feed")

# -------------------------------
# Fire Status Panel on Right
# -------------------------------
with col_status:
    st.subheader("🚨 Fire Status")

    if st.button("Analyze Fire"):
        try:
            # Call backend API
            response = requests.post(
                "http://127.0.0.1:8000/detect",
                json={"temperature": temperature, "smoke": smoke, "gas": gas}
            )
            result = response.json()
            fire_detected = result["fire_detected"]
            severity = result["severity"]
        except:
            st.error("❌ Cannot reach backend API")
            fire_detected = False
            severity = "LOW"

        # Determine background color
        if fire_detected:
            if severity == "HIGH":
                color = "#d32f2f"  # Red
                message = "🔥 HIGH FIRE ALERT! 🚨 Evacuate Immediately!"
                instructions = """
                - 🏃 Use nearest emergency exit  
                - ❌ Do not use elevators  
                - 🤝 Assist others if possible
                """
            elif severity == "MEDIUM":
                color = "#f57c00"  # Orange
                message = "⚠️ Medium Fire Risk Detected!"
                instructions = "⚠️ Be cautious. Prepare for evacuation."
            else:
                color = "#388e3c"  # Green
                message = "⚠️ Low Fire Risk. Stay Alert."
                instructions = ""
        else:
            color = "#1976d2"      # Blue
            message = "✅ No Fire Detected. Environment is Safe."
            instructions = ""

        # Colored card
        st.markdown(
            f"""
            <div style="
                background-color: {color};
                padding: 20px;
                border-radius: 15px;
                color: white;
                font-size: 18px;
                font-weight: bold;
            ">
                {message}
            </div>
            """,
            unsafe_allow_html=True
        )
        if instructions:
            st.markdown(instructions)

# -------------------------------
# Sensor Summary Cards
# -------------------------------
st.subheader("📊 Sensor Summary")
col1, col2, col3 = st.columns(3)
col1.metric("🌡 Temperature", f"{temperature} °C", "🔥 Hot" if temperature>60 else "Normal")
col2.metric("💨 Smoke", f"{smoke} %", "⚠️ Warning" if smoke>40 else "Safe")
col3.metric("🧪 Gas", f"{gas} ppm", "⚠️ High" if gas>500 else "Safe")

# -------------------------------
# Sensor History Chart
# -------------------------------
st.subheader("📈 Sensor History (Last 20 Records)")
st.line_chart(st.session_state.history.set_index("Time")[["Temperature","Smoke","Gas"]])

# -------------------------------
# Footer / Notes
# -------------------------------
st.markdown("---")
st.markdown("💡 This dashboard shows real-time sensor data, fire alerts, and evacuation instructions.")
