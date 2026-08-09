class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        longest = 0
        for i in nums:
            hashset.add(i)
        
        for i in hashset:
            if i-1 not in hashset:
                length = 0
                while i+length in hashset:
                    length += 1
                longest = max(length,longest)
        return longest