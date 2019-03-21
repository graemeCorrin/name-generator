import random
import string
from  sqlalchemy.sql.expression import func
from namegenserver.grammar import name_grammar
from namegenserver.model.givenname import GivenName
from namegenserver.model.surname import SurName


def generate_name(seed: str = '') -> str:
    """
    Generate a random name from a seed. If no seed is provided, the default seed for the random module is used

    :param seed: seed for random function
    :return: name
    """

    if seed:
        random.seed(seed)
    else:
        random.seed()

    result = name_grammar.evaluate()
    name = []

    for terminal in result:
        name.append(__eval_terminal(terminal))

    return ' '.join(name)


def __eval_terminal(terminal: str) -> str:
    """
    Get value for given terminal in the Grammar. If terminal does not correspond to a database table, literal value
    of terminal is returned.

    :param terminal: terminal to evaulate
    :return: value of terminal
    """

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
    given_name = GivenName.query.order_by(func.random()).first()
    return given_name.name

def __get_surname():
    surname = SurName.query.order_by(func.random()).first()
    return surname.name

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
