# 仿射密码文件
import general_math


def encode(k, b, plain):  # 仿射密码加密, k:乘法参数; plain:明文; b:加法参数，返回一个密文字符串
    if general_math.gcd(k, 26) != 1:  # 互素判断
        print('Invalid index!')
        return -1
    result = ''
    for letter in plain:
        num = ord(letter)-ord('a')
        num = (num * k + b) % 26  # 算法核心部分
        result += chr(num+ord('a'))
    print(result)
    return result


def decode(k, b, cipher):  # 仿射密码解密,k:乘法参数;b:加法参数; cipher:密文,返回一个明文字符串
    if general_math.gcd(k, 26) != 1:
        print('Invalid index!')
        return -1
    result = ''
    for letter in cipher:
        num = ord(letter)-ord('a')
        num = (general_math.extended_gcd([0, 1, k], [1, 0, 26])*(num-b)) % 26
        result += chr(num+ord('a'))
    print(result)
    return result


def main():
    encode(7, 10, 'cryptography')
    encode(9, 13, 'seeyoutomorrow')
    decode(15, 20, 'thisisciphertext')
    encode(2, 1, 'abcdef')


if __name__ == '__main__':
    main()
