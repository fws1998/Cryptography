import decrypt

def sign(m, n, d):
    ans = 1
    while d > 0:
        if d % 2 == 1:
            ans = (ans * m) % n
        d >>= 1
        m = m * m % n
    return ans


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


# 定义一个函数，参数分别为a,n，返回值为b
def findModReverse(a, m):  # 这个扩展欧几里得算法求模逆

    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def blind_sign(m, n, e, d, x):
    m_prime = x ** e * m # compute m'
    s_prime = sign(m_prime, d, n) # compute s'
    inverse_x = findModReverse(x, n) # compute inverse modulo of x
    return inverse_x * s_prime % n


def verify(s, n, e, m):
    message = sign(s, n, e)
    return message == m

n = 1139631134290681913324518075250462509444792614577115360833700594253534083115108212461164873379591734542309312064780949257819665132832661342154198437454459926525649486600336464897081397167045104842672493488133506984881500857942197501
e = 67559
d = 207295768068102279456514335033046425303132165927244033393328116698908705079805377126654354876758366533086185042407386444469697300448993171079415022477995849594447981729168914639729964957529446229650186590220990592254700038562058305
m = 3141592651253193

print(sign(m, n, d))
print(blind_sign(m, n, e, d, 2531))
