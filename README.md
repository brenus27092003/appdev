# Student Management System

A comprehensive Django-based system for managing student records, courses, and grades.

## Features

- Student information management
- Course management
- Grade recording and tracking
- User-friendly interface with Bootstrap styling

## Requirements

- Python 3.8 or higher
- Django 4.2 or higher
- python-dateutil 2.8.2 or higher

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd student_management_system
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the application at http://127.0.0.1:8000/

## Usage

1. Log in to the admin interface at http://127.0.0.1:8000/admin/
2. Add students, courses, and record grades through the user interface
3. View student details, course information, and grade reports

## Project Structure

- `students/` - Main application directory
  - `models.py` - Database models
  - `views.py` - View functions
  - `forms.py` - Form definitions
  - `templates/` - HTML templates
  - `urls.py` - URL routing

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License. 