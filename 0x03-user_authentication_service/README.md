# User authentication service

This project is aimed at developing a user authentication service using Flask, SQLAlchemy, and bcrypt. The service provides endpoints for user registration, login, logout, profile management, password reset, and more.

## Overview
This project builds on the previous concepts of basic and session authentication. It aims to implement a user authentication system using Flask, a lightweight WSGI web application framework. It follows industry best practices by using SQLAlchemy for database interactions and bcrypt for password hashing. The project includes various tasks such as creating user models, implementing registration, login, logout, profile management, password reset functionalities, and end-to-end integration tests.

## Learning objectives
- Gain understanding of API routing in Flask
- Learn to work with cookies and session management
- Understand how to use SQLAlchemy for database interactions
- Implement password hashing for secure user authentication
- Gain experience in building RESTful APIs with Flask

## Environment and setup
- Required packages: Flask, SQLAlchemy, bcrypt
To install the packages run:
        * `pip3 install flask sqlalchemy bcrypt`


## Project structure
- `app.py`: Main Flask application file with route definitions
- `auth.py`: Auth class implementation for user authentication
- `db.py`: DB class implementation for database interactions
- `user.py`: User model definition using SQLAlchemy
- `main.py`: Integration test module for end-to-end testing


## Usage
1. Start the Flask app: `python3 app.py`
2. Access the API endpoints using curl or any API testing tool.

## Testing
To run end-to-end integration tests, execute the main.py module
- `python3 main.py`
