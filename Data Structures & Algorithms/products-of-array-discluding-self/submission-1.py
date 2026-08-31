class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums = [1, 2, 4, 6] 
            [48,24,12,8]

        index 0: nums[0] = 1
            (1) * (2 * 4 * 6) = 48
        index 1: nums[1] = 2
            (1 * 1) * (4 * 6) = 24
        index 2: nums[2] = 4
            (1 * 2) * (6) = 12

                nums =       1  [1,  2, 4, 6] 1
        prefix_product =        [1,  1, 2, 8] 
        postfix_product =       [48, 24, 6, 1]
                                [48, 24, 12,8]
        """
        prefix_products = [0] * len(nums)
        pre_product = 1
        for i in range(len(nums)):
            prefix_products[i] = pre_product #prefix_products = [1, 1, 2, 8 ]
            pre_product *= nums[i]
        
        postfix_products = [0] * len(nums)
        post_product = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix_products[i] = post_product
            post_product *= nums[i]
        
        result = []
        for i in range(len(nums)):
            result.append(prefix_products[i] * postfix_products[i])

        return result

        # Time complexity: O(n) where n is the number of elements in nums
        # space complexity: O(n)
