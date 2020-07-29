## 문제 4.
## 로또 프로그램 작성
## 5000원으로 로또복권을 5장 자동으로 구매합니다.
## 이번 주 로또 당첨번호를 생성하여 로또 당첨을 확인하세요!
## 쉬운버전으로 먼저 작성합니다.
## 6숫자가 다 맞으면 1등, 5개 맞으면 2등으로 처리합니다.
## 즉, 쉬운버전은 보너스 숫자는 없는 것으로 간주합니다.
## 쉬운버전을 해결했다면
## 보너스 숫자를 이용하여 로또 당첨을 확인합니다.
## 보너스 숫자를 제외한 모든 숫자가 다 맞으면 1등,
## 보너스 숫자를 포함하여 6개의 숫자가 맞으면 2등,
## 보너스를 제외하고 5개의 숫자가 맞으면 3등으로 처리합니다.

## 쉬운버전의 출력은 1등 몇개, 2등 몇개, 3등 몇개,
## 4등 몇개, 꽝 몇개로 출력
## 어려운버전의 출력은 1등 몇개, 2등 몇개, 3등 몇개,
## 4등 몇개, 5등 몇개, 꽝 몇개로 출력

## 랜덤값을 도출하기 위해서는 다음의 코드를 이용한다.
import random

i = random.randint(1, 100)  # 1부터 100 사이의 임의의 정수
f = random.random()  # 0부터 1 사이의 임의의 float
i = random.randrange(1, 101, 2)  # 1부터 100 사이의 임의의 짝수
i = random.randrange(10)  # 0부터 9 사이의 임의의 정수

##### 추가문제
##### 1등에 당첨될려면 평균적으로 얼마만큼의 돈을 투자해야 할까요?
##### 로또 1게임은 1000원입니다.


def generate_lotto():
    tmplist = []
    for i in range(0, 7, 1):
        tmplist.append(random.randint(1, 45))
    return tmplist


def easy_lotto_test(list1, list2):
    count = 0
    for j in range(0, 6, 1):
        if list1[j] == list2[j]:
            count += 1
        else:
            pass
    if count == 6:
        print("1등 당첨 ㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷ")
    elif count == 5:
        print("2등 당첨 ㄷㄷㄷㄷㄷㄷㄷ")
    elif count == 4:
        print("3등 당첨 ㄷㄷㄷㄷ")
    elif count == 3:
        print("4등 당첨")
    else:
        print("다음기회에")


def hard_lotto_test(list1, list2, num1, num2):
    count = 0
    bonus_count = 0
    for j in range(0, 6, 1):
        if list1[j] == list2[j]:
            count += 1
        else:
            pass
    if num1 == num2:
        bonus_count += 1
    else:
        pass
    if count == 6:
        print("1등 당첨 ㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷㄷ")
    elif count == 5 and bonus_count == 1:
        print("2등 당첨 ㄷㄷㄷㄷㄷㄷㄷ")
    elif count == 5:
        print("3등 당첨 ㄷㄷㄷㄷ")
    elif count == 4:
        print("4등 당첨")
    else:
        print("다음기회에")


my_lotto_num = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
my_bonus_num = []
for k in range(0, 5, 1):
    my_lotto_num[k] = generate_lotto()
for k in range(0, 5, 1):
    my_bonus_num.append(my_lotto_num[k].pop())
this_week_lotto_num = generate_lotto()
this_week_lotto_num_bonus = this_week_lotto_num.pop()

# 내 로또 5개와 보너스 숫자들 모아놓은 5개짜리 리스트
# 이번주 로또번호와 보너스 번호 생성 함

for l in range(0, 5, 1):
    my_lotto_num[l].sort(reverse=True)
this_week_lotto_num.sort(reverse=True)

for m in range(0, 5, 1):
    easy_lotto_test(my_lotto_num[m], this_week_lotto_num)

print()
print()

for m in range(0, 5, 1):
    hard_lotto_test(my_lotto_num[m], this_week_lotto_num, my_bonus_num[m], this_week_lotto_num_bonus)

# 숫자를 7개 받고 
# 맨 마지막 숫자는 보너스숫자
# 배열의 sort를 하기 전에 따로 빼줘야 함
# 어떻게?
# pop()로 빼내고 그걸 따로 저장?
# 그러면 로또테스트 함수는 2개의 리스트 + 2개의 변수를 받는 함수여야 함
# 서브 함수에서 모든걸 판단하기는 힘들거같음 5가지 경우로 리턴 받아서 
# 메인에서 판단하여 각 몇개인지 판단해주는 게 좋아보임


##############################################################################################


print()
print()

class Lotto(object):
    def __init__(self):
        self.first_num = random.randint(1, 45)
        self.second_num = random.randint(1, 45)
        self.third_num = random.randint(1, 45)
        self.fourth_num = random.randint(1, 45)
        self.fifth_num = random.randint(1, 45)
        self.sixth_num = random.randint(1, 45)
        self.bonus_num = random.randint(1, 45)


    def __repr__(self):
        return str(self.first_num) + " " + str(self.second_num) + " " \
               + str(self.third_num) + " " + str(self.fourth_num) + " " \
               + str(self.fifth_num) + " " + str(self.sixth_num) \
               + " ++ " + str(self.bonus_num)


my_lotto_list = []
for i in range(0, 5, 1):
    my_lotto_list.append(Lotto())

print(my_lotto_list)