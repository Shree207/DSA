class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        rev = 0
        if x<0:
            sign = -1
            x = x * -1
        while x>0:
            dig = int (x % 10)
            rev = rev*10 + dig
            x = int (x / 10)

        rev = rev * sign
        if rev > 2**31 -1 or rev < (-2)**31:
            return 0
        return rev
        