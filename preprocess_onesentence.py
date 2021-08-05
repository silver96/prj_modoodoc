#병원 별 리뷰를 벡터화시키기 위해 한 문장으로 처리

import pandas as pd

df = pd.read_csv('./cleaned_review/total_cleaned_review_du.csv', index_col=0)
df.dropna(inplace=True)
print(len(df['names'].unique()))
one_sentences = []
categories = []
for name in df['names'].unique():
    category = df[df['names']==name].iloc[0,0] #title열에서 1번째 행값만 반환
    categories.append(category)
    temp = df[df['names']==name]['cleaned_sentences']
    one_sentence = ' '.join(temp)       # 여러개 리뷰 한 문장으로 이어붙이기
    one_sentences.append(one_sentence)      # 병원별 리뷰 리스트에 넣기
df_one_sentences = pd.DataFrame({'category':categories, 'names':df['names'].unique(), 'reviews':one_sentences})

print(df_one_sentences.head())
print(df_one_sentences.info())
df_one_sentences.to_csv('./cleaned_review/total_hospital_review_one_sentence.csv', encoding='utf-8-sig')
