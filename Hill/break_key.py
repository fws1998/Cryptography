import numpy as np
import Hill

def get_key(plain_matrix, chiper_matrix):
    inverse = Hill.reverse_key(plain_matrix)
    key = np.dot(chiper_matrix, inverse) % 41
    print(key)
    return key