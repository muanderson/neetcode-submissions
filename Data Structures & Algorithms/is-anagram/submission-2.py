class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = {}
        string2 = {}

        for i, letter in enumerate(s):
            string1[letter] = string1.get(letter, 0) + 1

        for i, letter in enumerate(t):
            string2[letter] = string2.get(letter, 0) + 1

        return string1 == string2