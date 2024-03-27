# 배열의 모든 원소의 합 구하기
# 하향식 재귀
#       이미 함수가 구현되어 있다고 가정하고 하위 문제 찾기
#       하위 문제에 대해 재귀 호출하기
def sum_array(arr):
    # 기저 조건
    if len(arr) == 1:
        return arr[0]

    # 하위 문제: 첫 번째 원소를 제외한 나머지 배열
    # 하위 문제에 대해 재귀 호출
    return arr[0] + sum_array(arr[1:])


print(sum_array([1, 2, 3, 4, 5]))