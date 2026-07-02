class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()

        for i,value in enumerate(nums):
            if value in unique:
                return True
            else:
                unique.add(value)

        return False