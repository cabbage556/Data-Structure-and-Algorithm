# 배열에서 가장 큰 수를 찾는 함수 세 개를 구현하기
#       하나는 O(N^2), 하나는 O(NlogN), 하나는 O(N)으로 작성

# O(N^2)
def find_max1(arr):
    for i in range(len(arr)):
        i_is_largest = True

        for j in range(len(arr)):
            if arr[i] < arr[j]:
                i_is_largest = False

        if i_is_largest:
            return arr[i]


# O(NlogN)
def find_max2(arr):
    arr.sort()
    return arr[-1]


# O(N)
def find_max3(arr):
    largest = arr[0]
    for i in range(1, len(arr)):
        if largest < arr[i]:
            largest = arr[i]

    return largest


print(find_max1([0, 5, 2, 1, 6, 3]))
print(find_max2([0, 5, 2, 1, 6, 3]))
print(find_max3([0, 5, 2, 1, 6, 3]))
