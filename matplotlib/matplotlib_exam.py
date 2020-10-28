##### 태어난 도시 - 매년 생일의 온도 시각화
import csv
# 차트 위한 패키지
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

with open("D:\Visualization\matplotlib\seoul_temp.csv", "r", encoding="utf-8") as f:
    csv_read = csv.reader(f)
    # csv 제목 셀 읽어옴
    header = next(csv_read)
    # 온도데이터 저장할 변수 - 평균, 최저, 최고
    mean_temp = []
    min_temp = []
    max_temp = []
    start_year = 1990
    data_year = []

    # 제목셀 다음줄부터 데이터 -> read
    for row in csv_read:
        # 연월일 데이터 -> 연, 월, 일로 구분하여 리스트로 저장
        date = row[0].split("-")
        # 매년 생일날만 추출
        if int(date[0]) >= start_year:
            if date[1] == "04" and date[2] == "06":
                data_year.append(row[0])
                # 기온 문자데이터 -> 실수형 반환
                mean_temp.append(float(row[2]))
                min_temp.append(float(row[3]))
                max_temp.append(float(row[4]))

# 폰트 위치 / 이름 지정
fontLocation = "C:/Windows/fonts/malgun.ttf"
fontName = font_manager.FontProperties(fname=fontLocation).get_name()
rc("font", family=fontName)

# 매 해 생일날 서울 기온 반환하는 메서드
def birthTemp():
    plt.figure(figsize=(12, 9))
    plt.plot(data_year, mean_temp, label="평균 온도")
    plt.plot(data_year, min_temp, label="최저 온도")
    plt.plot(data_year, max_temp, label="최고 온도")
    plt.ylabel("온도")
    plt.xlabel("매해 생일")
    plt.xticks(rotation="45")
    plt.legend(loc=0)
    plt.show()

if __name__ == "__main__":
    birthTemp()