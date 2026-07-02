class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}

        for i,value in enumerate(nums):
            if value in frequency_map:
                frequency_map[value] +=1
            else:
                frequency_map[value] = 1

        output = [k for k,v in sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)]

        return output[:k]