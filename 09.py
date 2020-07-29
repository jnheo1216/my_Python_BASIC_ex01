## 문제 8.
## 1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같습니다 (제곱의 합).
## 1**2 + 2**2 + ... + 10**2 = 385

## 1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같습니다 (합의 제곱).
## (1 + 2 + ... + 10)**2 = 552 = 3025

## 따라서 1부터 10까지 자연수에 대해 "합의 제곱"과 "제곱의 합" 의
## 차이는 3025 - 385 = 2640 이 됩니다.

## 그러면 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는
## 얼마입니까?


def sum_square(x):
    tmp = 0
    for i in range(1, x+1, 1):
        tmp = tmp + i
    return tmp * tmp


def square_sum(y):
    tmp = 0
    for j in range(1, y+1, 1):
        tmp = tmp + j * j
    return tmp


num = input("숫자 : ")
num = int(num)
ssq = sum_square(num)
sqs = square_sum(num)
print("합의제곱 : {}".format(ssq))
print("제곱의합 : {}".format(sqs))
print("합의제곱 - 제곱의합 : {}".format(ssq-sqs))

# 숫자 : 100
# 합의제곱 : 25502500
# 제곱의합 : 338350
# 합의제곱 - 제곱의합 : 25164150