class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_dict = {}

        sublist = []

        for i, string in enumerate(strs):
            string_sorted = tuple(sorted(string))

            if string_sorted in string_dict:
                string_dict[string_sorted].append(string)
            elif string_sorted not in string_dict:
                string_dict[string_sorted] = [string]
        
        return string_dict.values()

