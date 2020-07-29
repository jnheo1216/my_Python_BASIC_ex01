print("hello world!!")

# 문제1

my_list = []
my_list_sum = 0

for temp in range(1, 10, 1):
    if temp % 3 == 0:
        my_list.append(temp)
        my_list_sum += temp
    elif temp % 5 == 0:
        my_list.append(temp)
        my_list_sum += temp
    else:
        pass
print("10보다 작은 자연수중에서 3또는 5의 배수는")
print(my_list, end=" ")
print("가 존재해요! 이것들의 합은 {}입니다.".format(my_list_sum))

my_list_sum = 0
for temp in range(1, 1000, 1):
    if temp % 3 == 0:
        my_list.append(temp)
        my_list_sum += temp
    elif temp % 5 == 0:
        my_list.append(temp)
        my_list_sum += temp
    else:
        pass

print("1000으로 했을 때 합은 {}입니다.".format(my_list_sum))