class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        track = {}

        for i,value in enumerate(nums):
            complement = target - value
            if complement in track:
                return [track[complement], i]
            else:
                track[value] = i
        return None
