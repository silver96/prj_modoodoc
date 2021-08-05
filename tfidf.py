#문장의 단어 토큰을 생성하고 각 단어 수와 가중치를 조정하여 문자를 순서 벡터로 변환


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread #매트릭스 저장할 때 mmwrite, 읽을 땐 mmread
import pickle #변수 타입 그대로 저장

df_review_one_sentence = pd.read_csv('../preprocess/total_hospital_review_one_sentence.csv', index_col=0)
print(df_review_one_sentence.info())

Tfidf = TfidfVectorizer(sublinear_tf=True)      # sublinear_tf는 값의 스무딩 여부를 결정하는 파라미터
Tfidf_matrix = Tfidf.fit_transform(df_review_one_sentence['total_review'])
# fit_transform 된 Tfidf를 갖고 있으면 추후 데이터 추가 가능하므로 따로 저장

with open('./tfidf.pickle', 'wb') as f:
    pickle.dump(Tfidf, f)       # Tfidf 저장

mmwrite('./tfidf_hospital_review.mtx', Tfidf_matrix)        # 유사도 점수 매트릭스 저장
