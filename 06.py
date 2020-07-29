# 소수 구하기
# 100001번째 소수?
n = input("몇번째 소수를 알고싶나요? : ")
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
while count < n:
    if is_prime(j):  # 참 거짓 잘 쓰는 법
        prime_list.append(j)
        count += 1
    else:
        pass
    j += 1


print("{}번째 소수 : ".format(n), end=" ")
print(prime_list[-1])
# 104743?