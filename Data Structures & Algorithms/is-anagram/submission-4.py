class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      # sort both s and t using sorted()
      # sorted(s) = ['a', 'a', 'c', 'c', 'e', 'r', 'r']
      # then check if they match

      if len(s) != len(t):
        return False

      sorted_s = sorted(s)
      sorted_t = sorted(t)

      return sorted_s == sorted_t

      # Time complexity: O(n log n + m log m) where n is len(s) and m is len(t)