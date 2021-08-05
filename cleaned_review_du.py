import pandas as pd

같은 이름의 병원이 존재하므로 리뷰를 기반으로 중복제거

df = pd.read_csv('../crawling/total_reviews_Hospital_and_info.csv', index_col=0)
df.info()
# print(df.duplicated(['reviews']==True)
print(df.duplicated(['reviews']) == True)
df.drop_duplicates(['reviews'], inplace=True)
df.info()
df.to_csv('../crawling/total_reviews_Hospital_and_info_du.csv',encoding='utf-8')
