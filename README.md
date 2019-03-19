# Name Generator

A Web Application for generating names.

## Requirements
* Python 3.7
* PostgreSQL 9.6

## Setup

**Install required modules into your virtual environment**
```
pip install -r requirements.txt
```

**Create new database**
```
psql
create database name_generator_dev
```

**Setup database**
```
manage.py db upgrade
```

## Running the app server

Run
```
manage.py runserver
```


##ToDo

 - [x] Build basic server functionality
 - [x] Add seed option to UI
 - [ ] Seed database through Flask-Migrate / alembic ?
 - [ ] Add possible name constructions
 - [ ] Populate all seed tables
 - [ ] Add fantasy name generating logic
 - [ ] Populate possible name syllables
 - [ ] Add location name generating logic
 - [ ] Add redis task queue
 - [ ] Add more options to front-end