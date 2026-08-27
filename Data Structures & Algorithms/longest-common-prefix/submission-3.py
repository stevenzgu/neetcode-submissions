class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sorting-based reasoning
        # ["bat","bag","bank","band"]
        # bag, band, bank, bat

        # compare first word with last word
            # compare letters of each word, stop when the letters don't match anymore. concatenate put those letters into a string.
            # return that string
        strs.sort()
        first_word = strs[0]
        last_word = strs[-1]
        prefix = ""

        for i in range(len(first_word)):
            if first_word[i] == last_word[i]:
                prefix += first_word[i]
            else:
                return prefix
        
        return prefix
            # failed test case: strs=["interview","internet","internal","interval"]