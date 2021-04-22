# 一些通用数学函数的库
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def extended_gcd(a, mod):  # 扩展欧几里得算法
    if a[2] == 0:
        return mod[1]
    else:
        q = mod[2] // a[2]
        t1 = mod[0] - q * a[0]
        t2 = mod[1] - q * a[1]
        t3 = mod[2] - q * a[2]
        return extended_gcd([t1, t2, t3], a)
