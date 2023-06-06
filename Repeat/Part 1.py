# Task 2
def same_parity(list_1):
    return list(filter(lambda item: True if (item % 2) == list_1[0] % 2 else False, list_1))


# Task 3
def is_valid(string):
    length = [4, 5, 6]
    if len(string) in length:
        if string.isdigit():
            if ' ' not in string:
                return True
    return False


# Task 4
def print_given(*args, **kwargs):
    for i in args:
        print(i, type(i))

    for key, value in sorted(kwargs.items()):
        print(key, value, type(value))


# Task 5
def convert(string):
    lower, upper = 0, 0
    for letter in string:
        if letter.isalpha():
            if letter.islower():
                lower += 1
            else:
                upper += 1

    if lower >= upper:
        return string.lower()
    elif lower < upper:
        return string.upper()


# Task 6
def filter_anagrams(word, words):
    return [i for i in words if sorted(i) == sorted(word)]


# Task 7
def likes(names):
    if len(names) == 0:
        return 'Никто не оценил данную запись'
    elif len(names) == 1:
        return f'{names[0]} оценил(а) данную запись'
    elif len(names) == 2:
        return f'{names[0]} и {names[1]} оценили данную запись'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
    else:
        return f'{names[0]}, {names[1]} и {len(names[2:])} других оценили данную запись'


# Task 8
def index_of_nearest(numbers, number):
    if len(numbers) < 1:
        return -1
    else:
        list_1 = [abs(i - number) for i in numbers]
        return list_1.index(min(list_1))


# Task 9
def spell(*args):
    my_dict = {}
    for word in args:
        word = word.lower()
        if word[0] not in my_dict:
            my_dict[word[0]] = my_dict.get(word[0], len(word))
        else:
            if len(word) > my_dict[word[0]]:
                my_dict[word[0]] = len(word)
    return my_dict


# Task 10
def choose_plural(amount, declensions):
    second_choice = (2, 3, 4)
    third_choice = (0, 5, 6, 7, 8, 9, 11, 12, 13, 14)

    if (amount == 1 or amount % 10 == 1) and (amount not in third_choice) and (amount % 100 not in third_choice):
        return f'{amount} {declensions[0]}'
    elif amount % 10 in second_choice and amount not in third_choice and amount % 100 not in third_choice:
        return f'{amount} {declensions[1]}'
    elif amount % 10 in third_choice or amount in third_choice or amount % 100 in third_choice:
        return f'{amount} {declensions[2]}'


# Task 11
def get_biggest(numbers):
    if not numbers:
        return -1
    else:
        # Transform numbers to str
        numbers = list(map(str, numbers))
        # Find the longest str
        max_len = int(max(numbers, key=len))
        # We sort by multiplying the term by the length of the longest element
        numbers = sorted(numbers, key=lambda item: item * max_len, reverse=True)
        return int(''.join(numbers))
