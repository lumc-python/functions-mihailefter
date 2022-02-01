# Exercise 3. Palindrome
#
# Write a function that returns `True` if its argument is a palindrome and
# `False` otherwise. A palindrome is a word, number, phrase, or other sequence
# of characters which reads the same way backward as forward (e.g., `madam`,
# `Able was I ere I saw Elba`, `10101`, `90.09`).


def is_palindrome(value):
    """
    Checks whether the input value is a palindrome.
    Accepted types for the value are only str, list, and tuple.
    """
    if value == value[::-1]:
        return True
    else:
        return False


test_values = [
    'madam',
    'madama',
    'able was I ere I saw elba',
    'Able was I here I saw Elba',
    ['a', 'a', 'a'],
    ['a', 'a', 'b'],
    ['a', 1, 'b'],
    ('a', 1, 'a')
]

for test_value in test_values:
    print(test_value, is_palindrome(test_value))

# print(is_palindrome(10101))  # Error
print('10101', is_palindrome(str(10101)))  # True
print('90.09', is_palindrome(str(90.09)))  # True


def is_palindrome_v2(value):
    """
    Checks whether the input value is a palindrome.
    Accepted types for the value are: str, list, tuple, int, and float.
    """
    if isinstance(value, int) or isinstance(value, float):
        value = str(value)
    if value == value[::-1]:
        return True
    else:
        return False


print('10101', is_palindrome_v2(10101))  # True
print('90.09', is_palindrome_v2(90.09))  # True

print(['a', 'a', 'a'], is_palindrome(['a', 'a', 'a']))  # True

print('madam', is_palindrome('madam'))  # True
