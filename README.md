# nature-sound-recorder-backend
Nature Sound Recorder — Capstone Project Plan

Project Idea: "Nature Sound Recorder" is a web application that allows users to record natural sounds such as rain, birds, and ocean waves, categorize them, and view recordings made by others.




Technologies: Python, Django, DRF, PostgreSQL

Running Steps:

pipenv install django
pipenv shell


django-admin startproject  .
python manage.py startapp 

pipenv install psycopg2-binary

python manage.py makemigrations
python manage.py migrate

 pipenv install django-cors-headers

python manage.py runserver