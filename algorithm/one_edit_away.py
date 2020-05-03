"""
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，
编写一个函数判定它们是否只需要一次(或者零次)编辑。

"""


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if first == second:
            return True
        # first，second长度不为相等或差一位，则直接返回false
        if len(first) != len(second) and \
           len(first) != len(second) + 1 and \
           len(first) + 1 != len(second):
            return False
        # first, second长度相等
        elif len(first) == len(second):
            lf, ls = list(first), list(second)
            for i in range(len(lf)):
                if lf[i] != ls[i]:
                    ls[i] = lf[i]
                    if lf == ls:
                        return True
                    else:
                        return False
            return True
        # first,second长度相差一位
        else:
            longer = list(first if len(first) > len(second) else second)
            shorter = list(first if len(first) < len(second) else second)
            if longer[:-1] == shorter:
                return True
            for i in range(len(shorter)):
                if shorter[i] != longer[i]:
                    shorter.insert(i, longer[i])
                    if shorter == longer:
                        return True
                    break
            return False


s1 = "teacher"
s2 = "reacher"
print(Solution().oneEditAway(s1, s2))
