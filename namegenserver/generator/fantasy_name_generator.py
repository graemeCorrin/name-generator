import random
from namegenserver.generator.generator import Generator


class FantasyNameGenerator(Generator):

    def generate(self, seed: str = ''):
        result = self._evaluate(seed)
        return ''.join(result).capitalize()

    def _evaluate(self, seed: str = '') -> list:
        """
        Evaluate grammar. Ignore the seed.

        :param seed: seed for random function
        :return: result
        """

        result = self._grammar.evaluate()
        name = []

        for terminal in result:
            name.append(self._eval_terminal(terminal))

        return name

    def _eval_terminal(self, terminal: str) -> str:
        """
        Get value for given terminal in the Grammar. If terminal does not correspond to a database table, literal value
        of terminal is returned.

        :param terminal: terminal to evaulate
        :return: value of terminal
        """

        options = {
            'prefix': self.__get_prefix,
            'morpheme': self.__get_morpheme,
            'suffix': self.__get_suffix
        }

        if terminal not in options:
            return terminal
        else:
            return options[terminal]()

    @staticmethod
    def __get_prefix():
        return random.choice(['nas', 'ca', 'zon', 'sri', 'hel', 'viz'])

    @staticmethod
    def __get_morpheme():
        return random.choice(['gou', 'tin', 'ter', 'brem', 'phef', 'us', 'tex', 'joz'])

    @staticmethod
    def __get_suffix():
        return random.choice(['er', 'en', 'ius', 'ous', 'us'])
