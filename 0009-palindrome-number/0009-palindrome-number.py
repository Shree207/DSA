class Solution:
    def isPalindrome(self, x: int) -> bool:
        k=x
        rev=0
        if x < 0:
            return(False)
        elif x==0:
            return(True)
        else:
            while(x>0):
                d=int(x)%10
                rev = rev*10+d
                x=int(x/10)
            if k==rev:
                return(True)
            else:
                return(False)
        