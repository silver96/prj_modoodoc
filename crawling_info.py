import pandas as pd
import requests
import re
import time

categories = ['치과', '피부과', '성형외과', '안과', '산부인과', '비뇨기과', '정신건강의학과', '정형외과', '마취통증의학과',
              '신경외과', '재활의학과', '영상의학과', '외과', '신경과', '소아과', '내과', '이비인후과', '가정의학과', '한의원']

#categories.reverse()
print(categories)


print("시작")
for j in categories:
    print(j, '시작')
    links = []
    for i in range(1, 101):  # 페이지
        url2 = f'https://www.modoodoc.com/hospitals/?search_query={j}/&page={i}'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
        html = requests.get(url2, headers=headers).text
        soup = BeautifulSoup(html, 'lxml')
        hos_link = soup.select('div.doctor-total-box.border-bottom > a')  # .get('href')

        for hos in hos_link:
            try:
                link = hos.get('href')
                links.append(link)
            except:
                pass
        if i % 10 == 0:
            print(',', end='')
    name_info = []
    rank_info = []
    add_info = []
    link_info = []
    tel_info = []

    for k in range(len(links)):  # 링크
        if k % 20 == 0:
            print('.', end='')
        url3 = 'https://www.modoodoc.com' + links[k]
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
        html = requests.get(url3, headers=headers).text
        soup = BeautifulSoup(html, 'lxml')

        ranks = []
        keywords = soup.select('div.pb-2.text-left.my-3 > div.m-1.p-1 > a')
        for key in keywords:
            key = key.text.split(' (')[0]  # ( 이후 삭제
            ranks.append(key)

        # print(ranks)
        try:
            name = soup.select_one('div.hospital-doctor-name-box.d-flex.align-items-center').text.strip()
            add = soup.select_one('div.color49.mt-3').text.strip()
            link = soup.select_one('a.website-link-click').get('href')
            tel = soup.select_one('div.color49.mt-2').text.strip()
        except:
            continue
        name_info.append(name)
        rank_info.append(ranks)
        add_info.append(add)
        link_info.append(link)
        tel_info.append(tel)

    df_review = pd.DataFrame(
        {'names': name_info, 'rank': rank_info, 'address': add_info, 'link': link_info, 'telephone': tel_info})
    df_review.to_csv(f'reviews_Hospital_{j}_page.csv')
    print(j, '완료')
