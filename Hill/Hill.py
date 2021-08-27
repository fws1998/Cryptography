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

def EX_GCD(a,b,arr): #扩展欧几里得
    if b == 0:
        arr[0] = 1
        arr[1] = 0
        return a
    g = EX_GCD(b, a % b, arr)
    t = arr[0]
    arr[0] = arr[1]
    arr[1] = t - int(a / b) * arr[1]
    return g


def ModReverse(a,n): #ax=1(mod n) 求a模n的乘法逆x
    arr = [0,1,]
    gcd = EX_GCD(a,n,arr)
    if gcd == 1:
        return (arr[0] % n + n) % n
    else:
        return -1


# 求解密密钥
def reverse_key(key):
    list_A1 = []
    A1 = np.array(key)

    for i in range((np.linalg.inv(A1) * np.linalg.det(A1)).shape[0]):
        for j in range((np.linalg.inv(A1) * np.linalg.det(A1)).shape[1]):
            list_A1.append(round((np.linalg.inv(A1) * np.linalg.det(A1))[i][j]))  # round(x,n)n是表示保留几位小数，不写n默认是整数即n=0。

    A2 = np.array([list_A1], dtype=int)  # 伴随矩阵
    A2 = A2.reshape(A1.shape[0], A1.shape[1])  # 重塑矩阵,行列信息和A1相同。

    # 2.求((1/行列式)%26) A3。
    # 注意当行列式过大之后 （1/行列式）再进行模运算的时候会造成较大精度误差。通过除法改乘法来减小精度误差（1/行列式）% 26 =（1*行列式的乘法逆元）%26。
    A3 = ModReverse(round(np.linalg.det(A1)), len(dict))

    # 3.求逆矩阵A4
    A4 = (A3 * A2) % len(dict)
    return A4

decrypt_key = reverse_key(key)


def encrypt(plaintext, key):
    plain_matrix = []
    key = np.matrix(key)
    for i in plaintext:
        plain_matrix.append(dict[i])
    plain_matrix = np.matrix(plain_matrix)
    chiper_text = np.dot(key, plain_matrix)
    chiper = ""
    for a in chiper_text:
        chiper += new_dict[a[0] % (len(dict))]
    print(chiper)


def decrypt(chiper_text, key):
    list = []
    for i in chiper_text:
        list.append([dict[i]])
    list = np.dot(key, np.matrix(list))
    chiper = ""
    list = list.tolist()
    for a in range(0, 5):
        chiper += (new_dict[list[a][0] % (len(dict))])
    print(chiper)


text = "0ANJA, SCDOP, 7A4R8, 2YQR[, N11Z;, AXCJN, V9<R0, AZXUO, [06;;, 2U4;Z, XWKW:, V2BMV, :9264, :DGOP, JSB=9, L9:EF"
list1 = text.split(", ")
for i in list1:
    decrypt(i, decrypt_key)