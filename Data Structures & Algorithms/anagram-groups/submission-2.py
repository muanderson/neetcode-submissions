class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringgroups = {}

        for i, value in enumerate(strs):
            sortedstring = tuple(sorted(value))

            if sortedstring in stringgroups:
                stringgroups[sortedstring].append(value)
            else:
                stringgroups[sortedstring] = [value]
        
        return list(stringgroups.values())
