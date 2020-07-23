import random
from abc import ABCMeta, abstractmethod
from namegenserver.util.grammar import ContextFreeGrammar


class Generator(object):

    __metaclass__ = ABCMeta

    def __init__(self, grammar: ContextFreeGrammar):
        self._grammar = grammar

    @abstractmethod
    def generate(self, seed: str = '') -> str:
        """
        Generate the final result after any required post processing

        :param seed: seed for random function
        :return: result
        """
        pass

    def _evaluate(self, seed: str = '') -> list:
        """
        Evaluate grammar. Seed random with given seed.
        If no seed is provided, the default seed for the random module is used

        :param seed: seed for random function
        :return: result
        """

        if seed:
            random.seed(seed)
        else:
            random.seed()

        result = self._grammar.evaluate()
        name = []

        for terminal in result:
            name.append(self._eval_terminal(terminal))

        return name

    @abstractmethod
    def _eval_terminal(self, terminal: str) -> str:
        """
        Evaluate a terminal node of the Grammar

        :param terminal: terminal to evaluate
        :return: value of terminal
        """
        pass
