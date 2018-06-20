class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums or (sum(nums) + S) % 2 != 0:
            return 0
        dp = [{nums[0]: 1}]
        dp[0][-nums[0]] = dp[0].get(-nums[0], 0) + 1
        for i in nums[1:]:
            previous_map = dp[len(dp) - 1]

            new_map = {}

            for possible_sum, sum_possibilities in previous_map.items():
                new_map[possible_sum + i] = new_map.get(possible_sum + i, 0) + sum_possibilities
                new_map[possible_sum - i] = new_map.get(possible_sum - i, 0) + sum_possibilities

            dp.append(new_map)

        return dp[len(dp) - 1].get(S, 0)
