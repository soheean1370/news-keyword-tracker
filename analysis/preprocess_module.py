# 전처리, 불용어 제거 함수


import re
from konlpy.tag import Okt

okt = Okt()

def preprocess_text(text):
    text = text.lower()  # 1. 소문자화
    text = re.sub(r'[^\w\s가-힣]','',text)  # 2. 특수문자 제거: 영문자, 숫자, 공백, 한글을 제외한 모든 문자 제거 
    
    tokens = okt.morphs(text)  # 3. 명사 추출 (예: GPT, AI 등 유지)


    return tokens

def remove_stopwords(token_list, stopwords):
    """
    불용어를 제거한 토큰 리스트 반환
    """
    return [token for token in token_list if token not in stopwords]
