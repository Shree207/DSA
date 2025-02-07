#User function Template for python3
import math
class Solution:
    def armstrongNumber (self, n):
        # code here 
        dup = n
        arm = 0
        num = int (math.log(n,10) + 1)
        while n>0:
            dig = int(n%10)
            arm = arm + int(dig**num)
            n = int(n/10)
        #print(arm)
        if arm == dup:
            return True
        else:
            return False


#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        flag = ob.armstrongNumber(n)
        if flag:
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends