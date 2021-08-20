import numpy as np
import re
# 希尔密码的加密与解密

# 加密矩阵
key = [[29, 1, 5, 0, 26],
       [28, 17, 38, 25, 8],
       [37, 40, 1, 26, 14],
       [40, 33, 31, 34, 14],
       [31, 23, 29, 12, 23]]

dict = {  # 仅特殊字符 a对应0 0-9:26-35
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25,
    '0': 26,
    '1': 27,
    '2': 28,
    '3': 29,
    '4': 30,
    '5': 31,
    '6': 32,
    '7': 33,
    '8': 34,
    '9': 35,
    ':': 36,
    ';': 37,
    '<': 38,
    '=': 39,
    '[': 40
}

new_dict = {v: k for k, v in dict.items()}


# 求解密密钥
def reverse_key(key):
    a = np.matrix(key)
    #return a.I
    return np.linalg.inv(a)


def encrypt(plaintext, key):
    plain_matrix = []
    key = np.matrix(key)
    for i in plaintext:
        plain_matrix.append([dict[i]])
    plain_matrix = np.matrix(plain_matrix)
    chiper_text = key * plain_matrix
    chiper = ""
    for a in chiper_text:
        chiper += new_dict[a[0] % (len(dict) + 1)]
    print(chiper)


def decrypt(chiper_text):
    decrypt_key = reverse_key(key)
    list = []
    for i in chiper_text:
        list.append([dict[i]])
    list = reverse_key(key) * np.matrix(list)
    chiper = ""
    list = list.A
    for a in list:
        chiper += (new_dict[int(a[0]) % (len(dict))])
    print(chiper)


text = "0ANJA, SCDOP, 7A4R8, 2YQR[, N11Z;, AXCJN, V9<R0, AZXUO, [06;;, 2U4;Z, XWKW:, V2BMV, :9264, :DGOP, JSB=9, L9:EF"
list1 = text.split(", ")
for i in list1:
    decrypt(i)
