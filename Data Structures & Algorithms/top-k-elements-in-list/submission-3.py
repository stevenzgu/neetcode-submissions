class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        nums = [1,2,2,3,3,3], k = 2

        1. Store the frequency of each number using a dictionary
            {1:1, 2:2, 3:3}
        2. Make an array of lists with each frequency as the index
            [
            0   []
            1   [1]
            2   [2]
            3   [3]
            4   []
            5   []
            6   []
            ]
        3. Store the k most frequent elements in list -> output
        4. Loop: iterate backwards through array buckets
            if a bucket is not empty: 
                output += bucket[i]
        
            if len(output) >= k:
                return output
        """
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for freq_key, freq_value in freq.items():
            bucket[freq_value].append(freq_key)
            
        output = []
        for i in range(len(nums), 0, -1):
            if bucket[i]: 
                output += bucket[i]
            if len(output) >= k:
                return output
        
        return output
