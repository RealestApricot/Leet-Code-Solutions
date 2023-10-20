class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        PreviousRow = [1, 1]
        RowNumber = 1
        while RowNumber < rowIndex:
            RowNumber += 1
            NewRow = []
            for i in range(1, RowNumber):
                NewRow.append(PreviousRow[i-1] + PreviousRow[i])
            NewRow.insert(0, 1)
            NewRow.append(1)
            PreviousRow = NewRow
        return PreviousRow
