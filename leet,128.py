class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        net_set=set(nums)
        max_len=0
        for x in net_set:
            if (x-1) not in net_set:
                num=x
                num_len=1
                while (num+1) in net_set:
                    num+=1
                    num_len+=1
                if  num_len>max_len:
                    max_len=num_len
        return max_len
if __name__=="__main__":
    nums=[100,4,200,1,3,2]
    print(Solution().longestConsecutive(nums))