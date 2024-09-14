class getLengthUniqueStr:
    def __init__(self, string_list):
        self.dic_str = {}
        self.string_list = string_list
        self.func1()
    def func1(self):
        length = 0
        for str_obj in self.string_list:
            start, end, max_length = 0, 0, 0
            str_dic = dict()
            for end in range(len(str_obj)):
                if str_obj[end] in str_dic:
                    start = max(str_dic[str_obj[end]]+1, start)
                str_dic[str_obj[end]] = end
                max_length = max(max_length, end - start+1)

            # self.dic_str[max_length] = ''.join(list(str_dic.keys()))
            length = max(max_length, length)
        return length, str_dic
    def get_max_length(self):
        # max_length = max(self.dic_str.keys())
        max_length, str_dic = self.func1()
        print(max_length, str_dic)

strs = ["a b c a b c b b"]
# get_length_str = getLengthUniqueStr(strs)

# get_length_str.get_max_length()
#



def get_max_lenth_str(s):
    words = s.split()
    max_length = 0
    for i in words:
        max_length = max(max_length, len(i))
    return max_length
# s = "   fly me   to   the moon  "
# max_str = get_max_lenth_str(s)
# print(max_str)


def read_txt_file():
    with open("a.txt") as f:
        lines = f.readlines()
    line1 = lines[0].strip().split()
    line2 = lines[1].strip().split()
    new_line = line1 + line2
    new_line.sort(reverse=True)
    words = ' '.join(new_line)
    return words

# str_words = read_txt_file()
# print(str_words)

# test1 单例模式


from functools import wraps


def singleton(cls):
    instance = {}
    @wraps(cls)
    def wraaper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wraaper


class Person
    def


