# prj_modoodoc

프로젝트 진행 순서

-----------------------
데이터 수집
crawling_review.py
crawling_info.py

-----------------------
데이터 병합
데이터 수집량이 많아 여러대의 컴퓨터로 분산처리하여 concat과정 필수
concat_hospital.py 
concat_info.py
concat_hospital_info

-----------------------
데이터 전처리
preprocess_hospitalreview.py
preprocess_concat.py
preprocess_onesentence.py : tfidf를 통한 단어토큰사전 형성 위해

---------------- --------
모델링
tfidf.py : 문서 상 단어빈도가 높고, 그 단어가 포함된 문서가 적을수록 높은 값 => 병원명 기반 검색
word2vec.py : 문맥상 연관된 단어 분석 => 리뷰 키워드 기반 검색
hospital_recommended_system.py: 추천시스템 구현

-------------------------
시각화
wordcloud.py
word2vec_visualization.py
