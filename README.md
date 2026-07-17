<div align="center">

# 🏙️ Civic Complaint Management System

### A production-style web application for reporting, prioritizing, and managing civic complaints.

> Built with **Flask**, **PostgreSQL**, and **SQLAlchemy**, this project demonstrates backend engineering, authentication, relational database design, analytics dashboards, and cloud deployment.

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)]()
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)]()
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)]()
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)]()
[![Render](https://img.shields.io/badge/Hosted%20on-Render-46E3B7?logo=render)]()

</div>

---

# 📖 Overview

The **Civic Complaint Management System** is a production-style full-stack Flask application designed to streamline the reporting and management of public infrastructure complaints.

Citizens can submit complaints related to roads, electricity, water supply, garbage collection, street lights, and other civic issues through an intuitive web interface.

The system automatically categorizes each complaint using rule-based keyword matching and assigns a priority level based on the severity described by the user. Administrators can securely log in to monitor complaints, update their status, and analyze complaint trends through an interactive dashboard.

The project demonstrates practical software engineering concepts including backend development, authentication, relational database design, CRUD operations, dashboard development, PostgreSQL integration, and cloud deployment.

---

# 🚨 Problem Statement

Municipal complaints are often reported through fragmented communication channels, making it difficult for authorities to manage public issues efficiently.

Common challenges include:

- Difficulty prioritizing urgent complaints
- Lack of centralized complaint tracking
- Poor transparency in complaint resolution
- Delayed response times
- Manual complaint management
- Limited analytical insights for administrators

These challenges reduce operational efficiency and negatively impact citizen satisfaction.

---

# 💡 Solution

The Civic Complaint Management System provides a centralized platform where:

- Citizens can easily register complaints online.
- Complaints are automatically categorized.
- Priority levels are assigned based on complaint descriptions.
- Administrators securely manage complaint status.
- Complaint progress is tracked from **Open → In Progress → Resolved**.
- Dashboard analytics provide insights into complaint distribution and resolution progress.

---

# ✨ Features

## 👥 Citizen Portal

- Submit civic complaints
- Enter complaint location
- Automatic complaint categorization
- Automatic priority assignment
- View submitted complaints
- Filter complaints by category and status

---

## 🔐 Administrator Portal

- Secure administrator authentication
- Session-based login
- Complaint management dashboard
- Update complaint status
- Track complaint lifecycle
- Monitor complaint analytics

---

## 🗂 Complaint Categories

- 🛣 Road & Potholes
- ⚡ Electricity
- 🚰 Water Supply
- 🗑 Garbage Collection
- 💡 Street Lights
- 📌 Other Civic Issues

---

## 🚦 Priority Levels

- 🔴 High
- 🟡 Medium
- 🟢 Low

Priority is assigned automatically based on keywords present in the complaint description.

---

## 📊 Dashboard Features

- Total Complaints
- Open Complaints
- Complaints In Progress
- Resolved Complaints
- High Priority Complaint Count
- Category-wise Complaint Distribution
- Interactive Analytics Dashboard
- Complaint Management Table

---

# 🏗 Application Workflow

```text
Citizen

     │

     ▼

Submit Complaint

     │

     ▼

Rule-Based Category Detection

     │

     ▼

Priority Assignment

     │

     ▼

Store Complaint in PostgreSQL

     │

     ▼

Administrator Dashboard

     │

     ▼

Status Update

(Open → In Progress → Resolved)

     │

     ▼

Complaint Resolution
```

---

# 🎯 Key Highlights

- Production-style Flask Application
- PostgreSQL Database Integration
- SQLAlchemy ORM
- Secure Admin Authentication
- Rule-Based Complaint Classification
- Automatic Priority Assignment
- Dashboard Analytics
- Responsive User Interface
- Cloud Deployment on Render

---
# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3 |
| Backend Framework | Flask |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Frontend | HTML5, CSS3, Bootstrap 5 |
| Template Engine | Jinja2 |
| Authentication | Flask Sessions |
| Data Visualization | Chart.js |
| Deployment | Render |
| Version Control | Git & GitHub |

---

# 🏛 System Architecture

```text
                       Citizen

                          │

                          ▼

                Complaint Submission

                          │

                          ▼

                 Flask Application Server

        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼

 Category Detection   Priority Engine   Input Validation

        │                 │

        └──────────┬──────┘

                   ▼

          PostgreSQL Database

                   │

                   ▼

          Administrator Dashboard

                   │

                   ▼

      Complaint Status Management

(Open → In Progress → Resolved)
```

---

# 🗄 Database Design

### Complaint Table

| Field | Description |
|-------|-------------|
| sno | Primary Key |
| name | Citizen Name |
| location | Complaint Location |
| category | Complaint Category |
| description | Complaint Description |
| priority | High / Medium / Low |
| status | Open / In Progress / Resolved |
| date_created | Complaint Submission Time |

---

# 📂 Project Structure

```text
Civic Complaint Management System
│
├── app.py
├── requirements.txt
├── README.md
├── Procfile
├── runtime.txt
├── .gitignore
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── admin_login.html
│   ├── 403.html
│   └── 404.html
│
└── screenshots/
    ├── homepage.png
    ├── dashboard.png
    ├── login.png
    └── analytics.png
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/kanav-codes/civic-complaint-management-system.git
```

Move inside the project

```bash
cd civic-complaint-management-system
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file (or configure Render Environment Variables).

```env
DATABASE_URL=your_postgresql_database_url

SECRET_KEY=your_secret_key
```

---

# ▶ Running the Application

```bash
python app.py
```

Application will start on

```text
http://127.0.0.1:5000
```

---

# ☁ Deployment

This project is deployed using **Render** with a managed **PostgreSQL** database.

Deployment includes:

- Automatic GitHub deployment
- PostgreSQL integration
- Environment variables
- Gunicorn production server
- HTTPS support

---

# 🌐 Live Demo

## 🚀 Live Application

https://civic-complaint-system-ehvf.onrender.com/

---

# 📸 Screenshots

## 🏠 Home Page

> Add your homepage screenshot here.

```text
screenshots/homepage.png
```

---

## 📝 Complaint Submission

> Add complaint submission screenshot.

```text
screenshots/submission.png
```

---

## 📊 Administrator Dashboard

> Add dashboard screenshot.

```text
screenshots/dashboard.png
```

---

## 📈 Analytics Dashboard

> Add analytics screenshot.

```text
screenshots/analytics.png
```

---
# 🎯 Skills Demonstrated

This project demonstrates practical software engineering and backend development skills relevant to entry-level Software Engineering, Backend Engineering, and Machine Learning Engineering roles.

### Backend Development

- Flask Application Development
- Python Programming
- REST-style Routing
- CRUD Operations
- Request Handling
- Session Management
- Authentication & Authorization

---

### Database Engineering

- PostgreSQL Integration
- SQLAlchemy ORM
- Relational Database Design
- Database Querying
- Data Modeling

---

### Frontend Development

- HTML5
- CSS3
- Bootstrap 5
- Jinja2 Templates
- Responsive Web Design

---

### Software Engineering

- MVC-inspired Project Structure
- Production-ready Project Organization
- Error Handling
- Environment Variable Management
- Git Version Control
- GitHub Repository Management

---

### Deployment

- Render Cloud Deployment
- Gunicorn Production Server
- PostgreSQL Cloud Database
- Environment Configuration

---

# 📚 Learning Outcomes

While building this project, I gained practical experience in:

- Designing a complete Flask application from scratch
- Structuring backend applications using reusable components
- Integrating PostgreSQL with SQLAlchemy ORM
- Implementing secure administrator authentication
- Deploying production-ready applications on Render
- Building responsive user interfaces using Bootstrap
- Managing application configuration using environment variables
- Using Git and GitHub for version control

---

# 🚀 Future Improvements

The current version focuses on core complaint management functionality.

Future improvements include:

- 📷 Complaint Image Upload
- 📍 Google Maps Location Integration
- 📧 Email Notifications
- 🔔 Real-time Complaint Updates
- 🔍 Advanced Search & Filtering
- 📄 Pagination
- 👥 Multi-Administrator Support
- 📊 Advanced Analytics Dashboard
- 🔐 Role-Based Access Control
- 🌐 REST API
- 🤖 Machine Learning-based Complaint Classification
- 📈 Machine Learning-based Severity Prediction
- ☁ AWS / Docker Deployment

---

# 💼 Resume Highlights

### Key Engineering Contributions

- Developed a full-stack civic complaint management application using Flask and PostgreSQL.
- Designed a relational database schema using SQLAlchemy ORM.
- Implemented secure administrator authentication using Flask sessions.
- Built an analytics dashboard for monitoring complaint statistics.
- Automated complaint categorization and priority assignment using rule-based logic.
- Deployed the application to the cloud using Render.

---

# 👨‍💻 Author

## Kanav

**B.Tech Computer Science (Artificial Intelligence & Machine Learning)**

Vivekananda Institute of Professional Studies (GGSIPU)

---

### GitHub

https://github.com/kanav-codes

---

### LinkedIn

https://linkedin.com/in/kanav-bansal24

---

# 🤝 Contributing

Contributions, suggestions, and feedback are always welcome.

If you would like to improve this project:

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 📄 License

This project is released for **educational and portfolio purposes**.

Feel free to explore the code, learn from it, and build upon it.

---

# ⭐ Support

If you found this project useful or interesting, consider giving it a **⭐ Star** on GitHub.

It helps increase the visibility of the project and supports future improvements.

---

<div align="center">

### Thank you for visiting this repository!

**Built with Python • Flask • PostgreSQL • SQLAlchemy • Bootstrap • Render**

</div>
- GitHub Version Control

---
