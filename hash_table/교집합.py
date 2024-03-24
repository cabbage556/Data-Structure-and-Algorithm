# 두 배열의 교집합을 구해 배열로 반환하는 함수
def get_intersection(arr1, arr2):
    hash_table = dict()
    intersection_arr = []

    for val in arr1:
        hash_table[val] = True

    for val in arr2:
        if hash_table[val]:
            intersection_arr.append(val)

    return intersection_arr


print(get_intersection([1, 2, 3, 4], [2, 3]))