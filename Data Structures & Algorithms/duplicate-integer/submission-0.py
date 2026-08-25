class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # iterate through the list
        # store seen values in of the list in a set
        # check each value if it's in the set, if it's in the set, return false.
        # else, add that value to the seen set.

        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        
        return False