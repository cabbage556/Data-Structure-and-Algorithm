# 배열에서 최대값을 구하기
#       재귀 함수로 구현
#       시간 복잡도: O(N)
def get_max(arr):
    # 호출 횟수 확인
    print('recursion')

    # 기저 조건
    if len(arr) == 1:
        return arr[0]

    # 재귀 함수 호출 결과를 변수에 저장하기
    #       시간 복잡도를 O(2^N)에서 O(N)으로 줄여주는 효과가 있음
    #       핵심: 한 번 호출한 함수의 결과를 저장하여 다시 호출하지 않음
    max_of_remainder = get_max(arr[1:])

    if arr[0] > max_of_remainder:
        return arr[0]
    else:
        return max_of_remainder


print(get_max([1,2,3,4]))
