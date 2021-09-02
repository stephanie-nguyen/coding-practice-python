'''
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.
'''

import pdb
def secondHighest(s):
  first = second = -1
  #pdb.set_trace()
  for i in s:
    if i.isdigit():
      j=int(i)
      if j > first:
        first ,second = j, first
      elif first > j > second:
        second = j
  return second


s = "dfa12321a4fd"
print(secondHighest(s))
