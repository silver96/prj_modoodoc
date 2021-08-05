#키워드기반으로 한 추천시스템 구현에 활용

import pandas as pd
from gensim.models import Word2Vec

review_word = pd.read_csv('./preprocess/total_cleaned_review.csv', index_col=0)
print(review_word.info())
cleaned_token_review = list(review_word['cleaned_sentences'])
print(len(cleaned_token_review))
cleaned_tokens = []
count = 0
for sentence in cleaned_token_review:
    token = sentence.split(' ')     # 띄어쓰기 기준으로 각 단어 토큰화
    cleaned_tokens.append(token)
# print(len(cleaned_tokens))
# print(cleaned_token_review[0])
# print(cleaned_tokens[0])
embedding_model = Word2Vec(cleaned_tokens, vector_size=100, window=4,
                           min_count=10, workers=4, epochs=100, sg=1)   # vector_size는 몇차원으로 줄일지 지정, window는 CNN의 kernel_size 개념, 앞뒤로 고려하는 단어의 개수를 나타냄
                                                                        # min_count는 출현 빈도가 20번 이상인 경우만 word track에 추가하라는 의미(즉, 자주 안 나오는 단어는 제외)
                                                                        # workers는 cpu 스레드 몇개 써서 작업할 건지 지정, sg는 어떤 알고리즘 쓸건지 지정
embedding_model.save('./models/word2VecModel_hospital_l2.model')
print(embedding_model.wv.vocab.keys())
print(len(embedding_model.wv.vocab.keys()))
