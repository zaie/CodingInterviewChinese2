# 方法一：逐位判断
# 根据 与运算 定义，设二进制数字 nn ，则有：
# 若 n \& 1 = 0n&1=0 ，则 nn 二进制 最右一位 为 00 ；
# 若 n \& 1 = 1n&1=1 ，则 nn 二进制 最右一位 为 11 。
# 根据以上特点，考虑以下 循环判断 ：
# 判断 nn 最右一位是否为 11 ，根据结果计数。
# 将 nn 右移一位（本题要求把数字 nn 看作无符号数，因此使用 无符号右移 操作）。
# 算法流程：
# 初始化数量统计变量 res = 0res=0 。
# 循环逐位判断： 当 n = 0n=0 时跳出。
# res += n & 1 ： 若 n \& 1 = 1n&1=1 ，则统计数 resres 加一。
# n >>= 1 ： 将二进制数字 nn 无符号右移一位（ Java 中无符号右移为 ">>>" ） 。
# 返回统计数量 res。

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res


# 巧妙方法 n&(n−1) 解析： 二进制数字 n 最右边的 1 变成 0 ，其余不变。
# def count_one(x):
#     count = 0
#     while x:
#         print("{0:b}".format(x))
#         count += 1
#         x = x & (x - 1)
#     return count


# if __name__ == "__main__":
#     print(count_one(x=10))
