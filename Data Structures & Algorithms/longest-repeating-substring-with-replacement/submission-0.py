class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l, r = 0, 0
        longest_substring = 0
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            frequency = sorted(freq.items(), key = lambda x: x[1], reverse=True)
            max_freq = frequency[0][1]

            window_len = len(s[l:r+1])
            num_changes = window_len - max_freq

            if num_changes <= k:
                longest_substring = max(window_len, longest_substring)

            elif num_changes > k:
                freq[s[l]] -=1
                l += 1

        return longest_substring


