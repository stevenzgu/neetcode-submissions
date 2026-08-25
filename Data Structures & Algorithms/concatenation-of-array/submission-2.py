class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        #preallocating an array
        ans = [0] * (2 * n)
        #populate the ans array with values of nums from the start i and starting from half way i + n. 
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        
        return ans

# Time complexity: O(n)
# Space complexity: n, ans, i. ans = O(n) 

        