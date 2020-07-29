
import itertools

pool = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
my_soon = list(map(''.join, itertools.permutations(pool))) # 3개의 원소로 수열 만들기
#print(len(my_soon))
s_my_soon = sorted(my_soon)
print('순열의 1000000째 숫자 : ', s_my_soon[999999])
#2783915460