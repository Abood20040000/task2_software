def rotate_matrix_90(matrix):
    resultMatrix=[]
    length=len(matrix)
    for i in range(length):
        resultMatrix.append([])
    for i in range(length):
        for y in range(length):
            resultMatrix[i].insert(0,matrix[y].pop(0))

    return resultMatrix           


test=rotate_matrix_90([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(test)

