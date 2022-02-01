# Exercise 1. Multiplication
#
# Write a Python function to multiply all the positive numbers in a list.
# The function should return that result.


def multiply_positives(numbers):
    """
    Assuming as input a non-empty list of numerical values,
    it returns the multiplication of all the positive ones.
    """
    result = 1
    for number in numbers:
        if number > 0:
            result *= number
    return result


print(multiply_positives([-1, 2, -3, 4, -5]))
