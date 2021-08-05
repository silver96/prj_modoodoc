# prj_modoodoc

프로젝트 진행 순서

1. 데이터 수집

crawling_review.py : 병원카테고리, 병원명, 리뷰만 추출

crawling_info.py : 추천시스템 구현시 사용자편의 증대 위해 부가적인 정보 추출

2. 데이터 병합

데이터 수집량이 많아 여러대의 컴퓨터로 분산처리하여 concat과정 필수

concat_hospital.py 

concat_info.py

concat_hospital_info

3. 데이터 전처리

preprocess_hospitalreview.py

preprocess_concat.py

preprocess_onesentence.py : tfidf를 통한 단어토큰사전 형성 위해

4. 모델링

병원이름 + 리뷰 + 진료과목

tfidf.py : 문서 상 단어빈도가 높고, 그 단어가 포함된 문서가 적을수록 높은 값 => 병원명 기반 검색

word2vec.py : 문맥상 연관된 단어 분석 => 리뷰 키워드 기반 검색

hospital_recommended_system.py: 추천시스템 구현

5. 시각화

wordcloud.py : 불용어리스트 추출, 전반적인 리뷰품질 보는데 효과적

word2vec_visualization.py
