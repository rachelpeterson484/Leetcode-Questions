class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ins = 0
        start = 0
        last = -10001

        for i in range(len(nums)):
            curr = nums[i]

            if curr != last:
                start = ins
                last = curr
                nums[ins] = curr
                ins += 1

            elif ins - start < 2:
                nums[ins] = curr
                ins += 1
                continue

        return ins

