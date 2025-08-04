
# WebKnowledge

**WebKnowledge** is a web platform built with Django for a college work designed to connect individuals with special learning needs to qualified and experienced teachers. The system facilitates inclusive and personalized education by helping students find instructors who match their specific requirements.

## Purpose

Provide a digital environment that:

- Helps students with learning difficulties find personalized support.
- Allows specialized teachers to offer their services directly.
- Promotes educational inclusion through accessible technology.

## Key Features

- **User Registration for Students and Teachers**
  - Profiles with specialization, subject area, availability, and description.
- **Dynamic Homepage for Students**
  - Displays available teachers, filterable by specialization and more.
- **Simple Messaging System (CRUD-based)**
  - Students can initiate a conversation with teachers through a single button.
- **Search Bar**
  - Allows filtering of teachers by specialization or keywords.
- **Custom Templates**
  - Different layouts and dashboards for students and teachers.
- **Login and Authentication System**
  - Secure access to user dashboards and features.

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Django Templates
- **Database:** SQLite (for development), PostgreSQL (planned support)
- **Dev Environment:** GitHub Codespaces

## Running the Project Locally

```bash
git clone https://github.com/your-username/webknowledge.git
cd webknowledge
python -m venv venv
source venv/bin/activate        # On Linux/macOS
venv\Scripts\activate           # On Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open your browser at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
