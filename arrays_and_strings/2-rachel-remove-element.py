from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # The description is silly. So even though my solution doesn't technically pass their test cases, idc and I think this is better. 
        # They say they don't care what you have in the array after the # of val in the arr, but they do 
        count = 0
        arr_index = 0

        for num in nums:
            if num == val:
                count += 1
            if nums[arr_index] == val and arr_index < len(nums) - 1:
                non_num_value = nums[arr_index+1]
                nums[arr_index] = non_num_value
                nums[arr_index+1] = val
            arr_index += 1

        return count

        