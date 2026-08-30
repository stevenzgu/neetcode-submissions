class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["cat", "", "hello#world"]
        # maintain a str variable encoded_str = ""
        # for each word in the list, 
            # get the len()
            # encoded_str += str(len()) + "#" + word
        
        encoded_str = ""

        for word in strs:
            length = str(len(word))
            encoded_str += length + "#" + word

        return encoded_str

    def decode(self, s: str) -> List[str]:
        # "3#cat0#11#hello#world"
        # maintain a list variable decoded_list = []
        # loop: until i >= len(s)
            # i = 0
            # j = 1
            # loop: increment j until j == '#'
            # word_length = int(s[i:j])
            # word = s[j + 1: j + 1 + word_length]
            # decoded_list.append(word)
            # increment i = j + 1 + word_length
        
        decoded_list = []

        i = 0
        while i < len(s):
            j = i + 1

            while j < len(s):
                if s[j] == "#":
                    break
                j += 1
            
            word_length = int(s[i:j])
            word = s[j + 1: j + 1 + word_length]
            decoded_list.append(word)
            i = j + 1 + word_length

        return decoded_list

