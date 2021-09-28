def fast_exp(m, e, n):
    mod = 1
    while e > 1:
        if e & 1 == 1:
            mod = mod * m % n
        m = m * m % n
        e = e >> 1
    return mod * m % n


def sign(m, d, n):
    return fast_exp(m, d, n)


def verify(s, m, e, n):
    return m == fast_exp(s, e, n)


def blind_sign(m, n, e, d, x):
    blind_message = m * sign(x, e, n) % n
    blind_signature = sign(blind_message, d, n)
    print(blind_signature)
    inverse = findModReverse(x, n)
    signature = blind_signature * inverse % n
    return signature

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def findModReverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


n = 1139631134290681913324518075250462509444792614577115360833700594253534083115108212461164873379591734542309312064780949257819665132832661342154198437454459926525649486600336464897081397167045104842672493488133506984881500857942197501
e = 65537
d = 207295768068102279456514335033046425303132165927244033393328116698908705079805377126654354876758366533086185042407386444469697300448993171079415022477995849594447981729168914639729964957529446229650186590220990592254700038562058305
m = 3141592651253193

print(sign(m, d, n))
print(blind_sign(m, n, e, d, 2531))
