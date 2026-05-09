class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)   # O(n)
        longest = 0

        for num in num_set:
            # Check if this is the start of a sequence
            if num - 1 not in num_set:
                length = 1

                # Count consecutive numbers
                while num + length in num_set:
                    length += 1

                longest = max(longest, length)

        return longest