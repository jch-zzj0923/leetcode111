class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash={}
        for i in strs:
            key="".join(sorted(i))
            if key not in hash:
                hash[key]=[]
            hash[key].append(i)
        return list(hash.values())
if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))