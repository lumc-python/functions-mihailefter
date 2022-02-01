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
    at_count, gc_count = 0, 0
    for char in seq:
        if char in ('A', 'T'):
            at_count += 1
        elif char in ('G', 'C'):
            gc_count += 1

    return gc_count * 100.0 / (gc_count + at_count)


print("The sequence 'CAGG' has a %GC of {:.2f}".format(
          calc_gc_percent("CAGG")))
