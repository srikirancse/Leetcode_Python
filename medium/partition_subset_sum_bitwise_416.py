class Solution:
    def canPartition(self, nums):
        if sum(nums) & 1:
            return False
        bit_cache = 1
        for n in nums:
            bit_cache |= bit_cache << n
        print(bit_cache)
        return bool(bit_cache & (1 << int(sum(nums) / 2)))


solution = Solution()
solution.canPartition([1, 5, 11, 5])
