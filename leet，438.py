from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        m=len(p)
        n=len(s)
        cnt_win=Counter()
        cnt_p=Counter(p)
        for right,char in enumerate(s):
            cnt_win[char]+=1
            if right>=m:
                left_char=s[right-m]
                cnt_win[left_char]-=1
                if cnt_win[left_char]==0:
                    del cnt_win[left_char]
            if cnt_win==cnt_p:
                ans.append(right-m+1)
        return ans
if __name__=="__main__":
    s=Solution()
    print(s.findAnagrams("cbaebabacd","abc"))