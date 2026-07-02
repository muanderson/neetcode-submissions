class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groupings = {}

        for i, value in enumerate(nums):
            if value in groupings:
                groupings[value] +=1
            else:
                groupings[value] = 1
        
        sorted_items = sorted(groupings.items(), key=lambda x: (-x[1], x[0]))
        # Extract only the keys from the sorted items
        return [key for key, _ in sorted_items[:k]]
