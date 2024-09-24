# Project Title
## Description
This project is a video management application that allows users to upload, update, and delete video content. It includes features for liking, reviewing, and tracking watch time for videos. Additionally, users can register and log in to manage their profiles and interact with content.

## Table of Contents
## Features
- Technologies Used
- Installation
- Usage
- API Endpoints
- Models

## Features
  
- User registration and login system
- Video content upload, update, and deletion
- Like and review system for videos
- Watch time tracking
- Category management for organizing content
- Playlist creation for video collections
- Notification system for user interactions
- Location tracking of users
## Technologies Used
- Backend: Django, Django REST Framework
- Database: SQLite (or any other supported database)
- Frontend: (Optional if applicable)
- Other: Django Debug Toolbar, IPware for IP tracking
## Installation
```
Clone the repository:
git clone <repository-url>
cd <repository-folder>
Create a virtual environment:
```

```
python -m venv venv
source venv/bin/activate
```
## Install dependencies:

``` pip install -r requirements.txt ```
## Run migrations:
``` python manage.py migrate ```
## Create a superuser (optional for admin access):
``` python manage.py createsuperuser ```
## Run the development server:

``` python manage.py runserver```
## Usage
- Register a new user by sending a POST request to /account/create/.
- Log in with the registered user by sending a POST request to /account/login/.

## Manage video content:
- Upload videos using the /content/ endpoint.
- Update video details using PUT requests.
- Delete videos with DELETE requests.
## Interact with videos by liking and reviewing them through their respective endpoints.
- Track watch time using the /videoWatch/ endpoint.
## API Endpoints
## API Endpoints

| Method | Endpoint                         | Description                                    |
|--------|----------------------------------|------------------------------------------------|
| POST   | /account/create/                 | Register a new user                           |
| POST   | /account/login/                  | Log in a user                                 |
| GET    | /content/                        | Retrieve all video content                     |
| POST   | /content/                        | Upload a new video content                     |
| PUT    | /content/<int:pk>/               | Update an existing video content               |
| DELETE | /content/<int:pk>/               | Delete a video content                         |
| POST   | /video/<int:video_id>/like/     | Like a video                                  |
| POST   | /review/                         | Submit a review for a video                   |
| GET    | /videoWatch/                     | Retrieve watch time data                       |
| POST   | /videoWatch/                     | Track watch time for a video                  |
| GET    | /location/                       | Retrieve the location of the user             |
