class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        keys = set(nums)
        counts = {key:0 for key in keys}

        for num in nums:
            counts[num] += 1

        return max(counts, key=counts.get)
