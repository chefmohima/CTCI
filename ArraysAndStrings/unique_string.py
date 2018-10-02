
# Function to check if characters are unique in string##
import unittest

def check_unique(s):
# O(N*N) solution 
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                return False
    return True
    

def check_unique2(s):
#O(N) solution
    seen = []
    for c in s:
        if c not in seen:
            seen.append(c)
        else:
            return False
    return True

dataT = ['tRUE','123',' BLANK']
dataF = ['1233','  2BLANK']
class Test(unittest.TestCase):
  def test_check_unique(self):
    for input in dataT:
      self.assertTrue(check_unique(input))
    for input in dataF:
      self.assertFalse(check_unique(input))

  def test_check_unique2(self):
    for input in dataT:
      self.assertTrue(check_unique2(input))
    for input in dataF:
      self.assertFalse(check_unique2(input))



if __name__ == "__main__":
    unittest.main()

  



