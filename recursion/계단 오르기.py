# 주어진 계단 수를 오를 수 있는 모든 경로의 개수 구하기
#       한 번에 오를 수 있는 계단 수: 1, 2, 3
def number_of_paths1(n):
    # 기저 조건 하드코딩
    if n <= 0:
        return 0
    if n == 1:      # n - 1 계단에서 오를 수 있는 경로 수: 1
        return 1
    if n == 2:      # n - 2 계단에서 오를 수 있는 경로 수: 2
        return 2
    if n == 3:      # n - 3 계단에서 오를 수 있는 경로 수: 3
        return 4

    # 하위 문제1: 1 계단 전까지의 경로 수
    # 하위 문제2: 2 계단 전까지의 경로 수
    # 하위 문제3: 3 계단 전까지의 경로 수
    # 하위 문제에 대해 재귀 호출
    return number_of_paths1(n - 1) + number_of_paths1(n - 2) + number_of_paths1(n - 3)


def number_of_paths2(n):
    # 기저 조건
    #       n - 2 계단에서 오를 수 있는 경로의 수가 2가 되도록 기저 조건 설정
    if n < 0:
        return 0
    if n == 1 or n == 0:
        return 1

    # 하위 문제에 대해 재귀 호출
    return number_of_paths2(n - 1) + number_of_paths2(n - 2) + number_of_paths2(n - 3)


print(number_of_paths1(5))
print(number_of_paths2(5))
