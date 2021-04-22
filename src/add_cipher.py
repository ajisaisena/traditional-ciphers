# 加法密码加密函数，plain:明文；b:加密参数，返回一个密文字符串
def encode(plain, b):
    result = ''
    for letter in plain:
        num = ord(letter)-ord('a')
        num = (num + b) % 26
        result += chr(num+ord('a'))
    print(result)
    return result


def decode(cipher, b):  # 加法密码解密函数，cipher:密文；b:参数，返回一个明文字符串
    result = ''
    for letter in cipher:
        num = ord(letter)-ord('a')
        num = (num-b) % 26
        result += chr(num+ord('a'))
    print(result)
    return result
