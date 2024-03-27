# 수 배열을 받아 짝수만 포함하는 새 배열을 반환하기
def select_even(arr):
    # 기저 조건
    if len(arr) == 0:
        return []

    # 하위 문제: 첫 번째 원소를 제외한 나머지 배열
    # 하위 문제에 대해 재귀 호출
    if arr[0] % 2 == 0:
        return [arr[0]] + select_even(arr[1:])
    else:
        return select_even(arr[1:])


print(select_even([1,2,3,4,5]))