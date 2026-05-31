# https://datadriven.io/problems/the_window_cleaner

from collections import Counter

def longest_unique_substr(s):
    if not s:
       return 0
    
    counter = set()
    left = 0
    max_length = 0
    for c in s:
        print(counter)
        if c not in counter:
            counter.add(c)
        else:
            while c in counter:
                counter.remove(s[left])
                left += 1
            counter.add(c)
        max_length = max(max_length, len(counter))
    return max_length


inputs = [
  ("abcabcbb", 3)
]
for s, result in inputs:
    my_result = longest_unique_substr(s)
    print(my_result, my_result == result)
