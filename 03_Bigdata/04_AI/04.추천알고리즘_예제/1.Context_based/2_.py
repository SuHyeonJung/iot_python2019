from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import  cosine_similarity
import pickle
import codecs

def read_data(fin, delim):
    info_li = []

    for line in codecs.open(fin, 'r', encoding='latin-1'):
        line_items = line.strip().split(delim)

        key = int(line_items[0])

        if (len(info_li)+1) != key:
            print('errors at data_id')
            exit(0)
        info_li.append(line_items[1:])

    print('rows in %s: %d'%(fin, len(info_li)))

    return info_li

def similar_recommend_by_movie_id(movielens_id):
    movie_index = movielens_id-1
    # enumerate 함수로 [(리스트 인덱스 0, 유사도 0), (리스트 인덱스 1, 유사도 1)...]의
    # 리스트를 만듭니다. 그 후 각 튜플의 두 번째 항목, 즉 유사도를 이용하여 내림차순 정렬합니다.
    # 이렇게 만든 리스트의 가장 앞 튜플의 첫 번째 항목이 영화 ID가 됩니다.
    similar_movies = sorted(list(enumerate(movie_sim[movie_index])),key=lambda x:x[1], reverse=True)
    recommended = 1
    print("-----recommendation for movie %d------"%(movielens_id))
    for movie_info in similar_movies[1:6]:
        # 주어진 영화오 가장 비슷한 영화는 그 영화 자신이므로 출력 시 제외합니다.
        movie_title = movie_info_li[movie_info[0]]
        print('rank %d recommendation:%s'%(recommended,movie_title[0]))
        recommended += 1

f = open('movie_plot_li.bin', 'rb')
vectorizer2 = TfidfVectorizer(min_df=2, stop_words=['of', 'is', 'this', 'that', 'which'])

movie_plot_li = pickle.load(f)
# 모든 영화 Plot에 대한 Vacabulary 기준 CSR을 만들어준다.
X = vectorizer2.fit_transform(movie_plot_li)
feature_names = vectorizer2.get_feature_names()

movie_sim = cosine_similarity(X)

fin_movie = 'ml-100k/u.item'
movie_info_li = read_data(fin_movie, '|')

similar_recommend_by_movie_id(1)