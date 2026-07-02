class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, value in enumerate(numbers):
            complement = target - value

            if complement in hashmap and hashmap[complement] != i:
                return [hashmap[complement]+1,i+1]
            hashmap[value] = i

        return []
