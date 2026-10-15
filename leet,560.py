from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt=defaultdict(int)
        cnt[0]=1
        res=0
        prem_sum=0
        for num in nums:
            prem_sum+=num
            res+=cnt[prem_sum-k]
            cnt[prem_sum]+=1
        return res
if __name__ == "__main__":
    nums = [1, 2, 3]
    k = 3
    solution = Solution()
    result = solution.subarraySum(nums, k)
    print(result)  # Output: 2