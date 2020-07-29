# 피보나치에서 짝수항만 더하기

my_fib_list = [1, 2]

while my_fib_list[-1] < 4000000:
    my_var = my_fib_list[-2] + my_fib_list[-1]
    my_fib_list.append(my_var)


my_fib_list2 = [tmp for tmp in my_fib_list if tmp % 2 == 0]

my_fib_sum = 0
for temp in my_fib_list2:
    my_fib_sum += temp


print("짝수이면서 모든항 더하면 : ", end=" ")
print(my_fib_sum)