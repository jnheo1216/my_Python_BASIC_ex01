## 문제 5.
## 어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고,
## 이 소수들을 그 수의 소인수라고 합니다.
## 예를 들면 13195의 소인수는 5, 7, 13, 29 입니다.

## 600851475143의 소인수 중에서 가장 큰 수를 구하세요.import math




# 그 숫자까지 소수 구함
# 그것들로 그 숫자 나눠봄
# %나머지가 0이면 리스트에 추가해줌
# 리스트 정렬
# 끝

n = input("숫자? : ")
n = int(n)
prime_list = []
count = 0


def is_prime(my_var):  # 소수구하기
    if my_var < 2:
        return False
    for i in range(2, my_var, 1):  # 이거 몰랐음
        if my_var % i == 0:
            return False
    return True


j = 0
for k in range(1, n+1, 1):
    if is_prime(j):  # 참 거짓 잘 쓰는 법
        prime_list.append(j)
    else:
        pass
    j += 1

print(prime_list)


prime_list_in_num = []
for l in prime_list:
    if n % l == 0:
        prime_list_in_num.append(int(l))
    else:
        pass

print(prime_list_in_num)
prime_list_in_num.sort(reverse=True)


print("가장 큰 소인수 : {}".format(prime_list_in_num[0]))
# 아무튼 돌아가긴 함 근데 너무 오래걸림 ㅠㅠ
# 6857