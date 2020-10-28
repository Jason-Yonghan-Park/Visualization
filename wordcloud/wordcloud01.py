######## 워드 클라우드

# 필요한 패키지 임포트
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc

# 워드클라우드 패키지
import pytagcloud
import webbrowser

# json 처리 / 정규표현식 패키지
import json
import re

# bar chart 출력하는 함수
def showBarChart(wordInfo):
    # 한글 폰트 설정
    fontLocation = "C:/Windows/fonts/malgun.ttf"
    fontName = font_manager.FontProperties(fname=fontLocation).get_name()
    rc("font", family = fontName)

    plt.xlabel("주요 단어")
    plt.ylabel("빈도수")

    print(wordInfo.keys())
    sDicKeys = sorted(wordInfo, key=wordInfo.get, reverse=True)
    sDicValues = sorted(wordInfo.values(), reverse=True)
    print(sDicKeys)
    print(sDicValues)
    print(list(wordInfo.values()))

    plt.figure(figsize=(10, 6))
    # color = "C0" ~ "C9"
    # plt.bar(range(len(wordInfo)), sDicValues, color=["C"+str(i) for i in range(10)])
    import seaborn as sns
    sns.barplot(x=list(range(len(wordInfo))), y=sDicValues, palette="Set3")

    plt.xticks(range(len(wordInfo)), sDicKeys, rotation="70")
    plt.show()


# 워드클라우드 이미지로 출력하는 함수
def saveWordCloud(wordInfo, fileName):
    # 워드 클라우드 -> 빈도에 따라 글자의 크기 바뀜
    # value값에 따라 글자 크기, 색상 생성
    taglist = pytagcloud.make_tags(wordInfo.items(), maxsize=100)

    # 변환된 데이터를 이용하여 워드클라우드 이미지로 생성
    pytagcloud.create_tag_image(taglist, fileName, size=(720, 480), fontname="korean")

    webbrowser.open(fileName)

# 모듈 최상위 -> 실행
if __name__ == "__main__":

    # 데이터 파일 읽기
    openFileName = "D:\Visualization\wordcloud\kbsnews_words.json"
    cloudImagePath = openFileName + ".jpg"

    readFile = open(openFileName, "r", encoding="utf-8").read()
    # 읽어온 데이터 -> 문자열 -> 파이썬 자료구조 변환
    jsonData = json.loads(readFile)
    print(jsonData)

    # 워드클라우드 생성 위한 기사 내용 추출
    message = ""
    for item in jsonData:
        if "message" in item.keys():
            # dict list 내의 message키의 value값 중 일반 문자열이 아닌 문자들(특수 문자 등)을 공백으로 치환
            message = message + re.sub(r"[^\w]", "", item["message"])

    print(message)

    # 한글 품사를 다루는 클래스 - Okt, Kkma, Hannanum
    nlp = Okt()

    # 전처리한 문자열에서 명사만 추출
    nouns = nlp.nouns(message)
    print(nouns)

    # 추출한 명사 빈도 구함
    count = Counter(nouns)
    print(count)

    # 빈도 높은 명사 및 빈도만 따로 저장할 dict
    wordInfo = dict()

    for tags, counts in count.most_common(50):
        # 단어의 길이가 2 이상인 것만 추출
        if len(str(tags)) >= 2:
            wordInfo[tags] = counts
            print("{} : {}".format(tags, counts))

    print(wordInfo)

    # bar차트 출력
    showBarChart(wordInfo)

    # 워드 클라우드 생성하고 이미지 저장한 후 화면에 출력
    saveWordCloud(wordInfo, cloudImagePath)





