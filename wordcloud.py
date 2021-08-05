import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import collections
from konlpy.tag import Okt
import matplotlib as mpl
from matplotlib import font_manager, rc

# 한글 폰트 안 깨지도록 설정
fontpath = './Jalnan.ttf'
font_name = font_manager.FontProperties(fname=fontpath).get_name()
rc('font', family=font_name)
mpl.font_manager._rebuild()

df = pd.read_csv('../crawling/model_data_Hospital_and_info.csv', index_col=0)
df.dropna(inplace=True)
print(df.info())

categories = ['가정의학과', '내과', '마취통증의학과', '비뇨기과', '산부인과', '성형외과', '소아과',
              '신경과', '신경외과', '안과', '영상의학과', '외과', '이비인후과', '재활의학과',
              '정신건강의학과', '정형외과', '치과', '피부과', '한의원']

#print(df.head(20))
for category in categories:
    hospital_index = df[df['category'] == category].index[0]        # 영화의 첫 번재 인덱스 확인
    #print(movie_index)
    print(df.total_review[hospital_index])
    words = df.total_review[hospital_index].split(' ')        # 문장을 띄어쓰기 기준으로 잘라 문자열 리스트로 반환
    print(words)

    worddict = collections.Counter(words)       # 유니크한 단어를 뽑아 몇 번 나오는지 빈도 표시
    worddict = dict(worddict)
    print(worddict)
    hospital_stopwords = ['병원', '가격', '정보', '하다', '되어다', '있다', '같다', '해주다', '되다', '이다', '가다', '보다', '않다', '진료', '선생님',
                          '좋다', '그렇다',
                          '자다', '항상', '리뷰', '받다', '없다', '많다', '의사', '조금', '간호사', '다른', '알다', '일단', '때문', '줄평', '직원',
                          '정말', '그냥',
                          '나오다', '해주시', '기다', '여기', '정도', '알다', '매우', '모두', '궁금하다', '아니다', '둘다', '은빛', '들다', '맞다', '오다',
                          '다음', '다니다', '어떻다',
                          '아니다', '생각', '대해', '콤비 치과', '친절하다', '치료', '가격', '정보']

    # wordcloud_img = WordCloud(background_color = 'white', max_words = 2000,
    #                           font_path = fontpath, stopwords=stopwords).generate_from_frequencies(worddict)
    wordcloud_img = WordCloud(background_color = 'white', max_words = 2000,
                              font_path = fontpath, stopwords=hospital_stopwords).generate(df.total_review[hospital_index])
    plt.figure(figsize=(8,8))
    plt.imshow(wordcloud_img, interpolation='bilinear')
    plt.axis('off')     # 눈금 끄기
    plt.title(df.category[hospital_index], size=25)
    wordcloud_img.to_file(f'cleaned_{category}.png')
