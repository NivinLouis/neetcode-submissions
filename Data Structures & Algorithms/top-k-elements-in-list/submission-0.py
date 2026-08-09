class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        buckets = [[] for i in range(len(nums)+1)]
        result = []
        for i in nums:
            hashmap[i]= hashmap.get(i, 0) + 1
        
        for m,n in hashmap.items():
            buckets[n].append(m)
        
        for i in range(len(nums),0,-1):
            for j in buckets[i]:
                result.append(j)
                if len(result)==k:
                    return result
        return result
