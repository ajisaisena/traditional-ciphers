# 弗纳姆密码文件
def encode(key, plain):  # vernam加密函数,key:密钥,plain:明文,返回密文ascii码值,打印密文ascii码
    result = []
    for i in range(len(plain)):
        n = ord(plain[i]) ^ ord(key[i])
        result.append(int(n))
    for num in result:
        print(chr(num))
    print()
    return result


def decode(key, cipher):  # vernam解密函数,key:密钥,cipher:密文,返回一个明文字符串
    result = ''
    for i in range(len(cipher)):
        n = ord(key[i]) ^ ord(cipher[i])
        result += chr(int(n))
    print(result)
    return result


def main():
    input1 = open('input1.txt', 'r')
    input2 = open('input2.txt', 'r')
    output1 = open('output1.txt', 'w')
    output2 = open('output2.txt', 'w')
    plain = input1.read()
    cipher = input2.read()
    cipher1 = encode('Todayis20200308', plain)
    plain2 = decode('12345abcde', cipher)
    for num in cipher1:
        output1.write(chr(num))
    for char in plain2:
        output2.write(char)
    input1.close()
    output1.close()
    input2.close()
    output2.close()


if __name__ == '__main__':
    main()
