import requests
import json
from sklearn.feature_extraction.text import TfidfVectorizer
result_lines = []
movie_plot_li = []
movie_title_li = []
# http://www.omdbapi.com/?i=tt3896198&apikey=c863e960
# apikey: 13598b0d (daum)
# apikey: c863e960 (gmail)
# current_api_key = 'c863e960'
import codecs
import pickle

def read_data(fin, delim, mode='normal'):
    info_li = []

    index = 0
    for line in codecs.open(fin, 'r', encoding='latin-1'):
        index += 1
        try:
            line_items = line.strip().split(delim)

            key = int(line_items[0])

            if (len(info_li)+1) != key:
                print('errors at data_id')
                print(f'index:{index}')
                exit(0)
            if mode == 'plot':
                info_li.append(line_items[1])
            else:
                info_li.append(line_items[1:])
        except Exception as e:
            print(e)
            print(f'index:{index}')
    print('rows in %s: %d'%(fin, len(info_li)))

    return info_li

fin_movie = 'ml-100k/u.item'
movie_plot_file = 'ml-100k/ml-100k-plot.txt'
movie_info_li = read_data(fin_movie, '|')
movie_plot_li = read_data(movie_plot_file, '|', mode='plot')
# 영화 ID 1부터 100까지의 영화를 가져옵니다.
# 앞에서 생성해둔 무비렌즈 영화 정보 리스트 movie_info_li를 이용합니다.
# OMDb API 유료화로 아래 서비스는 활용할 수 없음
# for movie_info in movie_info_li[:100]:
#     movie_url = movie_info[3]
#
#     if movie_url == '':
#         print(movie_info)
#         movie_title_li.append('')
#         movie_plot_li.append('')
#
#     else:
#         response = requests.get(movie_url)
#         imdb_id = response.url.split('/')[-2]
#         print(imdb_id)
#         if imdb_id == 'www.imdb.com':
#             print('no imdb id of: %s' %(movie_info[0]))
#             IMDB ID가 없을 경유 예외 처리
#             movie_title = ''
#             movie_plot = ''
#     else:
#         try:
#             movie_response = requests.get('http://www.omdbapi.com/?i=' + imdb_id + '&plot=full&r=json&apikey=c86e960' )
#             movie_response = requests.get('http://www.omdbapi.com/?i=' + imdb_id + '&plot=full&r=json&apikey='+current_api_key)
#         except MissingSchema:
#         except:
#             OMDB API의 예외 처리
#             print('wrong URL: %s' % (movie_info[0]))
#             movie_title = ''
#             movie_plot = ''
#
#         try:
#             movie_title = json.loads(movie_response.text)['Title']
#             movie_plot = json.loads(movie_response.text)['Plot']
#             print(movie_response.txt)
#         except KeyError:
#             API 결과의 예외 처리
#             print('incomplete json: %s' % (movie_info[0]))
#             movie_title = ''
#             movie_plot = ''
#     result_lines.append("%s\t%s\n" % (movie_title, movie_plot))
#     movie_plot_li.append(movie_plot)
#     movie_title_li.append(movie_title)

print('download complete: %d movie data download'%(len(movie_title_li)))
# 2개 이하의 문서에서 나오는 단어는 TF-IDF 계산에서 제외합니다. 스톱워드는 'english'로 합니다.
# vectorizer = TfidfVectorizer(min_df=2, stop_words='of')
vectorizer = TfidfVectorizer(min_df=2, stop_words=['of', 'is', ' this', 'that', 'which'])
vectorizer.fit_transform(movie_plot_li)

feature_names = vectorizer.get_feature_names()
print(feature_names)

with open('movie_plot_li.bin', 'wb') as f:
    pickle.dump(movie_plot_li, f)

print('전처리 완료')