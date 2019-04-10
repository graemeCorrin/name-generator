import random
import string
from sqlalchemy.sql.expression import func
from namegenserver.model.givenname import GivenName
from namegenserver.model.surname import SurName
from namegenserver.generator.generator import Generator


class FullNameGenerator(Generator):

    def _eval_terminal(self, terminal: str) -> str:
        """
        Get value for given terminal in the Grammar. If terminal does not correspond to a database table, literal value
        of terminal is returned.

        :param terminal: terminal to evaulate
        :return: value of terminal
        """

        options = {
            'pronoun': self.__get_pronoun,
            'simple_title': self.__get_simple_title,
            'normal_title': self.__get_normal_title,
            'professional_title': self.__get_professional_title,
            'ruler_title': self.__get_ruler_title,
            'nickname': self.__get_nickname,
            'initial': self.__get_initial,
            'given_name': self.__get_given_name,
            'surname': self.__get_surname,
            'location_phrase': self.__get_location_phrase,
            'adjective': self.__get_adjective,
            'adverb': self.__get_adverb,
            'noun': self.__get_noun,
            'object_verb': self.__get_object_verb,
            'phrase_verb': self.__get_phrase_verb,
            'preposition': self.__get_preposition
        }

        if terminal not in options:
            return terminal
        else:
            return options[terminal]()

    @staticmethod
    def __get_pronoun():
        return random.choice(['He', 'She', 'The One', 'They'])

    @staticmethod
    def __get_simple_title():
        return random.choice(['Mr', 'Mrs', 'Ms', 'Miss', 'Dr', 'Sir'])

    @staticmethod
    def __get_normal_title():
        return random.choice(['Madam', 'Master', 'Father', 'Mother'])

    @staticmethod
    def __get_professional_title():
        return random.choice(['Professor', 'Chancellor', 'Principal', 'President', 'Warden'])

    @staticmethod
    def __get_ruler_title():
        return random.choice(['King', 'Queen', 'Emperor', 'Duchess', 'Earl'])

    @staticmethod
    def __get_nickname():
        return '"' + random.choice(['Smalls', 'The Fish', 'Potato', 'Lover of Soup', 'Goose']) + '"'

    @staticmethod
    def __get_initial():
        return random.choice(string.ascii_uppercase) + '.'

    @staticmethod
    def __get_given_name():
        given_name = GivenName.query.order_by(func.random()).first()
        return given_name.name

    @staticmethod
    def __get_surname():
        surname = SurName.query.order_by(func.random()).first()
        return surname.name

    @staticmethod
    def __get_location_phrase():
        return random.choice(['the Pit', 'the Void', 'the airport', 'Walmart', 'under the table'])

    @staticmethod
    def __get_adjective():
        return random.choice(['green', 'fragrant', 'tall', 'large', 'not nice'])

    @staticmethod
    def __get_adverb():
        return random.choice(['very', 'really', 'definitely', 'extremely', 'certainly'])

    @staticmethod
    def __get_noun():
        return random.choice(['soup', 'hot dogs', 'Christmas tree', 'ball', 'box'])

    @staticmethod
    def __get_object_verb():
        return random.choice(['kills', 'murders', 'licks', 'eats', 'slaps', 'sniffs', 'analyzes', 'avoids'])

    @staticmethod
    def __get_phrase_verb():
        return random.choice(['runs'])

    @staticmethod
    def __get_preposition():
        return random.choice(['to', 'at'])
