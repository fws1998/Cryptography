import numpy as np


# 将文本转化为数字矩阵
def text_to_number(text, dict, m):
    matrix = text_to_matrix(text, m)
    for i in range(0, m):
        for j in range(0, m):
            matrix[i][j] = dict[matrix[i][j]]
    return matrix


# 将文本转化为字符矩阵
def text_to_matrix(text, m):
    matrix = np.zeros((m, m), dtype="int32")
    matrix = matrix.tolist()
    for i in range(0, len(text)):
        matrix[int(i/m)][i % m] = text[int(i)]
    return matrix
