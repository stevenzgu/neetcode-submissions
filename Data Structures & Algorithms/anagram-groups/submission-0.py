class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # convert each string into a dictionary to keep track of the frequency of each letter (as a Signature).
        # create another dictionary with each signature as the key, and each key stores the strings of matching frequency as a list.
        # using a for loop and iterate through the dictionary, to create a list of all the dictionary values.

        # example
        # dictionary = {'a': 1, 'c': 1, 't': 1} 
        # signature = tuple(sorted(dictionary.items))
        # groups = {}
        # groups[signature] = group.get(, 0)
        # for group in groups:

        groups = {}
        result =[]
        
        for word in strs:
            freq = {}

            for letter in word: 
                if letter not in freq:
                    freq[letter] = 0

                freq[letter] += 1 
                # {'a': 1, 'c': 1, 't': 1}
            
            
            signature = tuple(sorted(freq.items()))
            if signature not in groups:
                groups[signature] = []
            
            groups[signature].append(word)
        
        for value in groups.values():
            result.append(value)
        
        return result

