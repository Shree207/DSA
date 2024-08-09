class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x==0:
            return True
        else:
            k=x
            rev=0
            while(x>0):
                d=int(x)%10
                rev=rev*10+d
                x=int(x/10)
            if rev==k:
                return True
            else:
                return False