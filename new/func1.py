def func():
    x = 1000
    print( "a")
    print(locals())
    print(globals())
    def fub():
        x = 200
        def fuc():
            nonlocal x
            x= 11000
            print(x)
        fuc()
    fub()
# func()

# print(dir([1,2].__iter__()))


def fun1():
    print(22)
    a=1
    yield a
    print(333)
    b = 2
    yield b

# test = fun1()
# print(">>>",test)
#
# re1 = next(test)
# print("re1",re1)
#
# re2 = next(test)
# print("re2",re2)


def longest_unique_substring(s):
    n = len(s)
    max_length = 0
    start = 0
    char_map = {}

    for end in range(n):
        if s[end] in char_map:
            # 更新左指针 start，确保窗口内没有重复字符
            start = max(char_map[s[end]] + 1, start)

        # 更新当前字符的最新位置
        char_map[s[end]] = end

        # 计算当前窗口大小
        max_length = max(max_length, end - start + 1)

    return max_length


# class LengthUniqueStr

s ="    fly me  to the moom"
d =s.split()
print(d)
max_l = 0
# for i in range(d):


def reverse_words_in_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(lines)
    if len(lines) != 2:
        print("文件内容不符合要求，应该有且仅有两行内容。")
        return

    line1 = lines[0].strip()
    line2 = lines[1].strip()

    words1 = line1.split()
    words2 = line2.split()
    words1.extend(words2)
    print(words1)
    print(words2)
    words1.sort(reverse=True)
    # new_words.s
    print(words1)


reverse_words_in_file("a.txt")