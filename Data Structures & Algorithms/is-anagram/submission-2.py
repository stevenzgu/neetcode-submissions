class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use a dictionary to keep count of the number of characters of each string.
        # if the character frequency count of both strings are the same, return True.

        # count the char frequency of s and t
        freq_s = {}
        freq_t = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            freq_s[s[i]] = freq_s.get(s[i], 0) + 1
            freq_t[t[i]] = freq_t.get(t[i], 0) + 1

        return freq_s == freq_t

# Time complexity: O(n + m)
# Space complexity: O(1)
        