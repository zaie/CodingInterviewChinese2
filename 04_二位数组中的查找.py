# def find_in_matrix(matrix, number):
#     if not isinstance(matrix, list) or len(matrix) == 0 or \
#             not isinstance(matrix[0], list) or not isinstance(number, int):
#         return False

#     # matrix是list of list
#     row = len(matrix)
#     col = len(matrix[0])

#     for i in range(row):
#         if len(matrix[i]) != col:
#             return False

#         for j in range(col):
#             if not isinstance(matrix[i][j], int):
#                 return False

#     i = 0
#     j = col - 1
#     while i < row and j >= 0:
#         if matrix[i][j] == number:
#             return True, i, j

#         if matrix[i][j] > number:
#             j -= 1

#         if matrix[i][j] < number:
#             i += 1
#     return False, None, None


# if __name__ == "__main__":
#     m = [[1, 2, 8, 9],
#          [2, 4, 9, 12],
#          [4, 7, 10, 13],
#          [6, 8, 11, 15]]
#     print(find_in_matrix(m, 15))

1. 从矩阵 matrix 左下角元素（索引设为 (i, j) ）开始遍历，并与目标值对比：
    当 matrix[i][j] > target 时，执行 i-- ，即消去第 i 行元素；
    当 matrix[i][j] < target 时，执行 j++ ，即消去第 j 列元素；
    当 matrix[i][j] = target 时，返回 true ，代表找到目标值。
2. 若行索引或列索引越界，则代表矩阵中无目标值，返回 false 。

每轮 i 或 j 移动后，相当于生成了“消去一行（列）的新矩阵”， 索引(i,j) 指向新矩阵的左下角元素（标志数），因此可重复使用以上性质消去行（列）。

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix) - 1, 0 # 从左下角开始寻找
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target: i -= 1
            elif matrix[i][j] < target: j += 1
            else: return True
        return False

作者：Krahets
链接：https://leetcode.cn/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/solutions/95306/mian-shi-ti-04-er-wei-shu-zu-zhong-de-cha-zhao-zuo/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
