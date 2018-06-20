class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in range(int((n - 1) / 2)):
            for j in range(i + 1, int(n + 1 / 2) + 1):
                if j - i > n - 1 - j:
                    break
                if self.is_valid(i, j, num):
                    return True

        return False

    def is_valid(self, i, j, num):
        if num[0] == '0' and i != 0:
            return False
        if num[i + 1] == '0' and j == i + 1:
            return False

        num1 = int(num[0:i + 1])
        num2 = int(num[i + 1:j + 1])

        while j < len(num) - 1:

            num2 = num2 + num1
            num1 = num2 - num1

            if num.startswith(str(num2), j + 1):
                i = j
                j += len(str(num2))
            else:
                return False

        return True


solution = Solution()
print(solution.isAdditiveNumber("198019823962"))
