class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        string1 = tuple(sorted(s))
        string2 = tuple(sorted(t))

        if string1 == string2:
            return True

        else:
            return False