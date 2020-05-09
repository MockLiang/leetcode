"""
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为
1，也可能是 无限循环
但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 集合法
class Solution:
    def next_num(self, n):
        sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            sum += digit*digit
        return sum

    def isHappy(self, n: int) -> bool:
        if n == 0:
            return False
        is_repeat = {n}
        while True:
            n = self.next_num(n)
            if n == 1:
                return True
            elif n in is_repeat:
                return False
            is_repeat.add(n)

    # 快慢指针法
    def is_happy(self, n):
        slow = n
        fast = n
        while True:
            slow = self.next_num(slow)
            fast = self.next_num(self.next_num(fast))
            print(slow, ", ", fast)
            if fast == 1:
                return True
            elif slow == fast:
                return False
        return True


print(Solution().is_happy(19))
