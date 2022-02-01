# Exercise 5. GC calculator
#
# Write a function that returns the total percentage of `G` and `C` from a DNA
# string (which presumably contains only `A`, `C`, `G`, and `T`). For example,
# if the string is `CCGT` the function should return `75.0`.
# - Try running the function with `ACTG123` as argument. What happens? Is this
#   acceptable behavior? Raise a `ValueError` whenever an unsupported character
#   is encountered in the input string.
# - Try running the function with the empty string as argument. What happens? Is
#   this acceptable behavior? Write code to cope with this situation, i.e.,
#   return `0.0`.
# - Add a docstring to the function.


def calc_gc_percent(seq):
    """
    Calculates the GC percentage of the given sequence.
    Arguments:
        - seq - the input sequence (string).
    Returns:
        - GC percentage (float).
    """
    at_count, gc_count = 0, 0
    # change input to all caps to allow for non-capital
    # input sequence.
    for char in seq.upper():
        if char in ('A', 'T'):
            at_count += 1
        elif char in ('G', 'C'):
            gc_count += 1
        else:
            raise ValueError("Unexpected character found: {}. Only "
                             "ACTGs are allowed.".format(char))

    # Corner case handling: empty input sequence.
    try:
        return gc_count * 100.0 / (gc_count + at_count)
    except ZeroDivisionError:
        return 0.0


print("The sequence 'CAGG' has a %GC of {:.2f}".format(
          calc_gc_percent("CAGG")))
