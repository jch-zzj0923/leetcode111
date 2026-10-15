from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        res=[]
        for right , val in enumerate(nums):
            while q and nums[q[-1]] <=val:
               q.pop()
            q.append(right)
            while  q[0]<=right-k:
                q.popleft()
            if  right>=k-1:
                res.append(nums[q[0]])
        return res
if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    solution = Solution()
    result = solution.maxSlidingWindow(nums, k)
    print(result)  # Output: [3, 3, 5, 5, 6, 7]