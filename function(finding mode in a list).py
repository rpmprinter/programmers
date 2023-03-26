#리스트의 최빈값을 구하는 함수

def solution(array):
    count_array = dict()
    count_array_list = list()
    for i in set(array):
        count_array[i] = array.count(i)
    for i in set(array):
        count_array_list.append(array.count(i))
    count_array_list.sort()

    if len(count_array_list) == 1:
        return array[0]
    elif count_array_list[-1] == count_array_list[-2]:
        return -1
    else:
        max_value = count_array_list[-1]
        for key, value in count_array.items():
            if value == max_value:
                return key
            else:
                continue
