# 维吉尼亚密码文件
def encode(key, plain):  # 维吉尼亚密码加密函数,key:密钥,plain:明文,返回一个密文字符串
    order_list = []  # 密钥序列
    result = ''
    for letter in key:
        order_list.append(ord(letter)-ord('a'))
    for i in range(0, len(plain)):
        result += chr((ord(plain[i])-ord('a') +
                      order_list[i % len(key)]) % 26+ord('a'))
    print(result)
    return result


def decode(key, cipher):  # 维吉尼亚解密函数,key:密钥,cipher:密文,返回一个明文字符串
    order_list = []  # 密钥序列
    result = ''
    for letter in key:
        order_list.append(ord(letter)-ord('a'))
    for i in range(0, len(cipher)):
        result += chr((ord(cipher[i])-ord('a') -
                      order_list[i % len(key)]) % 26+ord('a'))
    print(result)
    return result


def main():
    encode('interesting', 'zhonghuaminzuweidafuxing')
    decode('boring', 'kqjyhynruwnadzmk')


if __name__ == '__main__':
    main()
