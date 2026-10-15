class Solution:
    def maxArea(self, height: list[int]) -> int:
        lelf=0
        right=len(height)-1
        max_area=0
        while lelf<right:
            width=right-lelf
            h=min(height[right],height[lelf])
            current_area=h*width
            if current_area>max_area:
                max_area=current_area
            if height[lelf]<height[right]:
                lelf+=1
            else:
                right-=1
        return max_area
if __name__=="__main__":
    solution=Solution()
    height=[1,8,6,2,5,4,8,3,7]
    print(solution.maxArea(height))