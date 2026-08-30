class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a dictionary to keep track of the frequency of each number
        # create a array of lists of size n+1, use the array index as the frequency count and append the number into the list with the corresponding frequency
        # Loop and traverse through the list backwards, starting from the highest frequency to populate the result list
        # result = []
        # if an index in the array of lists is not empty, result += array[i]
        # if len(result) >= k:
            #return result

        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])
        # bucket = [[] for i in range(len(nums) + 1)]
        
        for freq_key, freq_value in freq.items():
            bucket[freq_value].append(freq_key)

        result = []
        for i in range(len(nums), 0, -1):
            if len(result) >= k:
                return result
            elif bucket[i]:
                result += bucket[i]

        return result

        # time complexity: O(n) where n is the number of elements in nums
        # space complexity: O(n)
