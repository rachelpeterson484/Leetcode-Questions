class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = [0 for _ in range(len(nums))]

        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                ans[i] = float('inf')
                continue
            ans[i] = min(ans[i+1:i+1+nums[i]]) + 1

        return ans[0]
