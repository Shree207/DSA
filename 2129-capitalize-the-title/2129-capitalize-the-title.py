class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l=title.split()
        s=""
        for word in l:
            if len(word) >2:
                word=word[0].upper()+word[1:].lower()
            else:
                word=word.lower()
            s=s+word+" "        
        return s.strip()
                
        