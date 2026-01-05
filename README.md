<div align="center">

# Privalk Web

**Secure, Real-time, and Private Messaging for the Modern Web.**

> 🚧 **Note:** This application is currently under active development. Features are subject to change.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)](https://flask.palletsprojects.com/)
[![Firebase](https://img.shields.io/badge/Firebase-Firestore-orange.svg)](https://firebase.google.com/)

[Description](#-description) • [Features](#-features) • [Tech Stack](#-tech-stack) • [Installation](#-installation) • [Contributing](#-contributing)

</div>

---

## 📖 Description

**Privalk Web** is an open-source, secure, and real-time messaging application built with Flask and Firebase. It features a modern, responsive UI with customizable themes (including AMOLED mode), privacy-focused settings, and a seamless user experience.

## ✨ Features

- **⚡ Real-time Messaging**: Instant message delivery using Server-Sent Events (SSE) for a snappy experience.
- **🔐 Secure Authentication**: Robust user accounts with password and security key login options.
- **👥 Friend System**: Send, accept, and decline friend requests. Manage your connections easily.
- **🎨 Customizable Appearance**:
  - **Themes**: Neon Green, Crimson Red, Hot Pink, Amber, Electric Purple.
  - **Modes**: Light, Dark, and System Sync.
  - **AMOLED Black**: True black mode for OLED screens to save battery.
  - **Chat Styling**: Customizable chat bubble styles and font sizes.
- **📱 Responsive Design**: Fully functional on both desktop and mobile devices with a native-app feel.
- **👤 User Profiles**: View user bios, join dates, and friend lists in a beautiful card layout.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Database**: Google Firebase Firestore (NoSQL)
- **Frontend**: HTML5, CSS3 (CSS Variables, Flexbox/Grid), JavaScript (Vanilla ES6+)
- **Real-time**: Server-Sent Events (SSE)

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- [Python 3.x](https://www.python.org/downloads/)
- A [Firebase](https://console.firebase.google.com/) project with Firestore enabled.

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/akash-kumarrr/privalk.git
   cd privalk
   ```

2. **Install Dependencies**
   ```bash
   # Create virtual environment (Optional but recommended)
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   pip install flask firebase-admin
   ```

3. **Firebase Setup**
   - Go to your Firebase Console.
   - Navigate to **Project Settings > Service accounts**.
   - Generate a new Private Key.
   - Download the JSON file and rename it to `serviceAccountKey.json`.
   - Place `serviceAccountKey.json` in the root directory of the project.

4. **Run the Application**
   ```bash
   python app.py
   ```

5. **Access the App**
   Open your browser and navigate to `http://127.0.0.1:5000`.

## 📂 Project Structure

```text
privalk/
├── app.py                 # Main Flask application routes
├── server.py              # Backend logic & Firebase integration
├── serviceAccountKey.json # Firebase credentials (Ignored by Git)
├── static/
│   ├── themes.css         # CSS Variables & Theme definitions
│   └── settings.js        # Frontend logic for settings & themes
└── templates/
    └── app.html           # Main Single Page Application (SPA) template
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

---

<div align="center">
  <sub>Built with ❤️ by <a href="https://github.com/akash-kumarrr">Akash</a></sub>
</div>
