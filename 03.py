# 문장에 몇개의 알파벳이 있나 누가 제일 많나?

my_alpha_list = "Hello world"
my_alpha_list = input("문장을 넣으세요!! : ")
my_alpha_list = my_alpha_list.lower()

my_a_list_s = 'abcdefghijklmnopqrstuvwxyz'
countAlpha_s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
largest_alp = 0
largest_alp_num = 0


for tmp in range(0, 26, 1):
    countAlpha_s[tmp] = my_alpha_list.count(my_a_list_s[tmp])  # 소문자 개수

largest_alp = countAlpha_s[0]
largest_alp_num = 0

for tmp in range(1, 26, 1):  # 비교 시작
    if largest_alp > countAlpha_s[tmp]:
        largest_alp = largest_alp
        largest_alp_num = largest_alp_num
    elif largest_alp < countAlpha_s[tmp]:
        largest_alp = countAlpha_s[tmp]
        largest_alp_num = tmp
    else:
        pass


print("가장 많은 알파벳 : ", end=" ")
print(my_a_list_s[largest_alp_num])

print("개수 : ", end=" ")
print(largest_alp)











