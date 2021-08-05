
import pandas as pd
from konlpy.tag import Okt
import re

categories = ['가정의학과', '내과', '마취통증의학과', '비뇨기과', '산부인과', '성형외과', '소아과',
              '신경과', '신경외과', '안과', '영상의학과', '외과', '이비인후과', '재활의학과',
              '정신건강의학과', '정형외과', '치과', '피부과', '한의원']

for category in categories:
    df = pd.read_csv(f'../crawling/reviews_Hospital_{category}.csv', index_col = 0)

    # 형태소 분리
    okt = Okt()

    # 불용어
    stopwords = pd.read_csv('stopwords.csv', index_col=0)
    # print(stopwords.head())
    hospital_stopwords = ['병원', '가격', '정보', '하다', '되어다', '있다', '같다', '해주다', '되다', '이다', '가다', '보다', '않다', '진료', '선생님', '좋다', '그렇다',
                 '자다', '항상', '리뷰', '받다', '없다', '많다', '의사', '조금', '간호사', '다른', '알다', '일단', '때문', '줄평', '직원', '정말', '그냥',
                 '나오다', '해주시', '기다', '여기', '정도', '알다', '매우', '모두', '궁금하다', '아니다', '둘다', '은빛', '들다', '맞다', '오다', '다음', '다니다', '어떻다',
                 '아니다', '생각', '대해', '콤비 치과', '친절하다', '치료', '가격', '정보']
    stopwords_list = list(stopwords.stopword) + hospital_stopwords # stopwords 컬럼 list형식으로 변환 후 새로운 stopwords list와 결합

    # reviews 컬럼에서 문장을 하나씩 추출
    count = 0
    cleaned_sentences = []
    for sentence in df.reviews:
        count += 1
        if count % 10 == 0: # 문장 10개 처리시 .
            print('.', end='')
        if count % 100 == 0: # 문장 100개 처리시 줄바꿈
            print('')
        sentence = re.sub('[^가-힣 | ' ']', '', str(sentence)) # 리뷰 하나 꺼내 sentence로 받음
        token = okt.pos(sentence, stem=True) # 형용사 동사는 원형으로
        df_token = pd.DataFrame(token, columns=['word', 'class']) # 형태소와 품사 분류
        df_cleaned_token = df_token[(df_token['class'] == 'Noun') | # 조건 인덱싱
                            (df_token['class'] == 'Verb') |
                            (df_token['class'] == 'Adjective')]
        words = []
        for word in df_cleaned_token['word']: # 불용어 제거
            if len(word) > 1:
                if word not in stopwords_list:
                    words.append(word)
        cleaned_sentence = ' '.join(words)
        cleaned_sentences.append(cleaned_sentence)
    df['cleaned_sentences'] = cleaned_sentences # 새 컬럼 생성
    df['category'] = category
    print(df.head())

    print(df.info())

    df = df[['category', 'names', 'cleaned_sentences']] # 타이틀과 전처리가 된 문장만 뽑아내기
    print(df.info())
    df.to_csv(f'./preprocess/cleaned_review_{category}.csv') # 재저장
