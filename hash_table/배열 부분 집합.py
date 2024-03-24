# 두 배열이 부분 집합인지 확인하는 함수
def is_subset(arr1, arr2):
    larger_arr = None
    smaller_arr = None
    hash_table = dict()

    if len(arr1) > len(arr2):
        larger_arr = arr1
        smaller_arr = arr2
    else:
        larger_arr = arr2
        smaller_arr = arr1

    for el in larger_arr:
        hash_table[el] = True

    for el in smaller_arr:
        val = hash_table.get(el, None)
        if val is None:
            return False

    return True


print(is_subset([1, 2, 3], [2, 3]))
print(is_subset([1, 2, 3], [2, 4]))
print(is_subset([2, 3], [2, 3, 4]))
print(is_subset([1, 2], [2, 3, 4]))
