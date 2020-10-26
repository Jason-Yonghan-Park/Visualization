####### 라인차트 / 산점도
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

# 여러 색상 / 선 스타일 / sin, cos 곡선 출력 함수
def chartLineStyle():
    x = np.linspace(0, 10, 1000)
    plt.plot(x, np.sin(x - 0), color= "blue", linestyle= "solid", linewidth= 3, label= "solid")
    plt.plot(x, np.sin(x - 1), color="g", linestyle="dashed", lw=3, label="dashed")
    plt.plot(x, np.sin(x - 2), color="0.75", linestyle="dotted", lw=3, label="dotted")
    plt.plot(x, np.sin(x - 3), color="#FFDD44", linestyle="solid", label="solid")
    plt.plot(x, np.sin(x - 4), color=(1.0, 0.2, 0.3), linestyle="-.", lw=3, label="point dashed")
    plt.plot(x, np.sin(x - 5), "-g", linestyle="-", lw=4, label="solid green")
    plt.axis([0, 10, -1.5, 1.5])
    plt.legend(loc= "upper center", fancybox= True, shadow= True, ncol= 3, bbox_to_anchor=(0.01, 1.30, 0.98, -0.2))
    plt.show()

# 산점도 출력 함수
def scatterChart(x_data, y_data):
    pass

# 계단형 라인 차트 함수
def multiLineChart():
    pass

# 다양한 사이즈 산점도 출력 함수
def multiSizeScatter():
    pass

if __name__ == "__main__":
    chartLineStyle()
    #scatterChart(x_data, y_data)
    #multiLineChart()
    #multiSizeScatter()