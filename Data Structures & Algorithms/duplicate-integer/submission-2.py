class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # sort the array
        # check if the adjacent value are equal
        # if equal, return True
        # if loop reaches the end, return False

        nums.sort()
        
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
            
        return False