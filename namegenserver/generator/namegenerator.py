import random

__gender = ['m',
            'f',
            'u']

__givennames_male = ['Bob',
                     'Chuck',
                     'Gregory',
                     'Peter',
                     'Harry']

__givennames_female = ['Susan',
                       'Mary',
                       'Anne',
                       'Rebecca',
                       'Bertha']

__givennames_unisex = ['Alex',
                       'Jordan',
                       'Taylor']

__surnames = ['Smith',
              'Johnson',
              'Williams',
              'Brown',
              'Jones'
              ]


def generate_name(seed: str = ''):
    if seed:
        random.seed(seed)
    else:
        random.seed()

    gender = random.choice(__gender[:2])
    givenname = __get_givenname(gender)
    surname = __get_surname()

    return f'{givenname} {surname}'


def __get_givenname(gender: str) -> str:
    if gender == 'm':
        return random.choice(__givennames_male + __givennames_unisex)
    elif gender == 'f':
        return random.choice(__givennames_female + __givennames_unisex)
    elif gender == 'u':
        return random.choice(__givennames_unisex)
    else:
        raise ValueError(f'{gender} is an invalid gender')


def __get_surname():
    return random.choice(__surnames)
