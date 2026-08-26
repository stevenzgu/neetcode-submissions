class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      # sort both s and t using sorted()
      # then check if they match

      sorted_s = sorted(s)
      sorted_t = sorted(t)

      return sorted_s == sorted_t