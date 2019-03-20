import random
import string
from namegenserver.grammar import ContextFreeGrammar

grammar = None


def generate_name(seed: str = ''):

    if not grammar:
        __create_grammar()

    if seed:
        random.seed(seed)
    else:
        random.seed()

    name_grammar = grammar.evaluate()
    name = []

    for terminal in name_grammar:
        name.append(__eval_terminal(terminal))

    return ' '.join(name)


def __create_grammar():
    global grammar
    grammar = ContextFreeGrammar()

    grammar.add_rule('start', (('thing', 'modifier'),))

    grammar.add_rule('thing', (('pronoun',), ('proper_noun',)))
    grammar.add_rule('proper_noun', (('full_name',), ('simple_title', 'full_name'), ('standalone_title', 'full_name',), ('standalone_title',)))
    grammar.add_rule('standalone_title', (('normal_title',), ('professional_title',), ('ruler_title',)))
    grammar.add_rule('full_name', (('given',), ('sur',), ('nickname',), ('given', 'nickname'), ('given', 'sur'), ('given', 'nickname', 'sur'), ('nickname', 'sur')))
    grammar.add_rule('given', (('initial',), ('given_name',)))
    grammar.add_rule('sur', (('initial',), ('surname',)))

    grammar.add_rule('modifier', (('article_modifier',), ('of_modifier',), ('who_modifier',), ('from_modifier',)))
    grammar.add_rule('article_modifier', (('the', 'adjective_phrase'), ('article', 'noun_phrase')))
    grammar.add_rule('of_modifier', (('of', 'location_phrase'), ('of', 'noun_phrase'), ('of', 'article', 'noun_phrase')))
    grammar.add_rule('who_modifier', (('verb_phrase',),))
    grammar.add_rule('from_modifier', (('from', 'location_phrase'),))

    grammar.add_rule('article', (('a',), ('the',)))
    grammar.add_rule('adjective_phrase', (('adjective',), ('adverb', 'adjective_phrase')))
    grammar.add_rule('noun_phrase', (('noun',), ('adjective_phrase', 'noun')))
    grammar.add_rule('verb_phrase', (('adverb',), ('adverb', 'verb_phrase'),))
    grammar.add_rule('verb', (('object_verb_phrase',), ('phrase_verb_phrase',)))
    grammar.add_rule('object_verb_phrase', (('object_verb',), ('object_verb', 'noun_phrase')))
    grammar.add_rule('phrase_verb_phrase', (('phrase_verb',), ('phrase_verb', 'preposition', 'noun_phrase')))


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
