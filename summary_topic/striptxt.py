import jieba
# import loading_article_num
import time


# jieba.load_userdict('userdict.txt')
# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence):
    # sentence_striped=
    sentence_seged = jieba.lcut(sentence.strip(),cut_all=False)
    stopwords = stopwordslist('../based_resources/stopwords.txt')  #x 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


