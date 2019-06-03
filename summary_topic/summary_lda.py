import xlrd
import xlwt
import pandas as pd
# from comment import striptxt
# -*- coding: utf-8 -*-
import numpy as np
import jieba
import numpy
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import lda
import lda.datasets
from summary_topic import striptxt
from race_picture import reload_excel

summary_set = reload_excel.get_RaceSummaryList()
sentence_list = []
for sen_line in summary_set:
    sentence_output = striptxt.seg_sentence(sen_line)  # 这里的返回值是字符串
    sentence_list.append(sentence_output)

# 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(sentence_list)
'''基于普通词频的数组'''
weight = x.toarray()

# print(x)
# analyze = vectorizer.build_analyzer()

'''基于TF-IDF的词频数组'''
# transformer = TfidfTransformer()
# tfidf_matrix = transformer.fit_transform(x)
# weight=tfidf_matrix.toarray()
# mar=np.asarray(weight)
# shape = mar.shape
#
# for x in range(0, shape[0]):
#     for y in range(0, shape[1]):
#         mar[x, y] = mar[x, y] + 0.49
#         mar[x, y] = round(mar[x, y])

model = lda.LDA(n_topics=19, n_iter=1000, random_state=1)
model.fit(np.asarray(weight))
# model.fit(mar.astype(int))  # model.fit_transform(X) is also available 训练的是词频矩阵
topic_word = model.topic_word_  # model.components_ also works
# 文档-主题（Document-Topic）分布
doc_topic = model.doc_topic_

# print("type(doc_topic): {}".format(type(doc_topic)))

# 输出主题中的TopN关键词
word = vectorizer.get_feature_names()
# for w in word:
#     print
#     w
# print
# topic_word[:, :3]
# print
# print(word)
n = 20
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(word)[np.argsort(topic_dist)][:-(n + 1):-1]
    # print(type(topic_words))
    print(u'*Topic {}\n- {}'.format(i, ' '.join(topic_words)))

# print(type(doc_topic))
# print(type(topic_word))
# numpy.savetxt('./art1topic8.csv', doc_topic, delimiter=',')  # 将得到的文档-主题分布保存
# numpy.savetxt('./art2topic8.csv', topic_word, delimiter=',',encoding='utf-8')

# 输出前20篇文章最可能的Topic
label = []
for n in range(0, 20):
    topic_most_pr = doc_topic[n].argmax()
    label.append(topic_most_pr)
    print("doc: {} topic: {}".format(n, topic_most_pr))

# data1 = pd.DataFrame({'comment_txt':comment_output,
#                       'number id':people_id,
#                       'topic label':label,
#                       })
# data1.to_excel(u'topic8_base.xls', index=False, encoding='"utf_8_sig')
# print('信息写入完成！')
