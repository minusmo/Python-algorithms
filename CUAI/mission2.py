"""
Q2. 주어진 CSV 파일을 불러오고, pandas와 matplotlib 패키지를 사용해 파일의 x, y좌표를 2차원 좌표계에 선그래프로 시각화 하세요.

"""

import csv
import pandas as pds
import matplotlib.pyplot as plt

data = pds.read_csv('data.csv')

plt.plot(data["x"], data["y"])
plt.show()