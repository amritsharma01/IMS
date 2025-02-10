# Examination Invigilator Management System

## Overview
The **Examination Invigilator Management System** is a web-based application designed to streamline the process of managing invigilators and examination schedules. Built using **Django**, it offers a responsive and user-friendly interface with secure authentication and role-based access control.

## Features
- **User Authentication**: Secure login system with role-based access control (Admin & Invigilator).
- **CRUD Operations**: Manage invigilators and exam schedules efficiently.
- **Responsive UI**: Designed with **HTML, CSS, and Bootstrap** for a seamless experience across devices.
- **Data Privacy & Compliance**: Ensures secure handling of user data.

## Tech Stack
- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Django
- **Database**: SQLite (configurable)

## Installation & Setup
```sh
# Clone the repository
git clone https://github.com/amritsharma01/IMS.git
cd invigilator-management

# Create virtual environment
python -m venv venv
source venv/bin/activate  # (Linux/macOS)
venv\Scripts\activate  # (Windows)

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the server
python manage.py runserver
```

## Usage
- **Admin** can add, update, and remove invigilators.
- **Invigilators** can view their assigned schedules.

## Future Enhancements
- **Email notifications** for schedule updates.
- **Automated scheduling system**.
- **Detailed reporting & analytics**.



## Contributors
- **Amrit Sharma** - [amritsharma1027@gmail.com](mailto:amritsharma1027@gmail.com)
