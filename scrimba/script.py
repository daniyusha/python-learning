# To open emoji picker you can press on #   Mac: Control+Command+Space

# print(playlist[-1]) - would give you the last item in the list
# print(playlist[-2]) - would give you the second to last item on the list 
# IndexError: index out of range - if there is no value under that index 

# Challenge: Four Joiners

# 1. Join ["mysite.com", "products", "sale"] with "/" to build a URL path
# 2. Join ["2026", "05", "29"] with "-" to format a date
# 3. Join ["hip", "hip", "hooray"] with " " for the crowd
# 4. Join `letters` into a single word with no separator.

letters = ["p", "y", "t", "h", "o", "n"]

url_path = "/".join(["mysite.com", "products", "sale"])
date = "-".join(["2026", "05", "29"])
crowd = " ".join(["hip", "hip", "hooray"])
word = "".join(letters)

