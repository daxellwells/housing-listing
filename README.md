# Simple Flask Backend utilizing SQLite

- Housing listing app built with Flask and SQLite

- Utilizes sqlite but implementation can be adapted to MySQL or PostgreSQL

## Features
- Submit listings via HTML
- View all submitted listings in a table
- Server-side validation for listing submissions

## How to run the app:
1. Install dependencies:
- Install Flask
    - pip install Flask

2. Run the app:
- "flask run" command in the command line
- flask will return to you your local_ip that the server is running on
    - usually http:127.0.0.1:5000


3. Open browser
- Connect to {local_ip}/submit-form to submit a listing
- Connect to {local_ip}/listings to view all listings