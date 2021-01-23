import sys
import os
import collections
# 이와 같이 모듈을 1개씩 import 하는 것이 convention이다.
print(sys.argv) # 터미널에 입력되는 인수를 사용할 수 있게합니다. (배열로)
print(collections.__file__)
print(os.__file__) # 각 모듈의 위치를 출력한다.
print(sys.path) # python의 evironment path를 출력한다.