# 정수 배열에서 빠진 숫자를 찾기
#       0부터 배열 길이만큼의 모든 정수를 포함해야 하는데, 숫자가 하나 빠져 있음
#       정렬을 사용해 O(NlogN) 시간 복잡도로 구현하기
def find_missing_number(arr):
    arr.sort()

    for i in range(len(arr)):
        if i != arr[i]:
            return i

    return None


print(find_missing_number([0, 1, 2, 4, 5, 6, 7]))
print(find_missing_number([0, 1, 2, 3, 5, 6, 7]))
