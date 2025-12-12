import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Trade Surveillance Dashboard", layout="wide")

# Load sample trades
trades = pd.read_csv("data/sample_trades.csv")
trades["symbol"] = trades["instrument"]


st.title("📊 Trade Surveillance & Anomaly Detection System")
st.metric("Total Trades", len(trades))
st.metric("Total Alerts", sum(1 for _ in open("data/alerts.log", "r", encoding="utf-8")))

st.markdown("Monitor trading patterns, detect suspicious activity, and review alerts in real time.")

# Filters
symbols = trades["instrument"].unique().tolist()
selected_symbol = st.selectbox("Select Symbol", symbols)
filtered = trades[trades["symbol"] == selected_symbol]

# Price and Volume Trends
col1, col2 = st.columns(2)
with col1:
    st.subheader(f"Price Trend — {selected_symbol}")

    fig, ax = plt.subplots(figsize=(8,4))

    # Plot price
    ax.plot(filtered["timestamp"], filtered["price"], marker="o", label="Price")

    # Detect anomalies
    sensitivity = st.slider("Sensitivity (Std Dev Multiplier)", 1.0, 5.0, 2.0)
    threshold = filtered["price"].mean() + sensitivity * filtered["price"].std()

    anomalies = filtered[filtered["price"] > threshold]

    # Plot anomalies
    ax.scatter(anomalies["timestamp"], anomalies["price"], color="red", label="Anomaly", zorder=5)
    
    # Show biggest anomaly value
    max_spike = anomalies["price"].max()
    st.success(f"Highest price anomaly detected: {max_spike:.2f}")


    # CLEAN X-AXIS (Fix messy labels)
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))  
    plt.xticks(rotation=45, fontsize=8)

    ax.legend()
    st.pyplot(fig)




    


with col2: 

    st.subheader(f"Volume Trend — {selected_symbol}")

    fig2, ax2 = plt.subplots(figsize=(8,4))
    ax2.bar(filtered["timestamp"], filtered["volume"], color="steelblue")

    # Cleaner x-axis
    ax2.xaxis.set_major_locator(plt.MaxNLocator(10))
    plt.xticks(rotation=45, fontsize=8)

    ax2.set_ylabel("Volume")
    st.pyplot(fig2)
st.caption(f"Last Updated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")


    
   


# Display alerts
st.subheader("⚠️ Alerts Log")

try:
    with open("data/alerts.log", "r", encoding="utf-8") as f:
        logs = f.readlines()
except FileNotFoundError:
    logs = []
    st.warning("No alerts found yet. Run the detection pipeline first.")

st.metric("Total Alerts Detected", len(logs))

# Display alerts
if logs:
    st.text_area("System Alerts", "".join(logs), height=250)
