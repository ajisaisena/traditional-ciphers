import add_cipher

'''
word类：记录测试文档中的字母频率
letter:字母
count:计数
'''
class word():
    def __init__(self, letter, count):
        self.letter = letter
        self.count = count

# alphabet:生成由26个字母类组成的列表，返回字母表
def alphabet():
    alphabet = []
    for i in range(26):
        alphabet.append(word(chr(i+97), 0))
    return alphabet

# 分析函数，字母类在此计数。text:测试文档，返回统计结果
def analyze(text):
    word_count = alphabet()
    for char in text:
        for x in word_count:
            if x.letter == char:
                x.count += 1
    return word_count

# 主要攻击函数。text:测试文档，返回10种可能性
def attack(text):
    result = []
    word_count = analyze(text)
    word_count.sort(key=lambda x: x.count, reverse=True)
    for i in range(10):# 进行前十种可能性分析
        offset = (ord(word_count[i].letter)-ord('a')-4) % 26
        prop_answer = add_cipher.decode(text, offset)
        result.append(prop_answer)
    return result


def main():
    input = open("test.txt", 'r')
    output = open("answer.txt", 'w')
    text = input.read()
    text = text.lower()
    text = add_cipher.encode(text, 15)
    answer = attack(text)
    for ans in answer:
        output.write(ans+'\n')


if __name__ == '__main__':
    main()
