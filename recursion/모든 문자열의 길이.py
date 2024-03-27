# 문자열 배열을 받아 모든 문자열 원소의 개수를 더해 반환하기
def get_string_length(arr):
    # 기저 조건
    if len(arr) == 1:
        return len(arr[0])

    # 하위 문제: 첫 번째 원소를 제외한 나머지 배열
    # 하위 문제에 대해 재귀 호출
    return len(arr[0]) + get_string_length(arr[1:])


print(get_string_length(["ab", "c", "def", "ghij"]))