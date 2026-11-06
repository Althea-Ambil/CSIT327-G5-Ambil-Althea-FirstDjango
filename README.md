# CampusConnect
### CSIT327-G5 – First Django Project

**Developer:** Althea Ambil  
**Section:** BSIT-2 (Replace with your exact section if needed)  
**Project Name:** CampusConnect

## Project Description

CampusConnect is a Django web application that allows users to create accounts, log in, and access a dashboard. The system includes user registration, authentication, and profile management features.

## Features

- User Registration
- User Login and Logout
- Dashboard
- User Profile Management
- Admin Panel
- Bootstrap 5 UI

## Technologies Used

- Python
- Django
- HTML
- CSS
- Bootstrap 5
- SQLite

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Althea-Ambil/CSIT327-G5-Ambil-Althea-FirstDjango.git
```

### 2. Navigate to the Project Folder

```bash
cd CSIT327-G5-Ambil-Althea-FirstDjango
```

### 3. Create a Virtual Environment

```bash
py -m venv .venv
```

### 4. Activate the Virtual Environment

```bash
.\.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
py manage.py migrate
```

### 7. Run the Django Development Server

```bash
py manage.py runserver
```

### 8. Open the Application

Visit the following URL in your browser:

http://127.0.0.1:8000/

## Project Structure

```text
campusconnect/
├── accounts/
├── campusconnect/
├── dashboard/
├── templates/
│   ├── dashboard/
│   ├── registration/
│   └── base.html
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## Author

Althea Ambil  
BSIT – CSIT327
