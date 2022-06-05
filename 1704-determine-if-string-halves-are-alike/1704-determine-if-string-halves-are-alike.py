class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel=set(['a','e','i','o','u','A','E','I','O','U'])
        count=0
        k=int(len(s)/2)
        for let in s[0:k]:
            if let in vowel:
                count+=1
        for let in s[k:]:
            if let in vowel:
                count-=1
        return count==0
         
                