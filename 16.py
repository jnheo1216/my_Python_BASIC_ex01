## 문제 16.
## n! 이라는 표기법은 n × (n − 1) × ... × 3 × 2 × 1을 뜻합니다.

## 예를 들자면 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800 이 되는데,
## 여기서 10!의 각 자리수를 더해 보면 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27 입니다.

## 100! 의 자리수를 모두 더하면 얼마입니까?


def get_factorial(x):
    tmp = 1
    for i in range(x, 1, -1):
        tmp = tmp * i
    return tmp


def all_sum(y):
    y = str(y)
    y_list = []
    for j in y:
        y_list.append(int(j))
    return sum(y_list)


num = input("숫자 : ")
fac_num = get_factorial(int(num))
print("{}! = ".format(num), fac_num)
print("모든자릿수 합 : {}".format(all_sum(fac_num)))
# 모든자릿수 합 : 648