import random
from namegenserver.generator.generator import Generator


class FantasyLocationGenerator(Generator):

    def generate(self, seed: str = ''):
        result = self._evaluate(seed)
        return ''.join(result).capitalize()

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
        return random.choice(['aber', 'fin', 'inver', 'wes', 'tre', 'nan'])

    @staticmethod
    def __get_morpheme():
        return random.choice(['keld', 'mere', 'le', 'tarn', 'fos', 'ey', 'usk', 'ar'])

    @staticmethod
    def __get_suffix():
        return random.choice(['cester', 'ford', 'mouth', 'stead', 'ton', 'gard'])
