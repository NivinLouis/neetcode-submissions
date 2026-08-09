class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ppdct = [0] * len(nums)
        result = []
        ppdct[0] = nums[0]
        for i in range(1,len(nums)):
            ppdct[i] = ppdct[i-1]*nums[i]

        spdct = [0] * len(nums)
        spdct[len(nums)-1]= nums[-1]
        for i in range(len(nums)-2,-1,-1):
            spdct[i] = spdct[i+1]*nums[i]
        
        for i in range(len(nums)):
            if i == 0:
                res = spdct[i+1]
            elif i == len(nums)-1:
                res = ppdct[i-1]
            else:
                res = ppdct[i-1] * spdct [i+1]
            result.append(res)
        
        return result
