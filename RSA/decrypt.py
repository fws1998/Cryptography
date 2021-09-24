import encrypt


def verify(s, n, e, m):
    message = encrypt.sign(s, n, e)
    return message == m
