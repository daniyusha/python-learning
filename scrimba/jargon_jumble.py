# Challenge: Scramble a Word
# 1. Create a game file named `jargon_jumble.py`
# 2. Create a list of at least 3 words and save to a variable called `words`
# 3. Use random.choice() to pick a word from the list
# 4. Use list(), random.shuffle(), and "".join() to scramble the word
# 5. Print the scrambled word

import random 
words = ["learning", "mindset" , "attitude"]
chosen = random.choice(words)
chosen_letters = list(chosen)
random.shuffle(chosen_letters)
scrambled_word = "".join(chosen_letters)
print(f"Scrambled word is {scrambled_word}")

# You can't say shuffled = random.shuffle(chosen_letters),
#  random.shuffle() should be done separately in one line 

  # random.shuffle() changes the list in place and returns None,
  # so shuffled = random.shuffle(...) gives None because it just changes the original list


# "".join() is a string method: the separator is a string,
#  and it glues the items into one new string.


# sorted() returns a NEW list of letters in alphabetical order, or list of numbers in its order
# list can be used with Strings and others, the thing is it should be iterable

# An iterable is anything you can loop over with for, one item at a time.

# ✅ list [1, 2], string "hi", tuple (1, 2), dict, range(5)
# ❌ int 5, float 3.14, None

# Claude about sorted(): 1. It works on any iterable, not just letters. sorted() always returns a new list of the items in order:

# python
# sorted("mindset")      # ['d', 'e', 'i', 'm', 'n', 's', 't']
# sorted([3, 1, 2])      # [1, 2, 3]
# sorted(("b", "a"))     # ['a', 'b']  ← tuple in, list out

# 2. The order is by ASCII code, not true alphabetical order. 
# Uppercase letters come before lowercase (Lecture 3: ‘A’–‘Z’ = 65–90, ‘a’–‘z’ = 97–122):

# python
# sorted("baA")    # ['A', 'a', 'b']
# sorted("Zoo")    # ['Z', 'o', 'o']