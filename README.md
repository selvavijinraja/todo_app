# 📝 Todo App

## 📌 Overview
The Todo App is a simple web application built with **Django** that allows users to manage their daily tasks. It demonstrates core concepts of web development such as models, views, templates, and database integration, while maintaining a clean and modular structure.  

This project is designed as a beginner-friendly introduction to Django and serves as a foundation for building more advanced task management systems.

---

## ⚙️ Features
- Add new tasks with a title/description
- View all tasks in a list format
- Persistent storage using **SQLite**
- Simple and clean HTML templates
- Extensible structure for CRUD operations (update, delete, mark complete)

---

## 📂 Project Structure
todo_app/ 
│ 
├── manage.py # Django project entry point 
├── db.sqlite3 # SQLite database 
├── todo/ # Core app logic (models, views, urls) 
├── todo_main/ # Additional app module 
├── templates/ # HTML templates for UI 
└── README.md # Project documentation

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Django installed (`pip install django`)

### Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/selvavijinraja/todo_app.git
   cd todo_app
2. Apply migrations:
   python manage.py migrate
3. Start the development server:
   python manage.py runserver
4. Open your browser at http://127.0.0.1:8000/ to use the app.
