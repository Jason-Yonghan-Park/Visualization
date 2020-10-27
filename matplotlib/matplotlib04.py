###### 차트 캔버스 설정 / 한 캔버스에 여러 차트 출력
import matplotlib.pyplot as plt
import numpy as np

# 2행 1열짜리 캔버스
def plot_2_1():
    # 캔버스 생성
    plt.figure(figsize=(4, 10))

    # subplot 생성 (행, 열, 위치)
    plt.subplot(2, 1, 1) # 첫번째
    plt.plot([2, 4, 6, 8], [1, 3, 5, 7], "g>-")
    plt.subplot(2, 1, 2) # 두번째
    plt.plot([20, 40, 60, 80], [-10, -20, -30, -40], "r<-.")

    plt.show()

# matplotlib03.py 에서 데이터 가지고 옴
from matplotlib03 import x_data, y_data

# 2행 2열짜리 캔버스
def plot_2_2():
    # 캔버스 생성
    fig = plt.figure()
    # subplot 생성 2행2열
    s1 = fig.add_subplot(2, 2, 1)
    s2 = fig.add_subplot(2, 2, 2)
    s3 = fig.add_subplot(2, 2, 3)
    s4 = fig.add_subplot(2, 2, 4)

    data = np.random.randint(1, 100, 100)

    # s1 -> 히스토그램
    s1.hist(data)
    # s2 -> 산점도
    s2.scatter(x_data, y_data)
    # s3 -> 선그래프
    s3.plot(np.arange(50), "-.")
    # s4 -> 꺾은선
    s4.plot(np.random.rand(100), "r--")

    plt.show()

if __name__ == "__main__":
    #plot_2_1()
    plot_2_2()