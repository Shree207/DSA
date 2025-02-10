#User function Template for python3
 

class Solution:
    def sumOfDivisors(self, n):
    	#code here 
    	i=1
    	summ=0
    	while (i<=n):
    	    j=1
    	    while (j*j<=i):
    	        if i%j==0:
    	            summ=summ+j
    	            if (i/j)!=j:
    	                summ=summ+(i/j)
    	        j=j+1
    	    i=i+1
    	return (int(summ)) 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
        print("~")

# } Driver Code Ends