"""
26. Remove Duplicates from Sorted Array
Given a sorted array nums, remove the duplicates in-place such that each
element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements
of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        write_index = 1
        for i in range(1, len(nums)):
            if nums[write_index-1] != nums[i]:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index