class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        Solution = [[1], [1, 1]]
        RowNumber = 2
        while RowNumber < numRows:
            RowNumber += 1
            PreviousRow = Solution[len(Solution)-1]
            NewRow = []
            for i in range(1, RowNumber-1):
                print(PreviousRow[i-1] + PreviousRow[i])
                NewRow.append(PreviousRow[i-1] + PreviousRow[i])
            NewRow.insert(0, 1)
            NewRow.append(1)
            Solution.append(NewRow)
        return Solution
