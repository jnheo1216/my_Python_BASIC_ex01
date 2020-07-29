## 문제 14.
## 2**15 = 32768 의 각 자리수를 더하면 3 + 2 + 7 + 6 + 8 = 26 입니다.

## 2**1000의 각 자리수를 모두 더하면 얼마입니까?

num = 2**1000
num = str(num)
num_list = []

for i in num:
    num_list.append(int(i))

print(sum(num_list))
#1366







