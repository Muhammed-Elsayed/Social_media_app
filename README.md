# # Social Media Platform

This is a social media platform built with Django and Django REST Framework (DRF). The platform allows users to create profiles, share posts, like and comment on posts, follow other users, and receive notifications. The project includes a custom authentication system using JWT tokens.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication and authorization using JWT tokens.
- Ability to create, edit, and delete posts.
- Like and comment on posts.
- Follow/unfollow users.
- Real-time notifications for likes, comments, and follows.

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: MySQL
- **Authentication**: JWT (JSON Web Tokens)
- **API Documentation**: Swagger

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Muhammed-Elsayed/Social_media_app
   cd social-media-platform

2. **make virtual environment**

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  
3. **install requirments**
   ```bash
   pip install -r requirements.txt

4. **Update the DATABASES setting in settings.py with your MySQL credentials.**

  
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

4.**migrate and runserver**
  ```bash
  python3 manage.py migrate
  python manage.py runserver






