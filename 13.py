## 문제 13.
## 6자리 이상 9자리 미만의 수를 입력으로 사용합니다.

## 수의 중앙을 기준으로 두 개의 수로 분리한 후 큰 수를 선택한다.
## - 수의 숫자개수가 홀수 개인 경우 수의 중앙 숫자를 기준으로
##   왼쪽과 오른쪽 수로 분리
## - 수의 숫자개수가 짝수 개인 경우 수를 반으로 나누어
##   왼쪽과 오른쪽 수로 분리
## 예1) 1234567 -> (123, 567) -> (567)
## 예2) 34217869 -> (3421, 7869) ->(7869)

## 입력으로 제공된 수를 더 이상 두 개의 수로 분리할 수 없을 때까지
## 과정을 반복하여 남은 최종 숫자를 구해 출력한다.
## 예1) 567 -> (5, 7) -> (7)
## 예2) 7869 -> (78, 69) -> (78) -> (7, 8) -> (8)


def compare(list):
    if list[0] > list[1]:
        return list[0]
    else:
        return list[1]


def cut_number(x):
    tmp = len(str(x))
    x_str = str(x)
    tmp_list = []
    for i in range(0, tmp, 1):
        tmp_list.append(int(x_str[i]))
    if tmp == 2:
        a = tmp_list[0]
        b = tmp_list[1]
    elif tmp == 3:
        a = tmp_list[0]
        b = tmp_list[2]
    elif tmp == 4:
        a = 10 * tmp_list[0] + tmp_list[1]
        b = 10 * tmp_list[2] + tmp_list[3]
    elif tmp == 5:
        a = 10 * tmp_list[0] + tmp_list[1]
        b = 10 * tmp_list[3] + tmp_list[4]
    elif tmp == 6:
        a = 100 * tmp_list[0] + 10 * tmp_list[1] + tmp_list[2]
        b = 100 * tmp_list[3] + 10 * tmp_list[4] + tmp_list[5]
    elif tmp == 7:
        a = 100 * tmp_list[0] + 10 * tmp_list[1] + tmp_list[2]
        b = 100 * tmp_list[4] + 10 * tmp_list[5] + tmp_list[6]
    elif tmp == 8:
        a = 1000 * tmp_list[0] + 100 * tmp_list[1] + 10 * tmp_list[2] + tmp_list[3]
        b = 1000 * tmp_list[4] + 100 * tmp_list[5] + 10 * tmp_list[6] + tmp_list[7]
    else:
        pass
    if a > b:
        return a
    else:
        return b

num = input("6자리 이상 9자리 미만 수 입력 :  ")

len_num = len(str(num))

print(num)
while len_num > 1.5:
   num = cut_number(num)
   print(num)
   len_num = len(str(num))




