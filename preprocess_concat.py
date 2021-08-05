# 전처리한 파일 하나로 합침
import pandas as pd

df = pd.read_csv('./preprocess/cleaned_review_치과.csv', index_col=0)
print(df.info())
df.drop_duplicates()
df.dropna(inplace=True)
print(df.info())

titles = ['치과', '피부과', '성형외과', '안과', '산부인과', '비뇨기과', '정신건강의학과', '정형외과', '마취통증의학과',
              '신경외과', '재활의학과', '영상의학과', '외과', '신경과', '소아과', '내과', '이비인후과', '가정의학과', '한의원']

df.columns = ['category','names', 'cleaned_sentences']
df.to_csv('./preprocess/cleaned_review_치과.csv')

for i in range(1, 19):
    df_temp = pd.read_csv(f'./cleaned_review/cleaned_review_{titles[i]}.csv', index_col=0)
    df.drop_duplicates()
    df_temp.dropna(inplace=True)
    df_temp.columns = ['category', 'names', 'cleaned_sentences']
    df_temp.to_csv(f'./cleaned_review_{titles[i]}.csv', encoding='utf-8-sig')
    df = pd.concat([df, df_temp], ignore_index=True)
print(df.info())
df.to_csv('./preprocess/total_cleaned_review.csv', encoding='utf-8-sig')
