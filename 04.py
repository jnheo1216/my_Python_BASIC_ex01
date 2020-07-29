## 문제 4.
## 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이
## 같은 수를 대칭수(palindrome)라고 부릅니다.

## 두 자리 수를 곱해 만들 수 있는 대칭수 중
## 가장 큰 수는 9009 (= 91 × 99) 입니다.

## 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수를 구하세요

dub_list = []

def judg_6(n):
    i = str(n)
    if i[0] == i[5] and i[1] == i[4] and i[2] == i[3]:
        # print("{}은 대칭수 맞다!".format(n))
        return True
    else:
        # print("{}은 대칭수 아니다".format(n))
        return False


for j in range(400, 1000, 1):
    for k in range(400, 1000, 1):
        big_num = j * k
        if judg_6(big_num):
            dub_list.append(big_num)
        else:
            pass

dub_list.sort()
print("6자리로 나오는 대칭수중에 가장 큰거 : ", end=" ")
print(dub_list[-1])