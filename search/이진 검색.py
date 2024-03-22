# 정렬된 배열의 이진 검색
def binary_search(arr, target):
    lower = 0
    upper = len(arr) - 1

    while lower <= upper:
        mid = (lower + upper) // 2
        mid_val = arr[mid]

        if target == mid_val:
            return mid
        elif target < mid_val:
            upper = mid - 1
        elif target > mid_val:
            lower = mid + 1

    return None


print(binary_search([3, 17, 75, 80, 202], 80))
print(binary_search([3, 17, 75, 80, 202], 202))
print(binary_search([3, 17, 75, 80, 202], 22))
