import string

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        lowercase_list= list(string.ascii_lowercase)
        morse_code_list= [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        morse_code_dict= {}
        result_set= set()

        for s, m in zip(lowercase_list, morse_code_list):
            morse_code_dict[s]=m

        for word in words:
            tmp_string= ''
            for w in word:
                tmp_string+= morse_code_dict[w]

            result_set.add(tmp_string)

        return len(result_set)
