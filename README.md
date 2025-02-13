# 🌐 Computer Networks Project - ENCS3320

## 📌 Overview

This repository contains my implementation of **Project #1 for the Computer Networks (ENCS3320) course at Birzeit University**. The project consists of three main tasks:

1. **Network Diagnostic Commands:** Using `ping`, `tracert`, `nslookup`, and Wireshark to analyze network communication.
2. **TCP Server-Client Application:** A simple server that verifies student IDs and executes system commands.
3. **Basic Web Server Implementation:** A Python-based web server handling multiple types of requests and serving static files.

## 🛠 Features

### ✅ **Part 1: Network Commands & Analysis**

- Run `ping`, `tracert`, and `nslookup` on `www.cornell.edu`.
- Use **Wireshark** to capture and analyze DNS packets.

### ✅ **Part 2: TCP Client-Server Application**

- Server listens on **port 9955**.
- If a valid student ID is received, the server:
  - Notifies the client about an upcoming screen lock.
  - Waits **10 seconds** before locking the system.
- Invalid IDs receive an error message.
- Implemented using **Python socket programming**.

### ✅ **Part 3: Web Server Implementation**

- Server listens on **port 9966**.
- Handles different types of HTTP requests:
  - Serves **HTML, CSS, PNG, and JPG** files.
  - Redirects `/cr`, `/so`, and `/rt` requests to external sites.
  - Returns appropriate HTTP **status codes** (e.g., `200 OK`, `404 Not Found`).
- Supports **desktop and mobile clients**.

## 📂 Contents

- 📂 **Codes:** Implementation of all codes.
- 📄 **Project Report (report.pdf):** Documentation of all tasks, analysis, and results.

## 📌 Requirements

- Python (For Web & TCP Applications)
- Wireshark (For Packet Capture)
- Basic knowledge of networking protocols & HTTP requests

## 👩‍💻 Authors

**Saja Asfour**

- 🎓 Computer Engineering Student at Birzeit University
- 🏠 GitHub: [SajaAsfour](https://github.com/SajaAsfour)

**Shahd Shreteh**
- 🎓 Computer Engineering Student at Birzeit University
- 🏠 GitHub: [ShahdShreteh](https://github.com/ShahdShreteh)

**Rawand Bawatneh**
- 🎓 Computer Engineering Student at Birzeit University
- 🏠 GitHub: [rawandbawatneh](https://github.com/rawandbawatneh)

## 📜 License

This repository is for educational purposes. Feel free to use and reference the work, but please give proper credit. 😊

