# 배열에서 최대값을 구하기
#       재귀 함수로 구현
#       시간 복잡도: O(2^N)
#           함수 호출마다 2번 재귀 호출(하위 문제 중첩)
def get_max(arr):
    # 호출 횟수 확인
    print('recursion')

    # 기저 조건
    if len(arr) == 1:
        return arr[0]

    if arr[0] > get_max(arr[1:]):  # 첫 번째 재귀 호출
        return arr[0]
    else:
        return get_max(arr[1:])  # 두 번째 재귀 호출: 첫 번째 재귀 호출의 결과와 동일함(하위 문제 중첩)


print(get_max([1,2,3,4]))