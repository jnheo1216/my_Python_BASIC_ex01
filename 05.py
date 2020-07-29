# 최소공배수
# 1~10까지의 최소공배수는 2520
# 1~20까지는?

from math import gcd

n = input("1부터 몇까지의 숫자로 ? : ")


def maxi(a, b):  # 두 수의 최소공배수
    return a * b // gcd(a, b)


def n_maxi():
    max_var = 1
    for j in range(2, int(n)+1, 1):
        max_var = maxi(max_var, j)
    return max_var


n_result = n_maxi()

print("1 ~ {} 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수 : ".format(n), end=" ")
print(n_result)
# 232792560?
