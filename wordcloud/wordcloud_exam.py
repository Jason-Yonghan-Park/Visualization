##### 코로나19 웹스크레이핑 파일 워드클라우드

# 필요한 패키지 임포트
from konlpy.tag import Okt
from collections import Counter
import pytagcloud
import webbrowser
import json
import re

# 워드 클라우드 이미지로 출력하는 함수
def printWordCloud(wordInfo, fileName):
    # 글자 빈도 따라 글자 색상, 크기 바뀜
    taglist = pytagcloud.make_tags(wordInfo.items(), maxsize=100)
    # 변환된 데이터를 이용 -> 워드클라우드 이미지 생성
    pytagcloud.create_tag_image(taglist, fileName, size=(720, 480), fontname="korean")

    webbrowser.open(fileName)

# 메인 시작
if __name__ == "__main__":
    # 데이터 파일 읽음
    openFileName = "D:\Visualization\wordcloud\코로나19_naver_news.json"
    cloudImagePath = openFileName + ".jpg"
    readFile = open(openFileName, "r", encoding="utf-8").read()
    # 읽어온 데이터 -> 문자열 -> 파이썬 자료 구조로 변환
    jsonData = json.loads(readFile)

    # 워드 클라우드 생성 위한 기사 내용 추출
    description = ""
    for item in jsonData:
        if "description" in item.keys():
            # jsonData 내 description키의 value중 일반 문자열 제외 제거
            description = description + re.sub(r"[^\w]", "", item["description"])

    # 한글 품사 클래스
    nlp = Okt()

    # 전처리한 문자열에서 한글 명사만 추출
    nouns = nlp.nouns(description)
    print(nouns)

    # 명사 빈도 구함
    count = Counter(nouns)
    print(count)

    # 빈도 높은 명사 + 빈도수 저장
    wordInfo = dict()

    for tags, counts in count.most_common(50):
        # 단어 길이 2자 이상만 추출
        if len(str(tags)) >= 2:
            wordInfo[tags] = counts

    printWordCloud(wordInfo, cloudImagePath)
