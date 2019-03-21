import random
import string
from namegenserver.grammar import name_grammar


def generate_name(seed: str = ''):

    if seed:
        random.seed(seed)
    else:
        random.seed()

    result = name_grammar.evaluate()
    name = []

    for terminal in result:
        name.append(__eval_terminal(terminal))

    return ' '.join(name)


def __eval_terminal(terminal):
    options = {
        'pronoun': __get_pronoun,
        'simple_title': __get_simple_title,
        'normal_title': __get_normal_title,
        'professional_title': __get_professional_title,
        'ruler_title': __get_ruler_title,
        'nickname': __get_nickname,
        'initial': __get_initial,
        'given_name': __get_given_name,
        'surname': __get_surname,
        'location_phrase': __get_location_phrase,
        'adjective': __get_adjective,
        'adverb': __get_adverb,
        'object_verb': __get_object_verb,
        'phrase_verb': __get_phrase_verb,
        'preposition': __get_preposition
    }

    if terminal not in options:
        return terminal
    else:
        return options[terminal]()

def __get_pronoun():
    return random.choice(['He', 'She', 'The One', 'They'])

def __get_simple_title():
    return random.choice(['Mr', 'Mrs', 'Ms', 'Miss', 'Dr', 'Sir'])

def __get_normal_title():
    return random.choice(['Madam', 'Master', 'Father', 'Mother'])

def __get_professional_title():
    return random.choice(['Professor', 'Chancellor', 'Principal', 'President', 'Warden'])

def __get_ruler_title():
    return random.choice(['King', 'Queen', 'Emperor', 'Duchess', 'Earl'])

def __get_nickname():
    return '"' + random.choice(['Smalls', 'The Fish', 'Potato', 'Lover of Soup', 'Goose']) + '"'

def __get_initial():
    return random.choice(string.ascii_uppercase) + '.'

def __get_given_name():
    return random.choice(['Bob', 'Sally', 'Gregory', 'Bertha', 'Fred', 'Peter', 'Rebecca', 'Alex', 'Jordan', 'Mary', 'Harry'])

def __get_surname():
    return random.choice(['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'])

def __get_location_phrase():
    return random.choice(['the Pit', 'the Void', 'the airport', 'Walmart', 'under the table'])

def __get_adjective():
    return random.choice(['green', 'fragrant', 'tall', 'large', 'not nice'])

def __get_adverb():
    return random.choice(['very', 'really', 'definitely', 'extremely', 'certainly'])

def __get_object_verb():
    return random.choice(['kills', 'murders', 'licks', 'eats', 'slaps', 'sniffs', 'analyzes', 'avoids'])

def __get_phrase_verb():
    return random.choice(['runs'])

def __get_preposition():
    return random.choice(['to', 'at'])
