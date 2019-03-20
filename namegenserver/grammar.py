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
        return self.__eval_recur(self.__start)

    def __eval_recur(self, key: str) -> list:

        options = self.__rules[key]
        option = random.choice(options)

        return_val = []
        for value in option:

            if value in self.__rules:
                return_val += self.__eval_recur(value)
            else:
                return_val.append(value)

        return return_val
