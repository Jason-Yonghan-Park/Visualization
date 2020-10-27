######## 방문객 현황 데이터 히트맵 시각화
# json 데이터 다루기 위한 패키지
import json
# 차트 위한 패키지
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 읽을 파일
openFileName = "D:\Visualization\matplotlib\미국인_방문객현황_2013_2019.json"

# 폰트 위치 / 이름 지정
fontLocation = "C:/Windows/fonts/malgun.ttf"
fontName = font_manager.FontProperties(fname=fontLocation).get_name()
rc("font", family=fontName)

# 파일 데이터 읽어와 저장할 변수
jsonList = []
# 파일 읽음
with open(openFileName, "r", encoding="utf-8") as openFile:
    # 파일 객체 통해 파일 내용 읽기
    readData = openFile.read()
    # 읽어온 데이터 -> 파이썬 자료구조로 변경
    jsonList = json.loads(readData)

print(jsonList)

# plt.plot(x, y, 옵션)
visitYear = []
visitMonth = []
visitCnt = []

for item in jsonList:

    # 각 연/월, 방문객수 추출 후 리스트에 저장장
    visitYear.append(item["yearMonth"][:4])
    visitMonth.append(item["yearMonth"][-2:])
    visitCnt.append(item["monthCount"])

# 편집한 자료 -> DataFrame 객체
import pandas as pd
df = pd.DataFrame({"연도":visitYear, "월":visitMonth, "방문객 수":visitCnt})
print(df)
df_pivot = df.pivot_table(index="연도", columns="월", values="방문객 수")
print(df_pivot)

# 히트맵 출력하기 위한 라이브러리 임포트
import seaborn as sns

plt.figure(figsize=(14, 6))
plt.title("미국인 방문객 현황 히트맵")

# 히트맵 그래프 설정
sns.heatmap(df_pivot, annot=True, fmt=".0f", cmap="rocket_r")

plt.show()

"""
plt.figure(figsize=(18, 8))
plt.grid(True)
plt.plot(index, visitCnt)
plt.xticks(index, visitYM)
plt.xlabel("방문객 수")
plt.ylabel("방문연월")
plt.show()
"""

