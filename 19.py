## 문제 19.
## 입력으로 제공되는 숫자열에서 짝수와 홀수를 추출하여 새로운 숫자열을 생성한다.
## 1) 입력된 숫자열에서 짝수와 홀수를 순서대로 추출한다.
##    [입력] 78235169
##    [짝수 추출] 826
##    [홀수 추출] 73519
## 2) 추출된 짝수의 뒤에 추출된 홀수를 연결하여 새로운 숫자열을 생성한다.
##    [짝수와 홀수 연결] 82673519

## 결과숫자열을 앞에서부터 순서대로 뺄셈 연산 또는 덧셈 연산 한다.
## 숫자열의 앞에서 부터 순서대로 뺄셈 연산한다.
## 단, 앞선 연산 결과가 0 이하이면 그 차례에는 덧셈 연산한다.
## [결과 숫자열] 82673519
## [각 수의 연산 순서와 방법]
##   8 - 2 = 6
##   6 – 6 = 0
##   0 + 7 = 7 (앞의 연산 결과가 0 이하이므로 덧셈 연산한다.)
##   7 – 3 = 4
##   4 – 5 = -1
##  -1 + 1 = 0 (앞의 연산 결과가 0 이하이므로 덧셈 연산한다.)
##   0 + 9 = 9 (앞의 연산 결과가 0 이하이므로 덧셈 연산한다.)
## [연산 결과] 9

## [입력]: 78235169
## [출력]: 9

## [입력]: 693756874
## [출력]: 7


def div_jjak(list):
    list_jjak = []
    for i in list:
        if int(i) % 2 == 0:
            list_jjak.append(int(i))
        else:
            pass
    return list_jjak


def div_hol(list):
    list_hol = []
    for i in list:
        if int(i) % 2 == 0:
            pass
        else:
            list_hol.append(int(i))
    return list_hol


def lets_do_sum_sub(list):
    tmplist = list
    tmplist.append(0)
    for i in range(0, len(tmplist)-1, 1):
        if tmplist[i] > 0:
            tmplist[i + 1] = tmplist[i] - tmplist[i + 1]
        else:
            tmplist[i + 1] = tmplist[i] + tmplist[i + 1]
    return tmplist[-1]


num = input("숫자 : ")
num_by_str = str(num)
num_by_int = int(num)

num_jjak = div_jjak(num_by_str)
num_hol = div_hol(num_by_str)
print("짝수추출 : ", num_jjak)
print("홀수추출 : ", num_hol)

my_new_list = num_jjak + num_hol
my_cal_result = lets_do_sum_sub(my_new_list)
print("출력 : {}".format(my_cal_result))

# 숫자 : 693756874
# 짝수추출 :  [6, 6, 8, 4]
# 홀수추출 :  [9, 3, 7, 5, 7]
# 출력 : 7
