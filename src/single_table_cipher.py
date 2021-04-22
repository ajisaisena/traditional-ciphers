# 单表密码文件
def encode(table, plain):  # 单表加密函数,table:表,plain:明文,返回一个密文字符串
    alphas = [chr(i) for i in range(97, 123)]
    alpha_dict = {}  # 使用字典
    result = ''
    for i in range(0, 26):
        alpha_dict[alphas[i]] = table[i]
    for letter in plain:
        result += alpha_dict[letter]
    print(result)
    return result


def decode(table, cipher):  # 单表解密函数,table:表,cipher:密文,返回一个明文字符串
    alphas = [chr(i) for i in range(97, 123)]
    table_dict = {}
    result = ''
    for i in range(0, 26):
        table_dict[table[i]] = alphas[i]
    for letter in cipher:
        result += table_dict[letter]
    print(result)
    return result


def main():
    table = 'qazwsxedcrfvtgbyhnujmiklop'
    encode(table, 'doyouwannatodance')
    decode(table, 'youcanreallydance')


if __name__ == '__main__':
    main()
