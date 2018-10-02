# Function to check if a tring is permutaion of a palindrome

import unittest
from collections import defaultdict

def check_permutation_palindrome(inputstr):
  d = defaultdict(int)
  for c in inputstr:
    d[c] += 1
  
  s =  sum(v%2 != 0 for v in d.values())
  return s <= 1

#Tests#

dataT = ('CIVIC','OONN')
dataF = ('NOOefN','CIVIIICCCC')

class Test(unittest.TestCase):
  def test(self):
    # test with inputs that are perm of palindrome
    for input in dataT:
      self.assertTrue(check_permutation_palindrome(input))
    # test with inputs that are not perm of palindrome
    for input in dataF:
      self.assertFalse(check_permutation_palindrome(input))

if __name__ == "__main__":
    unittest.main()  

  












