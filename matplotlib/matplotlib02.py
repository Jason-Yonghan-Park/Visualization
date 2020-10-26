###### 바차트 / 하나의 차트 화면에 여러 차트 그리기
import matplotlib.pyplot as plt
import numpy as np

# 한글 폰드 리소스 관리를 위한 font_manager
from matplotlib import font_manager, rc

fontLocation = "C:/Windows/fonts/malgun.ttf"
fontName = font_manager.FontProperties(fname=fontLocation).get_name()
print("fontName: ", fontName)
rc("font", family=fontName)

def scoreBarChart(names, score):
    plt.bar(names, score)
    plt.show()

def multiChart(names, score):
    plt.plot(names, score, "ro--")
    plt.xlabel("이름")
    plt.ylabel("점수")
    plt.title("국어 점수")
    plt.plot([1, 2, 3], [50, 60, 70], "bo:")
    plt.plot([1, 1, 1], [10, 20, 30], "r>--", [4, 4, 4], [40, 50, 60], "y*-.")
    plt.text(3, 96, "평균: {}".format(np.mean(score)))
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    names = ["홍길동", "이순신", "강감찬", "김유신", "임꺽정"]
    score = [89, 86, 97, 77, 92]
    #scoreBarChart(names, score)
    multiChart(names, score)