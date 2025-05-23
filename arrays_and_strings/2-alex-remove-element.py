class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n_removed = 0

        for i in range(len(nums)):
            if nums[i] == val:
                n_removed += 1
            else:
                nums[i - n_removed] = nums[i]

        return len(nums) - n_removed
