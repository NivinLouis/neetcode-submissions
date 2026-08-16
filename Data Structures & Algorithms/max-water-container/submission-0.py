class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        maxarea = 0

        while i<j:
            minheight = min(heights[i],heights[j])
            area = (j-i) * minheight

            maxarea = max(maxarea,area)

            if minheight==heights[i]:
                i+=1
            else:
                j-=1
        
        return maxarea
            