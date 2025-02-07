class Solution:
    def isPalindrome(self, x: int) -> bool:
        dup = x
        if x < 0:
            return False
        rev = 0
        while x>0:
            dig = int(x%10)
            rev = int (rev * 10) + dig
            x =int (x/10)
        # print(rev)
        if (dup==rev):
            return True
        else:
            return False
