import random
import string
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

        self.__adjective_list = []
        self.__adverb_list = []
        self.__name_first_list = []
        self.__name_last_list = []
        self.__name_nickname_list = []
        self.__noun_place_list = []
        self.__noun_thing_list = []
        self.__preposition_list = []
        self.__pronoun_list = []
        self.__title_action_list = []
        self.__title_simple_list = []
        self.__title_standalone_list = []
        self.__verb_intransitive_list = []
        self.__verb_transitive_list = []

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

    def __get_adjective(self):
        if len(self.__adjective_list) == 0:
            self.__adjective_list = Adjective.query.order_by(Adjective.id).all()
        return random.choice(self.__adjective_list).value

    def __get_adverb(self):
        if len(self.__adverb_list) == 0:
            self.__adverb_list = Adverb.query.order_by(Adverb.id).all()
        return random.choice(self.__adverb_list).value

    def __get_name_first(self):
        if len(self.__name_first_list) == 0:
            self.__name_first_list = NameFirst.query.order_by(NameFirst.id).all()
        return random.choice(self.__name_first_list).value

    def __get_name_last(self):
        if len(self.__name_last_list) == 0:
            self.__name_last_list = NameLast.query.order_by(NameLast.id).all()
        return random.choice(self.__name_last_list).value

    def __get_name_nickname(self):
        if len(self.__name_nickname_list) == 0:
            self.__name_nickname_list = NameNickname.query.order_by(NameNickname.id).all()
        return '"' + random.choice(self.__name_nickname_list).value + '"'

    def __get_noun_place(self):
        if len(self.__noun_place_list) == 0:
            self.__noun_place_list = NounPlace.query.order_by(NounPlace.id).all()
        return random.choice(self.__noun_place_list).value

    def __get_noun_thing(self):
        if len(self.__noun_thing_list) == 0:
            self.__noun_thing_list = NounThing.query.order_by(NounThing.id).all()
        return random.choice(self.__noun_thing_list).value

    def __get_preposition(self):
        if len(self.__preposition_list) == 0:
            self.__preposition_list = Preposition.query.order_by(Preposition.id).all()
        return random.choice(self.__preposition_list).value

    def __get_pronoun(self):
        if len(self.__pronoun_list) == 0:
            self.__pronoun_list = NameNickname.query.order_by(Pronoun.id).all()
        return random.choice(self.__pronoun_list).value

    def __get_title_action(self):
        if len(self.__title_action_list) == 0:
            self.__title_action_list = TitleAction.query.order_by(TitleAction.id).all()
        return random.choice(self.__title_action_list).value

    def __get_title_simple(self):
        if len(self.__title_simple_list) == 0:
            self.__title_simple_list = TitleSimple.query.order_by(TitleSimple.id).all()
        return random.choice(self.__title_simple_list).value

    def __get_title_standalone(self):
        if len(self.__title_standalone_list) == 0:
            self.__title_standalone_list = TitleStandalone.query.order_by(TitleStandalone.id).all()
        return random.choice(self.__title_standalone_list).value

    def __get_verb_intransitive(self):
        if len(self.__verb_intransitive_list) == 0:
            self.__verb_intransitive_list = VerbIntransitive.query.order_by(VerbIntransitive.id).all()
        return random.choice(self.__verb_intransitive_list).value

    def __get_verb_transitive(self):
        if len(self.__verb_transitive_list) == 0:
            self.__verb_transitive_list = VerbTransitive.query.order_by(VerbTransitive.id).all()
        return random.choice(self.__verb_transitive_list).value

    @staticmethod
    def __get_initial():
        return random.choice(string.ascii_uppercase) + '.'

    def __get_name_fantasy(self):
        return self.__fantasy_name_generator.generate()

    def __get_noun_place_fantasy(self):
        return self.__fantasy_location_generator.generate()
