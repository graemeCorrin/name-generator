import random
from typing import Sequence


class ContextFreeGrammar:

    def __init__(self):
        self.__start = None
        self.__rules = {}

    def add_rule(self, key: str, options: Sequence[Sequence[str]], weights: Sequence[float] = None):
        """
        Add a rule to the Context Free Grammar. The left side of the first rule added will be the starting point

        :param key: left side of the Context Free Grammar rule
        :param options: right side of the Context Free Grammar rule
        :param weights: weights for each option
        """

        if key in self.__rules:
            raise ValueError(f'key:{key} already exists within the Grammar')

        try:
            x = options[0][0]
        except:
            raise ValueError('Rules must be of an iterable of iterables')

        if weights and len(weights) != len(options):
            raise ValueError('Sequence of options and Sequence of weights must be the same length')

        if not self.__rules:
            self.__start = key

        if not weights:
            weights = [1 / len(options)] * len(options)

        self.__rules[key] = (tuple(options), tuple(weights))

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

        options = self.__rules[key][0]
        weights = self.__rules[key][1]
        option = random.choices(options, weights=weights, k=1)[0]

        return_val = []
        for value in option:

            if value in self.__rules:
                return_val += self.__eval_recur(value)
            else:
                return_val.append(value)

        return return_val

