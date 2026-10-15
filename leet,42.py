class Solution:
    def trap(self, height: list[int]) -> int:
        n=len(height)
        ans=0
        left=0
        right=n-1
        pre_max=0
        suf_max=0
        while left<=right:
           pre_max=max(pre_max,height[left])
           suf_max=max(suf_max,height[right])
           if pre_max<suf_max:
            ans+=pre_max-height[left]
            left+=1
           else:
            ans+=suf_max-height[right]
            right-=1
        return ans
if __name__=="__main__":
    height=[0,1,0,2,1,0,1,3,2,1,2,1]
    s=Solution()
    print(s.trap(height))