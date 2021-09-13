'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''


import pdb
class Solution(object):
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        #pdb.set_trace()
        additional = mapping[digits[-1]]
        return [s + c for s in prev for c in additional]

a = Solution()
print(a.letterCombinations('213'))


'''
class Solution(object):
   def letterCombinations(self, digits):
      if len(digits) == 0:
         return []
      characters = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
      result = []
      self.solve(digits,characters,result)
      return result
   def solve(self, digits, characters, result, current_string="",current_level = 0):
      if current_level == len(digits):
         result.append(current_string)
         return
      for i in characters[int(digits[current_level])]:
         self.solve(digits,characters,result,current_string+i,current_level+1)
a = Solution()
print(a.letterCombinations("379"))
'''