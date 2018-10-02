import unittest
#Function to check if a string2 is permutation of string1

#approach 1
def check_string_permutation(string1,string2):
    if len(string1) != len(string2):
        return False
    for c in string1:
        if string1.count(c) != string2.count(c):
            return False
    
    return True

#approach2    
def check_string_permutation2(string1,string2):
    if len(string1) != len(string2):
        return False
    list1 = sorted(string1)
    list2 = sorted(string2)
    if list1 != list2:
        return False
    return True


 

class Test(unittest.TestCase):
  def test_check_string_permutation(self):
    self.assertTrue(check_string_permutation('ABC','CBA'))
    self.assertTrue(check_string_permutation('BBAAC','CABAB'))
    self.assertFalse(check_string_permutation('ABC','AB'))
    self.assertFalse(check_string_permutation('ABC','A  BC'))

  def test_check_string_permutation2(self):
    self.assertTrue(check_string_permutation2('ABC','CBA'))
    self.assertTrue(check_string_permutation2('BBAAC','CABAB'))
    self.assertFalse(check_string_permutation2('ABC','AB'))
    self.assertFalse(check_string_permutation2('ABC','A  BC'))


if __name__ == "__main__":
    unittest.main()
    
    
    
