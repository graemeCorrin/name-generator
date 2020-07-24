from namegenserver.util.grammar import ContextFreeGrammar
from namegenserver.generator.full_name_generator import FullNameGenerator
from namegenserver.generator.fantasy_name_generator import FantasyNameGenerator
from namegenserver.generator.fantasy_location_generator import FantasyLocationGenerator


# FANTASY NAME GENERATOR

__fantasy_name_grammar = ContextFreeGrammar()
__fantasy_name_grammar.add_rule('start', (('prefix', 'suffix'), ('prefix', 'morpheme', 'suffix')))
__fantasy_name_generator = FantasyNameGenerator(__fantasy_name_grammar)


# FANTASY NAME GENERATOR

__fantasy_location_grammar = ContextFreeGrammar()
__fantasy_location_grammar.add_rule('start', (('prefix', 'suffix'), ('prefix', 'morpheme', 'suffix')))
__fantasy_location_generator = FantasyLocationGenerator(__fantasy_location_grammar)


# MAIN NAME GENERATOR

__name_grammar = ContextFreeGrammar()

__name_grammar.add_rule('start', (('proper_noun', ',', 'modifier'),
                                  ('pronoun', 'who_modifier')), (99, 1))

__name_grammar.add_rule('proper_noun', (('full_name',),
                                        ('title_simple', 'full_name'),
                                        ('title_standalone', 'full_name',)))

__name_grammar.add_rule('full_name', (('name_first_phrase',),
                                      ('name_last_phrase',),
                                      ('name_nickname',),
                                      ('name_first_phrase', 'name_nickname'),
                                      ('name_first_phrase', 'name_last_phrase'),
                                      ('name_first_phrase', 'name_nickname', 'name_last_phrase'),
                                      ('name_nickname', 'name_last_phrase')))

__name_grammar.add_rule('name_first_phrase', (('initial',),
                                              ('name_first',),
                                              ('name_fantasy',)), (1, 5, 5))

__name_grammar.add_rule('name_last_phrase', (('initial',),
                                             ('name_last',),
                                             ('name_fantasy',)), (1, 5, 5))

__name_grammar.add_rule('modifier', (('of_who_from',),
                                     ('the', 'title_standalone'),
                                     ('the', 'title_standalone', 'of_who_from'),
                                     ('title_action', 'of', 'noun_thing_phrase')))

__name_grammar.add_rule('of_who_from', (('of_modifier',),
                                        ('who_modifier',),
                                        ('from_modifier',)))

__name_grammar.add_rule('of_modifier', (('of', 'noun_place_phrase'),
                                        ('of', 'noun_thing_phrase')))

__name_grammar.add_rule('who_modifier', (('who', 'adverb_verb_phrase'),))

__name_grammar.add_rule('from_modifier', (('from', 'noun_place_phrase'),))

__name_grammar.add_rule('noun_thing_phrase', (('noun_thing',),
                                              ('adjective_phrase', 'noun_thing')))

__name_grammar.add_rule('noun_place_phrase', (('noun_place',),
                                              ('noun_place_fantasy',)))

__name_grammar.add_rule('adjective_phrase', (('adjective',),
                                             ('adverb', 'adjective_phrase')), (4, 1))

__name_grammar.add_rule('adverb_verb_phrase', (('verb_phrase',),
                                               ('adverb', 'adverb_verb_phrase')), (4, 1))

__name_grammar.add_rule('verb_phrase', (('verb_transitive_phrase',),
                                        ('verb_intransitive_phrase',)))

__name_grammar.add_rule('verb_transitive_phrase', (('verb_transitive',),
                                                   ('verb_transitive', 'noun_thing_phrase')))

__name_grammar.add_rule('verb_intransitive_phrase', (('verb_intransitive',),
                                                     ('verb_intransitive', 'preposition', 'noun_thing_phrase')))

full_name_generator = FullNameGenerator(__name_grammar, __fantasy_name_generator, __fantasy_location_generator)
