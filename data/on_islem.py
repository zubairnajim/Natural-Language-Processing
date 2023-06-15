import pandas as pd
import re
import snowballstemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec


#Sayisal degerlerin yok edilmesi
def remove_numeric(value):
    bfr = [item for item in value if not item.isdigit()]
    bfr = "".join(bfr)
    return bfr

#emoji function
def remove_emoji(value):
    bfr = re.compile("[\U00010000-\U0010ffff]", flags = re.UNICODE)
    bfr = bfr.sub(r'', value)
    return bfr

#tek character 
def remove_single_character(value):
    return re.sub(r'(?:^| )\w(?:$| )', '', value)

#noktalama isaretlerin kaldirmasi
def remove_noktalama(value):
    return re.sub(r'[^\w\s]', '', value)

#link function
def remove_link(value):
    return re.sub(r'((www\.[^s]+)|(https?://[^\s]+))', '', value)

#hashtag 
def remove_hash(value):
    return re.sub(r'#[^\s]+', '', value)

#username function
def remove_username(value):
    return re.sub(r'@[^\s]+', '', value)

#stop word function
def stem_word(value):
    stemmer = snowballstemmer.stemmer("turkish")
    value = value.lower()
    value = stemmer.stemWords(value.split())
    stop_words = ['fakat','lakin','ancak','acaba', 'ama', 'aslında', 'az', 'bazı', 'belki', 'biri', 'birkaç',
                   'birşey', 'biz', 'bu', 'çok', 'çünkü', 'da', 'daha', 'de', 'defa', 'diye', 'eğer', 'en', 'gibi',
                   'hem', 'hep', 'hepsi', 'her', 'hiç', 'için', 'ile', 'ise', 'kez', 'ki', 'kim', 'mı', 'mu', 'mü',
                   'nasıl', 'ne', 'neden', 'nerde', 'nerede', 'nereye', 'niçin', 'niye', 'o', 'sanki', 'şey', 
                   'siz', 'şu', 'tüm', 've', 'veya', 'ya', 'yani']
    value = [item for item in value if not item in stop_words]
    value = ' '.join(value)
    return value

#cagirmasi
def pre_processing(value):
    return [remove_numeric(remove_emoji
                          (remove_single_character
                           (remove_noktalama
                            (remove_link
                             (remove_hash
                              (remove_username
                               (stem_word(word))))))))
                               for word in str(value).split()]

#Bosluklari silmek
def remove_space(value):
    return [item for item in value if item.strip()]

#Bag of words
def bag_of_words(value): 
    vectorizer = CountVectorizer()
    x = vectorizer.fit_transform(value)
    return

#tf-idf model
def tfidf(value):
    vectorizer = TfidfVectorizer()
    x = vectorizer.fit_transform(value)
    return x.toarray().tolist()

#word2vec model
def word2vec(value):
    model = Word2Vec.load("X:\\EEM Dosyalar\\Yazan Zeka 4e Academy\\NLP Dogal Dil\\Natural-Language-Processing/data/word2vec.model")
    bfr_list = []
    bfr_len = len(value)

    for k in value:
        bfr = model.wv.key_to_index[k]
        bfr = model.wv[bfr]
        bfr_list.append(bfr)

    bfr_list = sum(bfr_list)
    bfr_list = bfr_list/bfr_len
    return bfr_list.tolist()
