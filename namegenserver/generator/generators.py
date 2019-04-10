from namegenserver.util.grammar import ContextFreeGrammar
from namegenserver.generator.full_name_generator import FullNameGenerator


# MAIN NAME GENERATOR

__name_grammar = ContextFreeGrammar()

__name_grammar.add_rule('start', (('proper_noun', ',', 'modifier'), ('pronoun', ',', 'who_modifier')), (.99, .01))

__name_grammar.add_rule('proper_noun', (('full_name',), ('simple_title', 'full_name'), ('standalone_title', 'full_name',), ('standalone_title',)))
__name_grammar.add_rule('standalone_title', (('normal_title',), ('professional_title',), ('ruler_title',)))
__name_grammar.add_rule('full_name', (('given',), ('sur',), ('nickname',), ('given', 'nickname'), ('given', 'sur'), ('given', 'nickname', 'sur'), ('nickname', 'sur')))
__name_grammar.add_rule('given', (('initial',), ('given_name',)))
__name_grammar.add_rule('sur', (('initial',), ('surname',)))

__name_grammar.add_rule('modifier', (('article_modifier',), ('of_modifier',), ('who_modifier',), ('from_modifier',)))
__name_grammar.add_rule('article_modifier', (('the', 'adjective_phrase'), ('article', 'noun_phrase')))
__name_grammar.add_rule('of_modifier', (('of', 'location_phrase'), ('of', 'noun_phrase')))
__name_grammar.add_rule('who_modifier', (('who', 'verb_phrase'),))
__name_grammar.add_rule('from_modifier', (('from', 'location_phrase'),))

__name_grammar.add_rule('article', (('a',), ('the',)))
__name_grammar.add_rule('adjective_phrase', (('adjective',), ('adverb', 'adjective_phrase')), (.8, .2))
__name_grammar.add_rule('noun_phrase', (('article', 'noun'), ('noun',), ('article', 'adjective_phrase', 'noun')))
__name_grammar.add_rule('verb_phrase', (('verb',), ('adverb', 'verb_phrase')), (.8, .2))
__name_grammar.add_rule('verb', (('object_verb_phrase',), ('phrase_verb_phrase',)))
__name_grammar.add_rule('object_verb_phrase', (('object_verb',), ('object_verb', 'noun_phrase')))
__name_grammar.add_rule('phrase_verb_phrase', (('phrase_verb',), ('phrase_verb', 'preposition', 'noun_phrase')))

full_name_generator = FullNameGenerator(__name_grammar)
