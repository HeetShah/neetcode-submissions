class Solution:

    def encode(self, strs: List[str]) -> str:

        all_encoded_strs = ''
        
        for word in strs:
            encoded_str = str(len(word)) + "#" + word
            # print('encoded_str: ', encoded_str)
            all_encoded_strs += encoded_str
        
        # print('all_encoded_strs: ', all_encoded_strs)
        return all_encoded_strs
        
    def decode(self, s: str) -> List[str]:

        result = []

        i = 0
        while len(s) != 0:
            # get all numbers upuntil the first #
            # print('current s: ', s)
            number_end = s.find('#')

            # print('number_end: ', number_end)

            # get the length of the word
            word_len = s[i:number_end]
            # print(word_len)

            start = number_end + 1
            end = start + int(word_len)
            # print(start, end)
            word = s[start:end]
            # print(word)

            result.append(word)
            # print(result)

            s = s[end:]

        
        return result