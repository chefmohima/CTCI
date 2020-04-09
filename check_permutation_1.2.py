# same problem as Leetcode 242. Valid Anagram
# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

#Input: s = "anagram", t = "nagaram"
#Output: true
#Example 2:

#Input: s = "rat", t = "car"
#Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        # if EITHER string is null or if length of strings differ,
        # then clearly they cant be anagrams
        if (not s or not t)  or (len(s) != len(t)):  
            return False
        
       #if the strings are anagrams then character counts should match exactly.
       # break the loop if there is any character that has a different count in the 2 strings
        counter = {}
        for c in s:
            if s.count(c) != t.count(c):
                return False
        return True
        
