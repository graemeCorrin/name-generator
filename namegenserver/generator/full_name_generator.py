import random
import string
from sqlalchemy.sql.expression import func
from namegenserver.model.adjective import Adjective
from namegenserver.model.adverb import Adverb
from namegenserver.model.name_first import NameFirst
from namegenserver.model.name_last import NameLast
from namegenserver.model.name_nickname import NameNickname
from namegenserver.model.noun_place import NounPlace
from namegenserver.model.noun_thing import NounThing
from namegenserver.model.preposition import Preposition
from namegenserver.model.pronoun import Pronoun
from namegenserver.model.title_action import TitleAction
from namegenserver.model.title_simple import TitleSimple
from namegenserver.model.title_standalone import TitleStandalone
from namegenserver.model.verb_transitive import VerbTransitive
from namegenserver.model.verb_intransitive import VerbIntransitive
from namegenserver.generator.generator import Generator
from namegenserver.generator.fantasy_name_generator import FantasyNameGenerator
from namegenserver.generator.fantasy_location_generator import FantasyLocationGenerator
from namegenserver.util.grammar import ContextFreeGrammar


class FullNameGenerator(Generator):

    def __init__(self, grammar: ContextFreeGrammar,
                 fantasy_name_generator: FantasyNameGenerator,
                 fantasy_location_generator: FantasyLocationGenerator):
        super().__init__(grammar)
        self.__fantasy_name_generator = fantasy_name_generator
        self.__fantasy_location_generator = fantasy_location_generator

    def generate(self, seed: str = ''):
        result = self._evaluate(seed)
        name = ' '.join(result)
        name_fixed = name.replace('" , ', '," ').replace(' , ', ', ')
        return name_fixed

    def _eval_terminal(self, terminal: str) -> str:
        """
        Get value for given terminal in the Grammar. If terminal does not correspond to a database table, literal value
        of terminal is returned.

        :param terminal: terminal to evaulate
        :return: value of terminal
        """

        options = {
            'adjective': self.__get_adjective,
            'adverb': self.__get_adverb,
            'name_first': self.__get_name_first,
            'name_last': self.__get_name_last,
            'name_nickname': self.__get_name_nickname,
            'noun_place': self.__get_noun_place,
            'noun_thing': self.__get_noun_thing,
            'preposition': self.__get_preposition,
            'pronoun': self.__get_pronoun,
            'title_action': self.__get_title_action,
            'title_simple': self.__get_title_simple,
            'title_standalone': self.__get_title_standalone,
            'verb_intransitive': self.__get_verb_intransitive,
            'verb_transitive': self.__get_verb_transitive,
            'initial': self.__get_initial,
            'name_fantasy': self.__get_name_fantasy,
            'noun_place_fantasy': self.__get_noun_place_fantasy
        }

        if terminal not in options:
            return terminal
        else:
            return options[terminal]()

    @staticmethod
    def __get_adjective():
        return Adjective.query.order_by(func.random()).first().value

    @staticmethod
    def __get_adverb():
        return Adverb.query.order_by(func.random()).first().value

    @staticmethod
    def __get_name_first():
        return NameFirst.query.order_by(func.random()).first().value

    @staticmethod
    def __get_name_last():
        return NameLast.query.order_by(func.random()).first().value

    @staticmethod
    def __get_name_nickname():
        return '"' + NameNickname.query.order_by(func.random()).first().value + '"'

    @staticmethod
    def __get_noun_place():
        return NounPlace.query.order_by(func.random()).first().value

    @staticmethod
    def __get_noun_thing():
        return NounThing.query.order_by(func.random()).first().value

    @staticmethod
    def __get_preposition():
        return Preposition.query.order_by(func.random()).first().value

    @staticmethod
    def __get_pronoun():
        return Pronoun.query.order_by(func.random()).first().value

    @staticmethod
    def __get_title_action():
        return TitleAction.query.order_by(func.random()).first().value

    @staticmethod
    def __get_title_simple():
        return TitleSimple.query.order_by(func.random()).first().value

    @staticmethod
    def __get_title_standalone():
        return TitleStandalone.query.order_by(func.random()).first().value

    @staticmethod
    def __get_verb_intransitive():
        return VerbIntransitive.query.order_by(func.random()).first().value

    @staticmethod
    def __get_verb_transitive():
        return VerbTransitive.query.order_by(func.random()).first().value

    @staticmethod
    def __get_initial():
        return random.choice(string.ascii_uppercase) + '.'

    def __get_name_fantasy(self):
        return self.__fantasy_name_generator.generate()

    def __get_noun_place_fantasy(self):
        return self.__fantasy_location_generator.generate()
