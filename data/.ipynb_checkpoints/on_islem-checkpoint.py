import pandas as pd
import re
import snowballstemmer


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
    return re.sub(r'(?:^|)\w(?:$)', '', value)

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
    stemmer = snowballstemmer.stemmer('turkish')
    value = value.lower()
    value = stemmer.stemWords(value.split())
    stop_words = ['fakat','lakin','ancak','acaba', 'ama', 'aslında', 'az', 'bazı', 'belki', 'biri', 'birkaç',
                   'birşey', 'biz', 'bu', 'çok', 'çünkü', 'da', 'daha', 'de', 'defa', 'diye', 'eğer', 'en', 'gibi',
                   'hem', 'hep', 'hepsi', 'her', 'hiç', 'için', 'ile', 'ise', 'kez', 'ki', 'kim', 'mı', 'mu', 'mü',
                   'nasıl', 'ne', 'neden', 'nerde', 'nerede', 'nereye', 'niçin', 'niye', 'o', 'sanki', 'şey', 
                   'siz', 'şu', 'tüm', 've', 'veya', 'ya', 'yani']
    value = [item for item in value if not item in stop_words]
    value = ''.join(value)
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