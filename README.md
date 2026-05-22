"# Cloud-Storage-System-" 
# ☁️ Cloud Based File Storage System

A simple cloud-based file storage system developed using **Python Flask**, **SQLite**, **HTML/CSS**, and basic cloud storage concepts.
This project allows users to register, login, upload, download, and delete files through a modern dashboard interface.

---

# 🚀 Features

✔ User Registration & Login
✔ Secure Session Handling
✔ File Upload System
✔ File Download System
✔ File Delete Functionality
✔ SQLite Database Integration
✔ Responsive Dashboard UI
✔ Glassmorphism Modern Design
✔ Cloud Storage Simulation

---

# 🛠 Technologies Used

| Technology   | Purpose                 |
| ------------ | ----------------------- |
| Python Flask | Backend Framework       |
| SQLite       | Database                |
| HTML/CSS     | Frontend Design         |
| JavaScript   | Optional Frontend Logic |
| Werkzeug     | Secure File Handling    |

---

# 📂 Project Structure

```text
cloud_project/
│
├── app.py
├── database.db
│
├── templates/
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── uploads/
│
├── static/
│
└── README.md
```

---

# ⚙️ Installation Guide

## 1️⃣ Install Python

Download and install Python from:

[Python Official Website](https://www.python.org/downloads/?utm_source=chatgpt.com)

---

## 2️⃣ Install Flask

Open terminal/cmd:

```bash
pip install flask
```

---

# 🗄️ Database Setup (IMPORTANT)

## Create SQLite Database

Create a file named:

```text
database.db
```

---

## Create Users Table

Run this SQL query:

```sql
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    password TEXT
);
```

---

## Create Files Table

```sql
CREATE TABLE files(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    filename TEXT,
    filepath TEXT
);
```

---

# ▶️ Running The Project

Open terminal in project folder:

```bash
python app.py
```

---

# 🌐 Open in Browser

```text
http://127.0.0.1:5000
```

---

# 🔐 Login System

Users can:

* Create account
* Login securely
* Access dashboard

Session handling is implemented using Flask sessions.

---

# ☁️ File Storage Working

## Upload

Files are uploaded into:

```text
/uploads
```

---

## Download

Users can download uploaded files directly.

---

## Delete

Files are deleted from:

* Database
* Upload folder

---

# 🧠 Project Architecture

```text
User Browser
     ↓
Frontend (HTML/CSS)
     ↓
Flask Backend (Python)
     ↓
SQLite Database
     ↓
Uploads Folder
```

---

# ⚡ Parallelism Concept

This project includes the concept of:

* Threading for file handling
* Concurrent request handling using Flask

---

# 🎯 Future Improvements

* Profile System
* Public/Private Files
* AWS / Firebase Integration
* File Sharing Links
* Storage Analytics
* Folder System

---

# 👨‍💻 Developed By

Muhammad Azeem

---

# 📘 Educational Purpose

This project was developed as a **PDC (Parallel & Distributed Computing)** semester project for learning:

* Cloud Concepts
* Distributed Systems
* File Management
* Flask Web Development
