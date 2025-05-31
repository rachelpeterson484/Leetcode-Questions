class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_slot = 0
        current_number = -101

        for i in range(len(nums)):
            if current_number != nums[i]:
                nums[next_slot] = nums[i]
                current_number = nums[i]
                next_slot += 1
        
        return next_slot


