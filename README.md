# 1. Multiplication

Write a Python function to multiply all the positive numbers in a list.
The function should return that result.

# 2. Function updates

Write a python function that transforms all the positive numbers from a list
and returns back `True` if it performed any action on the list and `False`
otherwise.

# 3. Palindrome

Write a function that returns `True` if its argument is a palindrome and
`False` otherwise. A palindrome is a word, number, phrase, or other sequence
of characters which reads the same way backward as forward (e.g., `madam`,
`Able was I ere I saw Elba`, `10101`, `90.09`).

# 4. k-mer counting

Remember Exercise 3 (Analyse a repeat structure) from yesterday's assignment?

    We are going to make a repeating DNA sequence and extract some subsequences
    from it.
    - Make a short tandem repeat that consists of three "ACGT" units and five
      "TTATT" units.
    - Print all suffixes of the repeat structure.
      - **Note**: A suffix is an ending. For example, the word "spam" has five
      suffixes: "spam", "pam", "am", "m" and "".
    - Print all substrings of length 3.
    - Print all unique substrings of length 3.

    **Hint**: All elements in a set are unique.

## (1/2)

Perform the following:
- Make a function from your implementation.
- Have `k` as an argument to the function.
- Test the function on several input strings.

## (2/2)

Modify your function to use a dictionary with substring counts.
- Use the substrings as dictionary keys.
- Use the counts as dictionary values.
- Have the function return the dictionary.
- Add a docstring to the function.
- Use the function to print k-mer counts for some strings.

# 5. GC calculator

Write a function that returns the total percentage of `G` and `C` from a DNA
string (which presumably contains only `A`, `C`, `G`, and `T`). For example,
if the string is `CCGT` the function should return `75.0`.
- Try running the function with `ACTG123` as argument. What happens? Is this
  acceptable behavior? Raise a `ValueError` whenever an unsupported character
  is encountered in the input string.
- Try running the function with the empty string as argument. What happens? Is
  this acceptable behavior? Write code to cope with this situation, i.e.,
  return `0.0`.
- Add a docstring to the function.
