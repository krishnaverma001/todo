# 📝 Django Task Manager

A minimal and clean web based task manager built with Django. Add, update, delete, and mark tasks as complete with a stylish, responsive UI using Poppins font and custom CSS.

## 🚀 Features

- ✅ Create new tasks
- ✏️ Update task titles
- 🗑️ Delete tasks
- ☑️ Mark tasks as complete/incomplete using a checkbox
- 🎨 Strikethrough styling for completed tasks
- 📱 Mobile responsive design

## 🖼️ Screenshots

> ![App Screenshot](app/static/images/SS.png)

---

## 🛠️ Tech Stack

- **Backend:** Django
- **Frontend:** HTML, CSS (custom), Django Templates
- **Database:** SQLite (default Django DB)

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/krishnaverma001/todo.git
cd todo
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py migrate
```
### 5. Run the Development Server
```bash
python manage.py runserver
```

### 6. Update settings
    Ensure DEBUG = True in settings.py for running locally.

Now open your browser and go to:
http://127.0.0.1:8000/

## 📁 Project Structure
```bash
.idea/                        # PyCharm IDE files (should be ignored)
.venv/                        # Virtual environment folder (should be ignored)
app/                          # Django app folder (contains your business logic)
│
├── static/                   # Static files (images, CSS)
│   ├── images/               # Folder for images
│   └── css/                  # Folder for CSS
│       └── style.css         # Main stylesheet
│
├── templates/                # HTML templates
│   ├── index.html            # Template for the main page
│   ├── update.html           # Template for updating tasks
│   └── delete.html           # Template for deleting tasks
│
├── models.py                 # Django models (database schema)
├── tests.py                  # Unit tests for your app
├── forms.py                  # Forms for creating or updating tasks
├── views.py                  # Views to handle requests and logic
└── urls.py                   # URLs for routing app-specific URLs
│
todo/                         # Main project folder
├── manage.py                 # Django management script
├── db.sqlite3                # SQLite database (should be ignored)
├── requirements.txt          # Dependencies for your project
├── README.md                 # Project description
└── .gitignore                # Git ignore file

```
## 🧑‍💻 Author
Krishna Verma

GitHub: @krishnaverma001

This project is for learning and demonstration purposes.