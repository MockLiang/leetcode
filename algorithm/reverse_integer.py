"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

"""


class Solution:
    def reverse(self, x: int) -> int:
        flag = -1 if x < 0 else 1
        if x < 0:
            x = -x
        R = str(x)[::-1]
        R = int(R)

        return R*flag


print(Solution().reverse(-12300))
