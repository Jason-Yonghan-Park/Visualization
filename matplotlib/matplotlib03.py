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
    plt.scatter(x_data, y_data, c="steelblue", edgecolors="dodgerblue")
    #plt.plot(x_data, y_data, "bo", markeredgecolor= "r")
    plt.show()

# 계단형 라인 차트 함수
def multiLineChart():
    data1 = np.random.randn(50)
    data2 = np.random.randn(50)

    plt.plot(data1, color="r", label="step", drawstyle="steps")
    plt.plot(data2, color="g", label="line")

# 다양한 사이즈 산점도 출력 함수
def multiSizeScatter():
    rng = np.random.RandomState(0)
    x = rng.randn(100)
    y = rng.randn(100)
    colors = rng.rand(100)
    sizes = rng.rand(100)*1000

    plt.scatter(x, y, s = sizes, c = colors, alpha=0.5)
    plt.colorbar()
    plt.show()

# 산점도 데이터 준비
point_list = []
for i in range(100):
    x = np.random.normal(0, 1) # 표준정규분포
    y = x * 0.1 + 0.2 + np.random.normal(0, 1)
    point_list.append([x, y])

x_data = [x[0] for x in point_list]
y_data = [y[1] for y in point_list]
print(x_data)
print(y_data)

if __name__ == "__main__":
    #chartLineStyle()
    #scatterChart(x_data, y_data)
    #multiLineChart()
    multiSizeScatter()