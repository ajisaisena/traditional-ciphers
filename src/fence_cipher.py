# 栅栏密码文件
def encode(row_num, plain):  # 栅栏密码加密函数,row_num:行数,plain:明文,返回一个密文字符串
    result = ''
    for i in range(row_num):
        buffer = ''
        for j in range(len(plain)):
            if j % row_num == i:
                buffer += plain[j]  # 迭代到指定位置时,加入buffer
        result += buffer
    print(result)
    return result


def decode(row_num, cipher):  # 栅栏密码解密函数,row_num:行数,cipher:密文,返回一个明文字符串
    cipher_iter = 0
    max_num = 0  # 记录分组最大长度
    result = ''
    fences = []
    ex_num = len(cipher) % row_num  # 当密文长度不整除行数时进行记录
    for i in range(row_num):
        buffer = ''
        if i < ex_num:  # 如果在记录的行数前,需要加1位密文
            buffer += cipher[cipher_iter:len(cipher) //
                             row_num + cipher_iter + 1]
            cipher_iter += len(cipher) // row_num + 1
            max_num = len(cipher) // row_num + 1
        else:  # 否则就按照普通的密文分组
            buffer += cipher[cipher_iter:len(cipher) // row_num + cipher_iter]
            cipher_iter += len(cipher) // row_num
            max_num = max(max_num, len(cipher) // row_num)
        fences.append(buffer)
    for i in range(max_num):  # 结果拼接
        if i < max_num - 1:
            for j in range(0, row_num):
                result += fences[j][i]
        else:  # 最后一列拼接
            for j in range(0, ex_num if ex_num != 0 else row_num):
                result += fences[j][i]

    print(result)
    return result


def main():
    m = encode(3, 'whateverisworthdoingisworthdoingwell')
    decode(3, m)
    decode(2, 'hatimriprathnelhelhsoemotntawat')


if __name__ == '__main__':
    main()
