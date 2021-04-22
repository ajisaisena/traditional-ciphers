import copy
import numpy as np
import sys
import general_math
# Hill密码文件
# 出于对代码阅读体验的考虑,我在此文件中采用了numpy中的函数
# 主要用于进行矩阵的格式化,并未直接调用库函数完成任何关键函数.
# 如果不使用Numpy库,该实验依然可以轻松完成,仅在部分地方繁琐一些


def get_det(matrix):  # 求行列式,matrix:矩阵,返回一个行列式值
    # 行列式方法采用不断进行行变换直至矩阵变为上三角矩阵的方法求行列式值
    temp_matrix = copy.deepcopy(matrix).astype('float')
    n = temp_matrix.shape[0]
    result = 1
    for column in range(n):
        row = column
        result *= temp_matrix[row][column]
        while temp_matrix[row][column] == 0 and row < n - 1:
            row += 1
        for i in range(row + 1, n):
            if temp_matrix[i][column] == 0:
                pass
            else:
                k = -temp_matrix[i][column] / temp_matrix[row][column]
                for j in range(column, n):
                    temp_matrix[i][j] += temp_matrix[row][j] * k
    return round(result, 0)


def cof(matrix, index):  # 求余子式函数,matrix:矩阵,index:所求余子式的行列坐标列表,返回一个余子式
    result = np.zeros((matrix.shape[0] - 1, matrix.shape[1] - 1))
    for i in range(matrix.shape[0]):
        temp = copy.deepcopy(matrix[i])  # 采用deepcopy防止修改原矩阵值
        if i == index[0] - 1:
            continue
        if i >= index[0]:
            true_i = i - 1  # true_i是真正的行的值,在跳过一行后需要-1
        else:
            true_i = i
        result[true_i] = np.append(temp[:index[1] - 1], temp[index[1]:])
    return get_det(result)


def al_cof(matrix, index):  # 求代数余子式,matrix:矩阵,index:所求余子式行列坐标列表,返回一个代数余子式
    return pow(-1, index[0] + index[1]) * cof(matrix, index)


def adj(matrix):  # 求余子式矩阵,matrix:矩阵,返回一个余子式矩阵
    result = np.zeros((matrix.shape[0], matrix.shape[1]))
    for i in range(1, matrix.shape[0] + 1):
        for j in range(1, matrix.shape[1] + 1):
            result[j - 1][i - 1] = al_cof(copy.deepcopy(matrix), [i, j])
    return result.astype('int')


def inv_matrix(matrix):  # 求模26意义下矩阵的逆,matrix:矩阵,返回一个矩阵
    if get_det(matrix) != 0:  # 检查:如果等于0,则无法求解
        adj_matrix = adj(matrix)
        det = get_det(matrix) % 26
        if general_math.gcd(det, 26) != 1:
            sys.exit("Waring: Your matrix is invalid:det not compatible with 26")
        result = np.zeros((adj_matrix.shape[0], adj_matrix.shape[1]))
        for i in range(adj_matrix.shape[0]):  # 乘行列式逆元
            for j in range(adj_matrix.shape[1]):
                result[i, j] = general_math.extended_gcd([0, 1, det], [
                    1, 0, 26]) * adj_matrix[i, j] % 26
        return result
    else:
        sys.exit("Waring: Your matrix is invalid:det zero")


def matrix_mul(key, plain):  # 矩阵乘法,key:密钥矩阵,plain:明文矩阵,返回一个密文矩阵
    cipher_text = [0 for x in range(key.shape[1])]
    for i in range(len(cipher_text)):
        for j in range(key.shape[1]):
            cipher_text[i] = int((
                cipher_text[i] + plain[j] * key[j][i]) % 26)
    return cipher_text


def str_to_ascii(string):  # 转换函数,string:字符串,返回一组ascii码
    result = []
    for i in string:
        result.append(ord(i) - ord('a'))
    return result


def ascii_to_str(array):  # 转换函数,array:ascii列表,返回一个字符串
    result = ''
    for i in array:
        result += chr(i + ord('a'))
    return result


def encode(key, plain_text):  # Hill密码加密函数,key:密钥矩阵,plain_text:明文字符串,返回一个密文字符串
    n = key.shape[1]
    encode_array = []
    true_len = len(plain_text)
    if len(plain_text) % n != 0:  # 如果不满足分组,加上一定长度
        for i in range(n - len(plain_text) % n):
            plain_text += 'a'
    plain_array = str_to_ascii(plain_text)
    for i in range(0, len(plain_array), n):
        encode_array += matrix_mul(key, plain_array[i:i + n])
    encode_array = encode_array[:true_len]  # 密文截取
    encode_text = ascii_to_str(encode_array)
    print(encode_text)
    return encode_text


def decode(key, cipher_text):  # Hill密码解密函数,key:密钥矩阵,cipher_text:密文字符串,返回一个明文字符串
    inv_key = inv_matrix(key)
    n = inv_key.shape[1]
    decode_array = []
    true_len = len(cipher_text)
    if len(cipher_text) % n != 0:
        for i in range(n - len(cipher_text) % n):
            cipher_text += 'a'
    cipher_array = str_to_ascii(cipher_text)
    for i in range(0, len(cipher_array), n):
        decode_array += matrix_mul(inv_key, cipher_array[i:i + n])
    decode_array = decode_array[:true_len]
    decode_text = ascii_to_str(decode_array)
    print(decode_text)
    return decode_text


def main():
    matrix = np.array([[5, 8], [17, 3]])
    cipher = encode(matrix, 'loveyourself')
    decode(matrix, cipher)
    matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
    decode(matrix, 'qweasdzxc')


if __name__ == '__main__':
    main()
