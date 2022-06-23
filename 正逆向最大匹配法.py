# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 21:07
# @Author  : Ling_dy
# @FileName: 自然语言练习.py.py
# @Software: PyCharm
class IMM(object):
    def __init__(self,dic_path):
        self.dictionary = set()
        self.maximum = 0
        #读取字典
        with open(dic_path,'r',encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                self.dictionary.add(line)
                if len(line) > self.maximum:
                    self.maximum = len(line)
    def cut(self,text):
        result = []
        index = len(text)
        #逆向最大匹配法
        while index >0:
            word = None
            for size in range(self.maximum,0,-1):#-1为步数，结尾为0，开头为self.maximum
                if index - size <0:
                    continue
                piece = text[(index - size):index]
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    index -= size
                    break
            if word is None:
                index -= 1
        return result[::-1]#倒置列表
    #正向最大匹配法
    # def cut1(self,text):
    #     result1 = []
    #     index = 1
    #     while index >0:
    #         word1 = None
    #         for size in range(self.maximum,0,-1):
    #             if index - size>0:
    #                 break
    #             piece = text[index-1:index-1+size]
    #             if piece in self.dictionary:
    #                 word1 = piece
    #                 result1.append(word1)
    #                 index += size
    #                 break
    #         if word1 is None:
    #             index += 1
    #     return result1[::-1]
    #双向最大匹配法




    # def cut2(self,text):
    #     result1 = cut(text)
    #     result2 = cut1(text)
    #     if len(result1) < len(result2):
    #         return result1
    #     else:
    #         return result2


def main():
    text = "南京市长江大桥"
    tokenizer = IMM('imm_dic.utf8')
    print(tokenizer.cut(text))
    print(tokenizer.cut1(text))
main()
