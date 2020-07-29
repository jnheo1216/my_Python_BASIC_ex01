## 문제 15.
## 각 부품의 생산정보가 문자열로 제공된다.
## [부품생산정보] : A7B5C4A1A8B9B3A5A8B9B1C7C1A1B3C7B9B3A7B8A1C9A8

## 각 부품정보는 부품명과 품질데이터로 구성된다.
## - A,B,C 3개의 부품이 있으며 품질은 1이상 10미만의 정수.
##   예) A7 : A부품, 품질 7

## 생산정보에서 품질이 7이상인 부품만을 순서대로 선택한다.
## [생산정보] A7B5C4A1A8B9B3A5A8B9B1C7C1A1B3C7B9B3A7B8A1C9A8
## [품질이 7이상인 부품 목록] A7A8B9A8B9C7C7B9A7B8C9A8

## 품질이 7이상인 부품들을 조립해 완성품을 만든다.
## A, B, C 세 부품이 순서대로 있을 때만 부품을 조립한다.
## A7A8B9A8B9C7C7B9A7B8C9A8 => A8B9C7, A7B8C9 2개 조립
## 조립한 부품의 목록과 전체 조립한 개수를 출력


def cut_7(list):
    dumylist = []
    for i in range(1, len(list), 2):
        if int(list[i]) > 6:
            dumylist.append(list[i-1])
            dumylist.append(list[i])
        else:
            pass
    return dumylist


def collect_abc(list):
    dumylist = []
    count = 0
    for i in range(4, len(list), 2):
        if list[i] == 'C' and list[i-2] == 'B' and list[i-4] == 'A':
            dumylist.append(list[i-4])
            dumylist.append(list[i-3])
            dumylist.append(list[i-2])
            dumylist.append(list[i-1])
            dumylist.append(list[i])
            dumylist.append(list[i+1])
            count += 1
        else:
            pass
    fin = ''.join(dumylist)
    return (fin, count)


parts_list = 'A7B5C4A1A8B9B3A5A8B9B1C7C1A1B3C7B9B3A7B8A1C9A8'
select_parts_list = cut_7(parts_list)
print(select_parts_list)
col_abc_list = collect_abc(select_parts_list)
print(col_abc_list)
print("생산된 조립부품 : {}".format(col_abc_list[0]), " {}개 생산".format(col_abc_list[1]))