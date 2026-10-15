class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow=0
        for fast in range(len(nums)):
                if nums[fast]!=0:
                    nums[slow],nums[fast]=nums[fast],nums[slow]
                    slow+=1
if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)  # Output: [1, 3, 12, 0, 0]