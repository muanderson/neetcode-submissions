class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, value in enumerate(nums):
            complement = target - value

            if complement in num_dict:
                return [num_dict[complement],i]
            num_dict[value] = i
            
        return []
        