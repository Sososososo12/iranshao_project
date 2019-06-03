from sklearn.feature_extraction.text import *
import xlrd
import jieba
from summary_topic import striptxt
from race_picture import reload_excel

summary_set=reload_excel.get_RaceSummaryList()

# content=jieba.lcut(summary1,cut_all=False)
sentence_list=[]
for sen_line in summary_set:
    sentence_list.append(striptxt.seg_sentence(sen_line))


vectorizer = CountVectorizer()
count = vectorizer.fit_transform(sentence_list)
print(vectorizer.get_feature_names())
print(vectorizer.vocabulary_)
print(count.toarray())

transformer = TfidfTransformer()
tfidf_matrix = transformer.fit_transform(count)
print(tfidf_matrix.toarray())
# print(content)