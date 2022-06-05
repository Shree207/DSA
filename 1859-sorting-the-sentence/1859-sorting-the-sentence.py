class Solution:
    def sortSentence(self, s: str) -> str:
        l=s.split()
        s=""
        output={}
        for word in l:
            output[word[-1]]=word[0:-1]
        for index,word in sorted(output.items()):
            s=s+word+" "
        return s.strip()
        