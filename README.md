﻿# Match Voice Agency

## Project Description
**Match Voice Agency** is a web application for managing football tournaments, matches, and commentators who provide live commentary for games. The project allows tournament organizers and sports agencies to efficiently track matches, assign commentators, and provide a user-friendly interface.

## Key Features
- **Tournament Management**: Add, edit, and delete tournaments.
- **Match Management**: Create match schedules.
- **Commentator Management**: Assign commentators to matches, view commentator profiles.

## Technologies
The project is built using the following technologies:
- **Backend**: Django
- **Frontend**: Bootstrap
- **Database**: PostgreSQL

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/NazarSerdiuk1/Match-voice-agency.git
   ```
2. Navigate to the project folder:
   ```bash
   cd match_voice_agency
   ```
3. Set up a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/MacOS
   venv\Scripts\activate    # For Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Load test data (if available):
   ```bash
   python manage.py loaddata dump.json
   ```
7. Start the development server:
   ```bash
   python manage.py runserver
   ```
8. Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Core Models
- **Tournament**: Name and description.
- **Match**: Teams, date,tournament.
- **Commentator**: Name, expirience in work.


## Roadmap
- Implement search and filtering for tournaments, matches, and commentators. .

## Authors
- **Nazar Serdiuk** — Backend Development.
- **Nazar Serdiuk** — Frontend Development.

## Match voice agency site
https://match-voice-agency.onrender.com/

