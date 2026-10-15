
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=[0]*128
        window=[0]*128
        for c in t:
            need[ord(c)]+=1
        left=0
        res=[]
        valid=0
        start=0
        min_len=float('inf')
        need_kind=0
        for i in range(128):
            if need[i]>0:
                need_kind+=1
        for right ,c in enumerate(s):
            idx=ord(c)
            window[idx] += 1
            if window[idx]==need[idx]:
                valid+=1
            while valid==need_kind:
                cur_len=right-left+1
                if cur_len <min_len:
                    min_len=cur_len
                    start=left
                d=s[left]
                d_idx=ord(d)
                if window[d_idx]==need[d_idx]:
                    valid-=1
                window[d_idx]-=1
                left+=1
        if min_len==float('inf'):
            return ''
        return s[start:start+min_len]
if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    solution = Solution()
    result = solution.minWindow(s, t)
    print(result)  # Output: "BANC"

