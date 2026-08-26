class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # One pass hash map approach
        # iterate through the array and store the value and index of each passing value in a dictionary
        # in each iteration, check if complement = target - current value exists in the dictionary.
        # if it exists, create a list with the complement's index and the current index.
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            else:
                seen[num] = i

# time complexity = O(n)
# space complexity = O(n)