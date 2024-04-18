# Session Authentication

![Session model](image.png)

## Overview
Session authentication is a mechanism used to verify and manage user identity and access within a web application. Unlike traditional authentication methods that require users to provide credentials (such as username and password) with each request, session authentication establishes a temporary session between the user and the server after successful login. This session is typically maintained using a unique identifier stored as a cookie in the user's browser.

## Project description
In this project, Session Authentication is implemented without relying on any additional modules. Session authentication is a common mechanism used to validate and authorize users accessing web applications. While it's typically recommended to utilize established frameworks or modules for authentication, this project aims to provide a deeper understanding of the underlying concepts by implementing it from scratch.

## Key concepts
- The concept of authentication
- Session management (how sessions are created, managed, and terminated in web applications.)
- HTTP cookies are and how they are used to store small pieces of data on the client side (user's browser)
- HTTP requests and responses within a web framework
- Statelessness vs. Statefulness in web applications
- Session expiration and the mechanisms for setting session timeouts.



## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```

## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)