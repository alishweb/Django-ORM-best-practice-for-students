# Django ORM best practice

## Basic Commands

- Install pipenv:

        $ pip install pipenv

- Install the required packages:

        $ pipenv install

- Activation of the virtual environment

        $ pipenv shell

- run server

        $ python manage.py runserver

## Important commands in Django

- start project

        $ django-admin startproject config .

- Create an app

        $ python manage.py startapp app_name

- run server

        $ python manage.py runserver


## Database creation and filling commands

- create database
#### first open powershell and write this code:
        $ mysql -u root -p
        $ CREATE DATABASE mystore;

-- Then go to the project settings and put your mysql password in the mypassword field

- make migrations command

        $ python manage.py makemigrations

- migrate command 

        $ python manage.py migrate

