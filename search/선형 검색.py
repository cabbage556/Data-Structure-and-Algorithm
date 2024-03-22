# 정렬된 배열의 선형 검색
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        elif arr[i] > target:
            break

    return None


print(linear_search([3, 17, 75, 80, 202], 75))
print(linear_search([3, 17, 75, 80, 202], 73))
