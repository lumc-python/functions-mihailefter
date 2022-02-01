# Exercise 2. Function updates
#
# Write a python function that transforms all the positive numbers from a list
# and returns back `True` if it performed any action on the list and `False`
# otherwise.


def reverse_positives(numbers):
    """
    Assuming as input a non-empty list of numerical values, this
    function converts all the positives ones into negative ones and
    returns True if any action was performed and False otherwise.
    """
    action_was_performed = False
    for i in range(0, len(numbers)):
        if numbers[i] > 0:
            numbers[i] *= -1
            action_was_performed = True
    return action_was_performed


numbers = [-1, 2, 3, -4.5]
print(reverse_positives(numbers))  # This prints True
print(numbers)

numbers = [-1, -2, -3, -4.5]
print(reverse_positives(numbers))  # This prints False
print(numbers)
