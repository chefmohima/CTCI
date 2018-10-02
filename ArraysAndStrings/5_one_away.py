#Function to check if string1 differs from string2 by one character
#If deleting/replacing/inserting ANY 1 character makes the 2 strings equal then
#return True else return False

import unittest

def check_one_away(string1,string2):
  if abs(len(string1) - len(string2)) > 1:
    return False
  countdiff = 0
  for i in range(min(len(string1),len(string2))):
      if string1[i] != string2[i]:
        countdiff += 1
      if countdiff > 1:
        return False
  return True

 

class Test(unittest.TestCase):
  def test(self):
    self.assertTrue(check_one_away('abc','abcd'))
    self.assertTrue(check_one_away('abc','ab'))
    self.assertTrue(check_one_away('abc','abp'))
    self.assertFalse(check_one_away('abcde','abc'))
    self.assertFalse(check_one_away('abc','abcde'))


if __name__ == "__main__":
    unittest.main()

 

#print(check_one_away('abcb','abcb'))


  




