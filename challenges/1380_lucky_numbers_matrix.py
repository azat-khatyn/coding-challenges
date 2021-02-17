"""
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.


Input: matrix = [[7,8],[1,2]]
Output: [7]
"""

def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
    lucky_candidate_rows = []
    for row in matrix:
        min_in_row = None
        for i in range(len(row)):
            if min_in_row is None or row[i] < row[min_in_row]:
                min_in_row = i
        lucky_candidate_rows.append(min_in_row)

    result = []
    for i in range(len(lucky_candidate_rows)):
        element = matrix[i][lucky_candidate_rows[i]]
        p = True
        for j in range(len(matrix)):
            if element < matrix[j][lucky_candidate_rows[i]]:
                p = False
                break
        if p:
            result.append(element)
    return result
