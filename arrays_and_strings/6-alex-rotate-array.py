class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotated = [0 for _ in range(len(nums))]

        for i, num in enumerate(nums):
            rotated[(i+k) % len(nums)] = nums[i]

        for i, num in enumerate(rotated):
            nums[i] = num
