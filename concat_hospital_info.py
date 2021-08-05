import pandas as pd

# #중복 제거
# df_dup = pd.read_csv('./crawling/cleaned_review_2020.csv', index_col=0)
# print(df_dup.duplicated().sum())
# df_undup = df_dup.drop_duplicates()
# print(df_undup.duplicated().sum())
# df_undup.to_csv('./crawling/cleaned_review_2020.csv')
# exit()


df = pd.read_csv('../preprocess/cleaned_review/total_hospital_review_one_sentence.csv', index_col=0)
print(df.info())
df.drop_duplicates()
df.dropna(inplace=True)
print(df.info())

df_temp = pd.read_csv('./total_reviews_Hospital_info.csv', index_col=0)
print(df_temp.info())
df_temp.drop_duplicates()
df_temp.dropna(inplace=True)
print(df_temp.info())

df.columns = ['category', 'names','reviews']
df_temp.columns = ['names', 'clinic','address','link','telephone']
#df_temp.to_csv(f'./cleaned_review_2_{titles[i]}.csv', encoding='utf-8-sig')

categories = []
names = []
reviews = []

clinics =[]
addresses = []
links = []
telephones = []

name_list = list(df_temp['names'])
# print(name_list)

for i in range(3444):
    try:
        if df.iloc[i, 1] in name_list:
            category = df['category'][i]
            name = df['names'][i]
            review = df['reviews'][i]
            clinic = df_temp[df_temp['names']==df['names'][i]].iloc[0,1]
            address = df_temp[df_temp['names'] == df['names'][i]].iloc[0, 2]
            link = df_temp[df_temp['names'] == df['names'][i]].iloc[0, 3]
            telephone = df_temp[df_temp['names'] == df['names'][i]].iloc[0, 4]
            categories.append(category)
            names.append(name)
            reviews.append(review)
            clinics.append(clinic)
            addresses.append(address)
            links.append(link)
            telephones.append(telephone)
    except:
        pass
print(categories, names)
df = pd.DataFrame({'category':categories, 'names':names, 'reviews':reviews,
                   'clinics':clinics, 'addresses':addresses, 'links':links, 'telephones':telephones})
print(df.info())
df.to_csv('./total_reviews_Hospital_and_info.csv', encoding='utf-8-sig')

df_use = df[['category','names', 'reviews', 'clinics']]
df_use['total_review'] = df_use['reviews'].str.cat(df_use['clinics'], sep=' ')
df_use = df_use[['category','names', 'total_review']]
df_use.head()
df_use.to_csv('./model_data_Hospital_and_info.csv', encoding='utf-8-sig')
# df.dropna(inplace=True)
# print(df.info())
# df.to_csv('./total_reviews_Hospital_and_info.csv', encoding='utf-8-sig')
