class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count={}
        s=0
        for let in stones:
            if let not in count:
                count[let]=1
            else:
                count[let]+=1
        for let in jewels:
            if let in count:
                s=s+count[let]
        return s