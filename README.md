<div align="center">

# 🏙️ Civic Complaint Management System

### A centralized web application for reporting, prioritizing, and tracking civic complaints.

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)]()
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)]()
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)]()
[![Render](https://img.shields.io/badge/Hosted%20on-Render-46E3B7?logo=render)]()

</div>

---

# 📖 Overview

The Civic Complaint Management System is a full-stack web application that helps organize and manage public infrastructure complaints submitted by citizens.

The platform allows users to report civic issues such as road potholes, electricity failures, water leakage, garbage accumulation, damaged streetlights, and other public safety concerns.

Each complaint is automatically categorized and assigned a priority level based on its description. Administrators can monitor complaints through a dashboard and update their status from **Open** to **In Progress** and **Resolved**.

This project demonstrates backend development, relational database design, CRUD operations, and deployment of a production-style Flask application.

---

# 🚨 Problem Statement

Many civic complaints are handled through fragmented communication channels, making it difficult to:

- Prioritize urgent complaints
- Track complaint progress
- Monitor resolution status
- Maintain transparency
- Organize large volumes of complaints

Without a centralized system, response times increase and complaint management becomes inefficient.

---

# 💡 Solution

This application provides a centralized complaint management platform where:

- Citizens can submit complaints.
- Complaints are automatically categorized.
- Priority levels are assigned based on complaint severity.
- Authorities can track complaint status.
- Dashboard provides an overview of complaint statistics.

---

# ✨ Features

## Citizen Portal

- Register civic complaints
- Location-based complaint submission
- Automatic complaint categorization
- Automatic priority assignment

---

## Complaint Categories

- 🛣 Road & Potholes
- ⚡ Electricity
- 🚰 Water Supply
- 🗑 Garbage
- 💡 Street Lights
- 🚨 Public Safety
- 📌 Other

---

## Priority Levels

- 🔴 High
- 🟡 Medium
- 🟢 Low

---

## Dashboard

- Total Complaints
- Open Complaints
- Complaints In Progress
- Resolved Complaints
- High Priority Complaint Count
- Category-wise Complaint Distribution

---

# 🏗 Workflow

```text
Citizen

    │

    ▼

Submit Complaint

    │

    ▼

Automatic Category Detection

    │

    ▼

Priority Assignment

    │

    ▼

Store in PostgreSQL Database

    │

    ▼

Dashboard

    │

    ▼

Status Update

    │

    ▼

Resolved
```

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Backend | Flask |
| Language | Python |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Frontend | HTML5, CSS3 |
| Templates | Jinja2 |
| Version Control | Git & GitHub |
| Deployment | Render |

---

# 📂 Project Structure

```text
.
├── app.py
├── templates/
├── static/
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/your-username/repository.git
```

Move into the project

```bash
cd repository
```

Create a virtual environment

```bash
python -m venv env
```

Activate virtual environment

Windows

```bash
env\Scripts\activate
```

Linux / macOS

```bash
source env/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure environment variables

```
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
```

Run the application

```bash
python app.py
```

---

# 🌐 Live Demo

**Live Application**

👉 [(https://civic-complaint-system-ehvf.onrender.com/)]

---

# 📸 Screenshots

## Home Page

<img width="1366" height="643" alt="image" src="https://github.com/user-attachments/assets/6bb6456a-8a56-4a40-b87d-035bb114a7e4" />
<img width="1116" height="267" alt="image" src="https://github.com/user-attachments/assets/2865bcab-ca6e-48ca-8ac2-0ed1c9813940" />

---

## Complaint Submission

<img width="1118" height="251" alt="image" src="https://github.com/user-attachments/assets/aeeb5744-9a1f-4203-ad0c-d6c0aaf0f830" />
<img width="1080" height="219" alt="image" src="https://github.com/user-attachments/assets/a16841f5-79db-46f1-a36c-11af04832028" />

---

## Dashboard

<img width="1365" height="639" alt="image" src="https://github.com/user-attachments/assets/3e3e2d1f-f43a-4c22-a32d-c8b4e1863195" />
<img width="1366" height="573" alt="image" src="https://github.com/user-attachments/assets/f5efdc6d-c39f-4377-8c8d-2304af572a94" />

---

# 🎯 Skills Demonstrated

- Flask Application Development
- PostgreSQL Integration
- SQLAlchemy ORM
- CRUD Operations
- Backend Routing
- Relational Database Design
- Template Rendering
- Dashboard Development
- Cloud Deployment
- Git Version Control

---

# 🚀 Future Improvements

- User Authentication
- Admin Panel
- Complaint Search & Filters
- Complaint Image Upload
- Email Notifications
- Interactive Maps
- Analytics Dashboard
- REST API
- AI-based Complaint Classification
- Machine Learning-based Severity Prediction

---

# 👨‍💻 Author

**Kanav**

B.Tech Computer Science (AI & ML)

Vivekananda Institute of Professional Studies (GGSIPU)

GitHub: https://github.com/kanav-codes

LinkedIn: https://linkedin.com/in/kanav-bansal24
---

# 📄 License

This project is intended for educational and portfolio purposes.

---

<div align="center">

⭐ If you found this project useful, consider giving it a Star.

</div>
