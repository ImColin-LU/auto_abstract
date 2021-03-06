# -*- encoding:utf-8 -*-
import os
import math
import networkx as nx
import numpy as np

sentence_delimiters = ['?', '!', ';', '？', '！', '。', '；', '……', '…', '\n']
allow_speech_tags = ['an', 'i', 'j', 'l', 'n', 'nr', 'nrfg', 'ns', 'nt', 'nz', 't', 'v', 'vd', 'vn', 'eng']


class AttrDict(dict):
    """Dict that can get attribute by dot"""

    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


def combine(word_list, window=2):#用于构建网络的边
    """构造在window下的单词组合，用来构造单词之间的边。
    """
    if window < 2: window = 2
    for x in range(1, window):
        if x >= len(word_list):
            break
        word_list2 = word_list[x:]
        res = zip(word_list, word_list2)
        for r in res:
            yield r


def get_similarity(word_list1, word_list2):#计算两个句子的相似程度
    """默认的用于计算两个句子相似度的函数。
    Keyword arguments:
    word_list1, word_list2  --  分别代表两个句子，都是由单词组成的列表
    """
    words = list(set(word_list1 + word_list2))
    vector1 = [float(word_list1.count(word)) for word in words]
    #统计某个单词在句子中的频率
    vector2 = [float(word_list2.count(word)) for word in words]

    vector3 = [vector1[x] * vector2[x] for x in range(len(vector1))]
    vector4 = [1 for num in vector3 if num > 0.]
    co_occur_num = sum(vector4)#分子——同时在两句子中的词的数目

    if abs(co_occur_num) <= 1e-12:
        return 0.

    denominator = math.log(float(len(word_list1))) + math.log(float(len(word_list2)))  # 分母

    if abs(denominator) < 1e-12:
        return 0.

    return co_occur_num / denominator#返回句子的相似度


def sort_words(vertex_source, edge_source, window=2, pagerank_config={'alpha': 0.85, }):#对单词的关键程度进行排序
    """
    vertex_source   --  二维列表，子列表代表句子，子列表的元素是单词，这些单词用来构造pagerank中的节点
    edge_source     --  二维列表，子列表代表句子，子列表的元素是单词，根据单词位置关系构造pagerank中的边
    window          --  一个句子中相邻的window个单词，两两之间认为有边
    pagerank_config --  pagerank的设置
    """
    sorted_words = []
    word_index = {}
    index_word = {}
    _vertex_source = vertex_source
    _edge_source = edge_source
    words_number = 0
    for word_list in _vertex_source:#对每个句子进行处理，提取出的是包含单词的列表
        for word in word_list:
            if not word in word_index:#更新word_index 假如字典中没有单词，就将这个单词与索引添加到字典中
                word_index[word] = words_number
                index_word[words_number] = word#对word进行反向映射
                words_number += 1

    graph = np.zeros((words_number, words_number))#构建一个word_number*word_number的矩阵，实现图计算

    for word_list in _edge_source:
        for w1, w2 in combine(word_list, window):
            if w1 in word_index and w2 in word_index:
                index1 = word_index[w1]
                index2 = word_index[w2]
                graph[index1][index2] = 1.0
                graph[index2][index1] = 1.0
    #根据窗口判断其连接

    nx_graph = nx.from_numpy_matrix(graph)
    #构成邻接矩阵
    scores = nx.pagerank(nx_graph, **pagerank_config)  # 使用pageRank算法进行迭代
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    for index, score in sorted_scores:
        item = AttrDict(word=index_word[index], weight=score)
        sorted_words.append(item)

    return sorted_words


def sort_sentences(sentences, words, sim_func=get_similarity, pagerank_config={'alpha': 0.85, }):#对句子进行排序

    sorted_sentences = []
    _source = words
    sentences_num = len(_source)
    graph = np.zeros((sentences_num, sentences_num))#矩阵表示连接

    for x in range(sentences_num):
        for y in range(x, sentences_num):
            similarity = sim_func(_source[x], _source[y])
            graph[x, y] = similarity
            graph[y, x] = similarity

    nx_graph = nx.from_numpy_matrix(graph)
    scores = nx.pagerank(nx_graph, **pagerank_config)  # this is a dict
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)

    for index, score in sorted_scores:
        item = AttrDict(index=index, sentence=sentences[index], weight=score)
        sorted_sentences.append(item)

    return sorted_sentences


if __name__ == '__main__':
    pass