#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        # code here
        k=int(n)
        c=0
        while n>0:
            dig=int(n%10)
            if dig!=0:
                if k%dig==0:
                    c=c+1
            n=int(n/10)
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.evenlyDivides(N))
        print("~")

# } Driver Code Ends