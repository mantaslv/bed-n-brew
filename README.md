# Bed-n-Brew Python Project Seed

This repo contains the seed codebase for the MakersBnB project in Python (using 
Flask and Pytest).

Someone in your team should fork this seed repo to their GitHub account.
Everyone in the team should then clone this fork to their local machine to work on it.

> NOTE: If you encounter a `ModuleNotFound` error, deactivate and then reactivate your virtual env. If that doesn't help, please reach out to your coach.

## Setup

```shell
# Set up the virtual environment
; python -m venv bnb-venv

# Activate the virtual environment
; source bnb-venv/bin/activate 

# Install dependencies
(makersbnb-venv); pip install -r requirements.txt

# Install the virtual browser we will use for testing
(makersbnb-venv); playwright install
# If you have problems with the above, contact your coach

# Create a test and development database
(makersbnb-venv); createdb bed_n_brew_db_dev
(makersbnb-venv); createdb bed_n_brew_db_test

# Open lib/database_connection.py and change the database names
(makersbnb-venv); open lib/database_connection.py

# Create a .env file in the root directory
# Add your secret key to the .env file (used for session management and CSRF protection)
echo 'SECRET_KEY="your_secret_key_here"' > .env

# Run the tests (with extra logging)
(makersbnb-venv); pytest -sv

# Run the app
(makersbnb-venv); python app.py

# Now visit http://localhost:5001/index in your browser
```

## Environment Setup

The application uses environment variables for security. You'll need to set these up locally:

1. Create a `.env` file in the root directory of the project
2. Add the following line to your `.env` file:
   ```
   SECRET_KEY="your_secret_key_here"
   ```
   Replace `your_secret_key_here` with a secure random string
3. The `.env` file is already in `.gitignore` to ensure sensitive data isn't committed to the repository

Note: Never commit your actual `.env` file to version control. A `.env.example` file is provided as a template.