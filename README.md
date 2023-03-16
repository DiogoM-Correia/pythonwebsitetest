How it works (for windows):

1 - Open the terminal windows in a given folder (Desktop for example)
    cd Desktop

2 - Download the git environment 
    git clone https://github.com/DiogoM-Correia/juntossomosmais.git

3 - Change directory to the project and inside the main folder (Website)
    cd juntossomosmais

4 - If you don't have, install the pipenv package to open the virtual environment
    pip install pipenv

5 - Launch the virtual environment
    pipenv sheel

6 - Change again directory to the main folder: Website
    cd Website

7 - Run the following commands to run migrations and start website 
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

8 - Available pages:
    - / -> home page 
    - /upload -> page to upload both CSV and JSON files
    - /api/users -> page to retrive title, first and last names of users

Notes:
1. No information to determine country region (default 'Sul' for now)
2. It was not possible to develop the filtering component and pagination of the API
3. The front end was not the focus
4. It was prepared the output method for the JSON format but not completly implemented