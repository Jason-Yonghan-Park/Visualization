######## 방문객 현황 데이터 라인 차트 시각화
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
visitYM = []
visitCnt = []
index = []
i = 0

for item in jsonList:
    # 분기별 데이터 추출
    month = int(item["yearMonth"][-2:])
    # 3으로 나눠서 0일 때(매년 3월씩만 추출)
    if month % 3 == 0:
        index.append(i)
        visitYM.append(item["yearMonth"])
        visitCnt.append(item["monthCount"])
        i += 1

plt.figure(figsize=(18, 8))
plt.grid(True)
plt.plot(index, visitCnt)
plt.xticks(index, visitYM)
plt.xlabel("방문객 수")
plt.ylabel("방문연월")
plt.show()