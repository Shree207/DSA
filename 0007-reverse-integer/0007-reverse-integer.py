class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign=-1
            x=x*(-1)
        elif x==0:
            return 0
        else:
            sign=1
        rev=0
        while(x>0):
            d=int(x)%10
            #print(d,' ',x,' ',rev)
            rev=rev*10+d
            if rev<-2**31 or rev > (2**31)-1:
                return 0
            x=int(x/10)
        rev=rev*sign
        return rev