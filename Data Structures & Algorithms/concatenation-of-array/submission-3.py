class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #approach: ans is the result of appending nums 2 times.
        ans = []
        for i in range(2):
            for num in range(len(nums)):
                ans.append(nums[num])
        
        return ans
        