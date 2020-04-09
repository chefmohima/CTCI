class Solution:
    def urlify(self, s):
        
        #wordlist = s.split()
        #result = "%20".join(wordlist)
        #return result
        charlist = list(s)
        
        resultlist = []
        i = 1
        while i in range(1, len(charlist)):
            while charlist[i] == ' ' and charlist[i] == charlist[i-1] and i < len(charlist)-1:
                i += 1
            resultlist.append(charlist[i-1])
            i += 1
            
        return ''.join(resultlist)
            
        
    
            
s  =Solution()
s.urlify("Mr Jon Snow     ")
