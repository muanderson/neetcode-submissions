class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i, value in enumerate(strs):
            string_sorted = tuple(sorted(value))

            if string_sorted in hashmap:
                hashmap[string_sorted].append(value)

            elif string_sorted not in hashmap:
                hashmap[string_sorted] = [value]

        return hashmap.values()

