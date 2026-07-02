class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_cleaned = []

        for i, value in enumerate(s):
            if value.isalnum():
                string_cleaned.append(value.lower())

        string_cleaned = ''.join(string_cleaned)

        return string_cleaned == string_cleaned[::-1]