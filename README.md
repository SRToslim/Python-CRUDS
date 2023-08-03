# Python CRUDS Project

## First create directory to make a virtual environment
python -m venv env

## Download the zip file
Download and upzip it and past all file into the same directory of env

## Active the virtual environment
env\scripts\activate

## Install package
pip install -r requirements.txt

## Migrate
python manage.py migrate

## Super User
python manage.py createsuperuser

## Rub Server
python manage.py runserver
