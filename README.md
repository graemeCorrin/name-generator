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

## ToDo

 - [x] Build basic server functionality
 - [x] Add random seed option to UI
 - [ ] Populate database through Flask-Migrate / alembic ?
 - [x] Create Context Free Grammar to build possible name structures
 - [ ] Pull name components from database
 - [ ] Populate all read-only database tables
 - [ ] Add fantasy name generating logic
 - [ ] Add location name generating logic
 - [ ] Populate name and location syllable tables
 - [ ] Add redis task queue
 - [ ] Add more options to front-end