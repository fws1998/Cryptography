import numpy as np
import Hill

def get_key(plain_matrix, chiper_matrix):
    inverse = Hill.reverse_key(plain_matrix)
    print(inverse)
    key = np.dot(inverse, chiper_matrix) % 41
    print(key)
    return key.T