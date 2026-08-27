class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:            
        # attempt 2:
        # use the word with least number of characters, compare each letter of that word with all the other words
            # if all words, have that letter, add it to a string.
            # stop when at least one word don't have a matching letter.
            
            # find word with minimum length: 
            min_letter_word = min(strs, key=len)
            prefix = ""

            for i in range(len(min_letter_word)): #loop through all letters of the first word
                for j in range(1, len(strs)): # loop through all the other words
                    if min_letter_word[i] != strs[j][i]: # check if the ith letter of the first word is not equal to the ith letter of word number j.
                        return prefix
                
                prefix += min_letter_word[i]

            return prefix
