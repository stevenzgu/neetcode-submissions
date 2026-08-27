class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sorting-based reasoning
        # ["bat","bag","bank","band"]
        # bag, band, bank, bat

        # compare first word with second word
            # compare letters of each word, stop when the letters don't match anymore. concatenate put those letters into a string.
            # return that string
        # strs.sort()
        # first_word = strs[0]
        # second_word = strs[1]
        # prefix = ""

        # for i in range(len(first_word)):
        #     if first_word[i] == second_word[i]:
        #         prefix += first_word[i]
        #     else:
        #         return prefix
            
            # failed test case: strs=["interview","internet","internal","interval"]
            
        # attempt 2:
        # use the first word, compare each letter of the first word with all the other words
            # if all words, have that letter, add it to a string.
            # stop when at least one word don't have a matching letter.
            strs.sort()
            first_word = strs[0]
            prefix = ""

            for i in range(len(first_word)): #loop through all letters of the first word
                for j in range(1, len(strs)): # loop through all the other words
                    if first_word[i] != strs[j][i]: # check if the ith letter of the first word is not equal to the ith letter of word number j.
                        return prefix
                
                prefix += first_word[i]

            return prefix





        
        # go into the first word, check if every other word have the same first letter, second letter, etc.
            # if a letter matches in all other words, add it to a list.
            # stop when the letter don't match for at least one word.
