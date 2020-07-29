## 문제 11.
## 양의 정수 n에 대하여, 다음과 같은 계산 과정을 반복하기로 합니다.

## n → n / 2 (n이 짝수일 때)
## n → 3 * n + 1 (n이 홀수일 때)

## 13에 대하여 위의 규칙을 적용해보면 아래처럼 9번의 과정을 통해 1이 됩니다.

## 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

## 아직 증명은 되지 않았지만, 이런 과정을 거치면 어떤 수로 시작해도
## 마지막에는 1로 끝나리라 생각됩니다.
## (이런 수들을 우박수 hailstone sequence라 합니다.)

## 그러면, 백만(1,000,000) 이하의 수로 시작했을 때 1까지 도달하는데
## 가장 긴 과정을 거치는 숫자는 얼마입니까?
## 계산 과정 도중에는 숫자가 백만을 넘어가도 괜찮습니다.


def calcul(my_int):
    if my_int % 2 == 0:
        return my_int / 2
    else:
        return my_int * 3 + 1


list_to_mil = [(1, 3)]
winner = [0, 0]

# for i in range(2, 1001, 1):  # 숫자크면 힘들어함;;
#     count = 1
#     tmp = i
#     while tmp > 2:
#         tmp = calcul(tmp)
#         count += 1
#     list_to_mil.append((i, count))

for i in range(2, 1000001, 1):
    count = 1
    tmp = i
    while tmp > 2:
        tmp = calcul(tmp)
        count += 1
    if count > winner[1]:
        winner[1] = count
        winner[0] = i
    else:
        pass


# print(list_to_mil)

s_list_to_mil = reversed(sorted(list_to_mil, key=lambda t : t[1]))

# print(s_list_to_mil)

# cnt = 1
# for k in s_list_to_mil:
#     print("{}위 : {} , {}번".format(cnt, k[0], k[1]))
#     cnt += 1

print("제일 많이 실행해야하는수 : {}, ".format(winner[0]), end=" ")
print(" {}번".format(winner[1]))
# print(s_list_to_mil[0])

# 제일 많이 실행해야하는수 : 837799,   524번