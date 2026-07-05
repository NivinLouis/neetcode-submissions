class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freqrep = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in freqrep:
                return [freqrep[diff],i]
            freqrep[nums[i]] = i
        