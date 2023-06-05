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

