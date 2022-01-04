# 선형 회귀 실습

import numpy as np

x = [2, 4, 6, 8]
y = [81, 93, 91, 97]

# x 와 y의 평균값
mx = np.mean(x)
my = np.mean(y)
print("x와 y의 평균값: ",mx , my)

# 기울기 공식의 분모
divisor = sum([(mx - i) ** 2 for i in x])

#기울기 공식의 분자
def top(x, mx, y, my):
    d = 0
    for i in range(len(x)):
        d += (x[i] - mx) * (y[i] - my)
    return d
dividend = top(x, mx, y, my)

print("분모, 분자: ", divisor, dividend)

# 기울기와 y절편 구하기
a = dividend / divisor
b = my - (mx * a)
print(" 기울기 a, y 절편 b: ", a, b)
