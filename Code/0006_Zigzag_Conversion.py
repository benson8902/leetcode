class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        count = 0
        inflection_point = False
        rows = [""]*numRows
        for i in s:
            rows[count] += i
            if inflection_point == False:
                count += 1
            elif inflection_point == True:
                count -= 1
            if count == numRows-1:
                inflection_point = True
            elif count == 0:
                inflection_point = False

        return "".join(rows)
