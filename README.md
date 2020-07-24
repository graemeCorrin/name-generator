
# Name Generator

This project is inspired by the procedurally generated deck names in the Unique Deck Game [KeyForge](https://www.keyforgegame.com/).

It uses a [context-free grammar](https://en.wikipedia.org/wiki/Context-free_grammar) to define the rules that make up a valid name, then evaluates that grammar, making a weighted random choice at each decision point.

## The Grammar
Context-free grammars are described by a four-element tuple, G = (V, Σ, R, S), where
 - V is a finite set of variables (non-terminal)
-  Σ is a finite set terminal symbols
-  R is a set of production rules where each production rule maps a variable to a string s∈(V∪Σ)∗;
-  S a start symbol (which is in V)

### V
||||
|--|--|--|
start|proper_noun|full_name
name_first_phrase|name_last_phrase|modifier
of_who_from|of_modifier|who_modifier
from_modifier|noun_thing_phrase|noun_place_phrase
adjective_phrase|adverb_verb_phrase|verb_phrase
verb_transitive|verb_intransitive|



### Σ
||||
|--|--|--|
adjective|adverb|name_first
name_last|name_nickname|noun_place
noun_thing|preposition|pronoun
title_action|title_simple|title_standalone
verb_intransitive|verb_transitive|initial
name_fantasy|noun_place_fantasy|

### R
 - start → proper_noun + , + modifier
 - start → pronoun + who_modifier

 - proper_noun → full_name
 - proper_noun → title_simple + full_name
 - proper_noun → title_standalone + full_name

 - full_name → name_first_phrase
 - full_name → name_last_phrase
 - full_name → name_nickname
 - full_name → name_first_phrase + name_nickname
 - full_name → name_first_phrase + name_last_phrase
 - full_name → name_first_phrase + name_nickname + name_last_phrase
 - full_name → name_nickname + name_last_phrase

 - name_first_phrase → initial
 - name_first_phrase → name_first
 - name_first_phrase → name_fantasy
 
 - name_last_phrase → of_who_from
 - name_last_phrase → name_last
 - name_last_phrase → name_fantasy

 - modifier → initial
 - modifier → the + title_standalone
 - modifier → the + title_standalone + of_who_from
 - modifier → title_action + of + noun_thing_phrase

 - of_who_from → of_modifier
 - of_who_from → who_modifier
 - of_who_from → from_modifier

 - of_modifier → of + noun_place_phrase
 - of_modifier → of + noun_thing_phrase

 - who_modifier → who + adverb_verb_phrase
 
 - from_modifier → from+ noun_place_phrase
 
 - noun_thing_phrase → noun_thing
 - noun_thing_phrase → adjective_phrase + noun_thing
 
 - noun_place_phrase → noun_place
 - noun_place_phrase → noun_place_fantasy
 
 - adjective_phrase → adjective
 - adjective_phrase → adverb + adjective_phrase 
  
 - adverb_verb_phrase → verb_phrase
 - adverb_verb_phrase → adverb + verb_phrase
  
 - verb_phrase → verb_transitive_phrase
 - verb_phrase → verb_intransitive_phrase
  
 - verb_transitive_phrase → verb_transitive
 - verb_transitive_phrase → verb_transitive + noun_thing_phrase
  
 - verb_intransitive_phrase→ verb_intransitive
 - verb_intransitive_phrase→ verb_intransitive + preposition + noun_thing_phrase
 

### S
 - start

## Examples

Evaluation tree for
**The One who Definitely Really Destroys Obedient Turkeys**
![Context Free Grammar Example 1](https://raw.githubusercontent.com/graemeCorrin/name-generator/master/img/cfg_example_1.png)

Evaluation tree for
**Miss Nasbremus "Sweetie Pie," Savior of Cat Calendars**
![Context Free Grammar Example 1](https://raw.githubusercontent.com/graemeCorrin/name-generator/master/img/cfg_example_2.png)

## Setup

### Requirements
* Python 3.7
* PostgreSQL 12.3

Any very of PostgreSQL should work.  Tested with 9.6 and 12.3.

It will not run on Python 2, and some of the packages break with Python 3.8; they need to be updated before it will run on 3.8.  For now, everything works on 3.7.

**Install required modules into your virtual environment**
```
pip install -r requirements.txt
```

**Create new database**
```
psql
create database name_generator_dev
```

**Initialize database schema**
```
manage.py db upgrade
```


**Populate database**
Run all sql scripts in data folder

## Running the app server

Run
```
manage.py runserver
```

## Adding Migrations
Modify the models
Then, to create a new migration script, run
```
manage.py db migrate
```

Then, to run the new migration script, run
```
manage.py db upgrade
```



## ToDo

 - [x] Build basic server functionality
 - [x] Add random seed option to UI
 - [x] Create Context Free Grammar to build possible name structures
 - [x] Pull name components from database
 - [x] Populate all read-only database tables
 - [x] Add fantasy name generating logic
 - [x] Add location name generating logic
 - [ ] Populate name and location syllable tables
 - [ ] Add redis task queue
 - [ ] Add more options to front-end
 
 
## Known Issues
 - Places need to be split into proper names and normal names.  Proper names should not have adjectives, normal names require an article, but adjectives go between article and noun.
 - Commas should be placed between 2 or more adverbs
 - Should be possible to get multiple adjectives
 
