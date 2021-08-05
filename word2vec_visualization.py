import pandas as pd
import matplotlib.pyplot as mpl
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

font_path = './visualization/malgun.ttf'
font_name = font_manager.FontProperties(
    fname=font_path).get_name()
mpl.rcParams['axes.unicode_minus'] = False
rc('font',family=font_name)

embedding_model = Word2Vec.load('./models/word2VecModel_hospital_l2.model')
key_word='신경치료'
sim_word = embedding_model.wv.most_similar(key_word, topn=10)
print(sim_word)

#차원을 축소시켜 2차원에 표시
vectors = []
labels = []
for label, _ in sim_word:
    labels.append(label)
    vectors.append(embedding_model.wv[label])
df_vectors = pd.DataFrame(vectors)
print(df_vectors.head())

tsne_model = TSNE(perplexity=40, n_components=2,
                  init='pca', n_iter=2500, random_state=23) #TSNE 이용해서 2차원 공간에 투시
new_values = tsne_model.fit_transform(df_vectors)
df_xy = pd.DataFrame({'words':labels,
                      'x':new_values[:,0],
                      'y':new_values[:,1]})
print(df_xy.head())

print(df_xy.shape)
df_xy.loc[df_xy.shape[0]] = (key_word, 0,0)
plt.figure(figsize=(8,8))
plt.scatter(0,0,s=1500, marker='*') #plt.scatter(x,y, s=마커 크기 값(또는 배열), c=마커 색 값(또는 배열))
for i in range(len(df_xy.x)):
    a = df_xy.loc[[i,10], :]
    plt.plot(a.x, a.y, '-D', linewidth=2)
    plt.annotate(df_xy.words[i], xytext=(5,2),#xytext: text가 위치할 지점
                 xy=(df_xy.x[i],df_xy.y[i]),
                 textcoords='offset points',
                 ha='right', va='bottom') #va='bottom': 글씨 크기가 다를 때 정렬 기준
plt.show()
