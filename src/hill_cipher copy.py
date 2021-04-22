import copy
import numpy as np
import sys


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


def get_det(matrix):
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


def cof(matrix, index):
    result = np.zeros((matrix.shape[0] - 1, matrix.shape[1] - 1))
    for i in range(matrix.shape[0]):
        temp = copy.deepcopy(matrix[i])
        if i == index[0] - 1:
            continue
        if i >= index[0]:
            Ri = i - 1
        else:
            Ri = i
        result[Ri] = np.append(temp[:index[1] - 1], temp[index[1]:])
    return get_det(result)


def al_cof(matrix, index):
    return pow(-1, index[0] + index[1]) * cof(matrix, index)


def adj(matrix):
    result = np.zeros((matrix.shape[0], matrix.shape[1]))
    for i in range(1, matrix.shape[0] + 1):
        for j in range(1, matrix.shape[1] + 1):
            result[j - 1][i - 1] = al_cof(copy.deepcopy(matrix), [i, j])
    return result.astype('int')


def inv_matrix(matrix):
    if get_det(matrix) != 0:
        adj_matrix = adj(matrix)
        det = get_det(matrix) % 26
        if gcd(det, 26) != 1:
            sys.exit("Waring: Your matrix is invalid:det not compatible with 26")
        result = np.zeros((adj_matrix.shape[0], adj_matrix.shape[1]))
        for i in range(adj_matrix.shape[0]):
            for j in range(adj_matrix.shape[1]):
                result[i, j] = extended_gcd([0, 1, det], [
                    1, 0, 26]) * adj_matrix[i, j] % 26
        return result
    else:
        sys.exit("Waring: Your matrix is invalid:det zero")


def matrix_mul(key, plain_text):
    cipher_text = [0 for x in range(key.shape[1])]
    for i in range(len(cipher_text)):
        for j in range(key.shape[1]):
            cipher_text[i] = int((
                cipher_text[i] + plain_text[j] * key[j][i]) % 26)
    return cipher_text


def str_to_ascii(string):
    result = []
    for i in string:
        result.append(ord(i) - ord('a'))
    return result


def ascii_to_str(array):
    result = ''
    for i in array:
        result += chr(i + ord('a'))
    return result


def encode(key, plain_text):
    n = key.shape[1]
    encode_array = []
    true_len = len(plain_text)
    plain_text = plain_text.lower()
    if len(plain_text) % n != 0:
        for i in range(n - len(plain_text) % n):
            plain_text += 'a'
    plain_array = str_to_ascii(plain_text)
    for i in range(0, len(plain_array), n):
        encode_array += matrix_mul(key, plain_array[i:i + n])
    encode_array = encode_array[:true_len]
    encode_text = ascii_to_str(encode_array)
    print(encode_text)
    return encode_text


def decode(key, cipher_text):
    inv_key = inv_matrix(key)
    n = inv_key.shape[1]
    decode_array = []
    true_len = len(cipher_text)
    cipher_text = cipher_text.lower()
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
    M = np.array([[17, 17, 5], [21, 18, 21], [2, 2, 19]])
    cipher = encode(M, 'paymoremoney')
    decode(M, cipher)


if __name__ == '__main__':
    main()
