# Flask Notes App

This is a simple Flask web application that allows users to sign up, add, and delete notes. The project uses Flask, Flask-SQLAlchemy, Flask-Login, and other libraries to create a basic note-taking platform.

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package installer)
- Virtualenv (optional but recommended)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/flask-notes-app.git

   cd flask-notes-app
   ```

2. ** Set up the database: **

```bash

flask db init
flask db migrate
flask db upgrade
```

4. Running the Application

**_ Run the Flask development server: _**

```bash
 flask run
```

Visit http://localhost:5000 in your web browser to access the application.

** Features **

- User Sign-up: Users can create accounts with a unique email address and a password.

- Note Addition: Authenticated users can add notes with a title and content.

- Note Deletion: Authenticated users can delete their notes.

** Project Structure **
-website/: Contains the main Flask application code.

- **init**.py: Initializes the Flask app.
- **models**.py: Defines the database models (User, Note).
- **views**.py: Defines the routes and views.
- **auth**.py: Handles user authentication and authorization.
  ...
- static/: Contains static files ( JS).

- templates/: Contains HTML templates.

- requirements.txt: Lists the project dependencies.

- **main**.py: Entry point for running the application.

Contributing
Feel free to contribute to the project by creating issues or pull requests. Your feedback and contributions are welcome!
