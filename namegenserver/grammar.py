import random


class ContextFreeGrammar:

    def __init__(self):
        self.__start = None
        self.__rules = {}

    def add_rule(self, key: str, options: tuple):
        """
        Add a rule to the Context Free Grammar. The left side of the first rule added will be the starting point

        :param key: left side of the Context Free Grammar rule
        :param options: right side of the Context Free Grammar rule
        """

        if key in self.__rules:
            raise ValueError(f'key:{key} already exists within the Grammar')

        try:
            x = options[0][0]
        except:
            raise ValueError('Rules must be of an iterable of iterables')

        if not self.__rules:
            self.__start = key

        self.__rules[key] = options

    def evaluate(self) -> list:
        """
        Evaluate grammar starting at the Start rule

        :return: Result of evaluation
        """

        return self.__eval_recur(self.__start)

    def __eval_recur(self, key: str) -> list:
        """
        Evaluate a rule of the grammar using recursion

        :param key: key of the current rule to evaluate
        :return: result of evaluating current rule
        """

        options = self.__rules[key]
        option = random.choice(options)

        return_val = []
        for value in option:

            if value in self.__rules:
                return_val += self.__eval_recur(value)
            else:
                return_val.append(value)

        return return_val


name_grammar = ContextFreeGrammar()

name_grammar.add_rule('start', (('thing', 'modifier'),))

name_grammar.add_rule('thing', (('pronoun',), ('proper_noun',)))
name_grammar.add_rule('proper_noun', (('full_name',), ('simple_title', 'full_name'), ('standalone_title', 'full_name',), ('standalone_title',)))
name_grammar.add_rule('standalone_title', (('normal_title',), ('professional_title',), ('ruler_title',)))
name_grammar.add_rule('full_name', (('given',), ('sur',), ('nickname',), ('given', 'nickname'), ('given', 'sur'), ('given', 'nickname', 'sur'), ('nickname', 'sur')))
name_grammar.add_rule('given', (('initial',), ('given_name',)))
name_grammar.add_rule('sur', (('initial',), ('surname',)))

name_grammar.add_rule('modifier', (('article_modifier',), ('of_modifier',), ('who_modifier',), ('from_modifier',)))
name_grammar.add_rule('article_modifier', (('the', 'adjective_phrase'), ('article', 'noun_phrase')))
name_grammar.add_rule('of_modifier', (('of', 'location_phrase'), ('of', 'noun_phrase'), ('of', 'article', 'noun_phrase')))
name_grammar.add_rule('who_modifier', (('verb_phrase',),))
name_grammar.add_rule('from_modifier', (('from', 'location_phrase'),))

name_grammar.add_rule('article', (('a',), ('the',)))
name_grammar.add_rule('adjective_phrase', (('adjective',), ('adverb', 'adjective_phrase')))
name_grammar.add_rule('noun_phrase', (('noun',), ('adjective_phrase', 'noun')))
name_grammar.add_rule('verb_phrase', (('adverb',), ('adverb', 'verb_phrase'),))
name_grammar.add_rule('verb', (('object_verb_phrase',), ('phrase_verb_phrase',)))
name_grammar.add_rule('object_verb_phrase', (('object_verb',), ('object_verb', 'noun_phrase')))
name_grammar.add_rule('phrase_verb_phrase', (('phrase_verb',), ('phrase_verb', 'preposition', 'noun_phrase')))
