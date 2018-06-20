class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        array_sum = sum(nums)
        if sum(nums) % 2 != 0:
            return False

        array_sum = int(array_sum / 2)
        array_length = len(nums)

        dp = [False] * (array_sum + 1)
        dp[0] = True

        for num in nums:
            for i in reversed(range(array_sum + 1)):
                if i >= num:
                    dp[i] = dp[i] or dp[i - num]

        return dp[array_sum]