# License Management System

A secure **License Management and Validation System** built using **Flask**, **SQLAlchemy**, and **Flask-Login**, designed to manage software licenses with authentication-protected admin access and a public license validation API.

This project follows **backend engineering best practices** such as secure password handling, role-based access control, RESTful APIs, and database-driven license lifecycle management.

---

## 📌 Problem Statement

Software products often require a reliable mechanism to:

* Validate license keys
* Track license expiration
* Revoke compromised or expired licenses
* Manage licenses through a secure admin interface

This system provides a **centralized backend service** to validate licenses and manage them securely.

---

## 🏗️ System Architecture

```
Client / Software
        ↓
License Validation API (JSON)
        ↓
Database (SQLAlchemy ORM)
        ↓
Admin Dashboard (Authenticated)
```

---

## 📂 Project Structure

```
licence_management/
│
├── app.py                 # Flask application entry point
├── config.py              # Application configuration
├── models.py              # Database models (User, License)
├── licence.db             # SQLite database
│
├── templates/             # HTML templates
│   ├── login.html
│   └── admin_dashboard.html
│
├── static/                # Static files (CSS, JS)
│
├── requirements.txt       # Python dependencies
├── README.md
```

---

## ⚙️ Tech Stack

* **Backend:** Flask (Python)
* **Database:** SQLite (via SQLAlchemy ORM)
* **Authentication:** Flask-Login
* **Security:** Bcrypt password hashing
* **Frontend:** HTML + Jinja2 templates
* **API:** RESTful JSON endpoints

---

## 🔑 Key Features

### ✅ License Validation API

* Public endpoint to validate license keys
* Checks:

  * License existence
  * Active status
  * Expiration date

### ✅ Admin Authentication

* Secure login using hashed passwords
* Session-based authentication
* Protected admin routes

### ✅ License Management

* Add new licenses
* View all licenses
* Revoke licenses instantly
* Track license expiration

### ✅ Secure Design

* Password hashing with bcrypt
* Role-based access control (admin)
* ORM-based database access (SQL injection safe)

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/vikash282/licence_management.git
cd licence_management
```

### 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python app.py
```

The app will run on:

```
http://127.0.0.1:5000
```

---

## 🔌 API Usage

### License Validation Endpoint

**POST** `/validate-license`

**Request Body (JSON):**

```json
{
  "licenseKey": "ABC-123-XYZ"
}
```

**Response (Valid License):**

```json
{
  "valid": true
}
```

**Response (Invalid / Expired License):**

```json
{
  "valid": false,
  "message": "License expired"
}
```

---

## 🔐 Admin Dashboard

* Login via `/login`
* Access dashboard at `/admin`
* Features:

  * View all licenses
  * Add new licenses
  * Revoke licenses
  * Logout securely

---

## 🧠 Engineering Practices Followed

* Secure password hashing (bcrypt)
* ORM-based database modeling
* Session-based authentication
* Role-based authorization
* Clean separation of concerns
* RESTful API design
* Production-ready backend patterns

---

## 🚀 Future Improvements

* Token-based authentication (JWT)
* Rate limiting for license validation API
* Dockerization
* CI/CD pipeline
* License usage analytics
* Multi-product license support
* PostgreSQL/MySQL support

**Vikash Pandey**
GitHub: [https://github.com/vikash282](https://github.com/vikash282)
