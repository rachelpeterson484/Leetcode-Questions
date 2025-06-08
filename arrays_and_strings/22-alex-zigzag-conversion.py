class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        rowIdx = 0
        direction = 1

        for c in s:
            rows[rowIdx].append(c)
            rowIdx += direction

            if rowIdx > numRows - 1:
                rowIdx = max(0, rowIdx - 2)
                direction = -1

            if rowIdx < 0:
                rowIdx = min(numRows - 1, rowIdx + 2)
                direction = 1

        return ''.join(''.join(row) for row in rows)
