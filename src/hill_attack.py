import hill_cipher
import numpy as np
import sys

# Hill密码攻击文件


def matrix_mul(a, b):  # nxn矩阵运算(模26意义下),a:左矩阵,b:右矩阵,返回一个矩阵
    result = np.zeros((a.shape[0], b.shape[1]))
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            for k in range(a.shape[1]):
                result[i][j] = int(result[i][j] + a[i][k] * b[k][j]) % 26
    return result


def attack(n, plain_text, cipher_text):  # 攻击函数,n:维度,plain_text:明文字符串;cipher_text:密文字符串,返回一个密钥矩阵
    plain = []
    cipher = []
    result = np.zeros((n, n))
    j = 0
    plain_list = hill_cipher.str_to_ascii(plain_text)
    cipher_list = hill_cipher.str_to_ascii(cipher_text)
    for i in range(n):  # 做明文密文矩阵的初始化
        plain.append(plain_list[i * n:(i + 1) * n])
        cipher.append(cipher_list[i * n:(i + 1) * n])
        j = i
    plain_matrix = np.array(plain)  # 装入矩阵中
    cipher_matrix = np.array(cipher)
    while hill_cipher.gcd(hill_cipher.get_det(result), 26) != 1:  # 如果给的是一个不满足Hill密码的密钥,则继续
        while hill_cipher.gcd(hill_cipher.get_det(plain_matrix) % 26, 26) != 1:  # 如果明文不可逆
            j += 1
            if (j + 1) * n > len(plain_list):  # 如果所用明文已不足,则报错
                sys.exit('cannot get key: plain text inv error')
            plain.pop(0)  # 弹出上一个明文对
            plain.append(plain_list[(j * n):((j + 1) * n)])  # 填入下一个明文对
            cipher.pop(0)  # 密文更新
            cipher.append(cipher_list[(j * n):((j + 1) * n)])
            cipher_matrix = np.array(cipher)
            plain_matrix = np.array(plain)
        plain_inv = hill_cipher.inv_matrix(plain_matrix)  # 求逆矩阵
        result = matrix_mul(plain_inv, cipher_matrix)  # 求密钥矩阵
    print(result)
    return result


def main():
    attack(2, 'youarepretty', 'kqoimjvdbokn')
    attack(3, 'ysezymxvv', 'qweasdzxc')


if __name__ == '__main__':
    main()
