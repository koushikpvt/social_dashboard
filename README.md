# 🛡️ SafeGas Dashboard

A real-time IoT dashboard for monitoring gas leaks, servo activity, and alert events — built with ESP32, Supabase, and React.

## 🚀 Overview

SafeGas is a safety-focused system that detects hazardous gas levels, triggers servo-based shutoff mechanisms, and logs contextual data to the cloud. This dashboard visualizes live sensor data, servo rotation history, and alert status — all in a clean, responsive UI.

---

## ⚙️ Getting Started

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

### Prerequisites

- Node.js ≥ 18
- Supabase project with `gas_logs` and `servo_events` tables
- Telegram bot token (optional for alerts)

### Installation

```bash
# Clone the repo
git clone https://github.com/koushikpvt/safegas-dashboard.git
cd safegas-dashboard

# Install dependencies
npm install

# Start the dashboard
npm start
