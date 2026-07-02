class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)  # Remove duplicates and allow O(1) lookups
        longest = 0
        
        for num in numSet:
            # Only start counting if this is the start of a sequence
            # (i.e., num-1 is not in the set)
            if num - 1 not in numSet:
                current_num = num
                current_streak = 1
                
                # Keep checking for consecutive numbers
                while current_num + 1 in numSet:
                    current_num += 1
                    current_streak += 1
                
                longest = max(longest, current_streak)
        
        return longest


