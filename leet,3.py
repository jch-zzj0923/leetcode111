from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        cnt=Counter()
        left=0
        for right,char in enumerate(s):
            cnt[char]+=1
            while cnt[char]>1:
                cnt[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
if __name__=="__main__":
    s=Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))