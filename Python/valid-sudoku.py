# Time:  O(9^2)
# Space: O(9)

# Determine if a Sudoku is valid, 
# according to: Sudoku Puzzles - The Rules.

# Three rules
# 1. Each row has 1-9 once
# 2. Each column has number 1-9 once
# 3. Each 9 boxes have number 1-9

#
# The Sudoku board could be partially filled, 
# where empty cells are filled with the character '.'.
#
# A partially filled sudoku which is valid.
#
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable.
# Only the filled cells need to be validated.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in xrange(9):
            # 如果横排和竖排的数字不为真(有重复的数字)
            if not self.isValidList([board[i][j] for j in xrange(9)]) or \
               not self.isValidList([board[j][i] for j in xrange(9)]):
                # 则返回错误
                return False
        # 两个for循环组成一个3*3的数组框
        for i in xrange(3):
            for j in xrange(3):
                # 这一排代码什么意思？
                if not self.isValidList([board[m][n] for n in xrange(3 * j, 3 * j + 3) \
                                                     for m in xrange(3 * i, 3 * i + 3)]):
                    return False
        return True

    # 用来判断有没有重复的数字
    def isValidList(self, xs):
        # 返回不为空的数字组成的数组
        # xs中x不等于.的数字
        xs = filter(lambda x: x != '.', xs)
        # 采用set来过滤掉重复的数字
        # 如果set的大小和原数组一样，则说明没有重复的数字，返回true
        return len(set(xs)) == len(xs)


if __name__ == "__main__":
    board = [[1, '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', 2, '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', 3, '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', 4, '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', 5, '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', 6, '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', 7, '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', 8, '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', 9]]
    print Solution().isValidSudoku(board)
