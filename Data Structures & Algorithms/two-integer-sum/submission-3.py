class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two pointer approach
        # convert the array into a 2d array, storing the value and original index
        # sort the array, have one pointer starting from the left and a pointer starting from the right
        # while left < right:

        # if nums[left] + nums[right] = target:
            # return list
        # elif nums[left] + nums[right] > target:
        # decrement right pointer
        # elif nums[left] + nums[right] < target:
        # increment left pointer
        sorted_nums = []

        for i, num in enumerate(nums):
            sorted_nums.append((num, i))

        sorted_nums.sort()
        
        left = 0
        right = len(sorted_nums) - 1
        
        while left < right:
            if sorted_nums[left][0] + sorted_nums[right][0] == target:
                a = sorted_nums[left][1]
                b = sorted_nums[right][1]
                return [min(a, b), max(a, b)]
            elif sorted_nums[left][0] + sorted_nums[right][0] > target:
                right -= 1
            else:
                left += 1

        return []

# Time complexity: O(n) + O(n log n) + O(n) = O(n log n)
# Space complexity: O(n)
