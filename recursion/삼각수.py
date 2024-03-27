# 삼각수에서 n번째 값 구하기
#       삼각수: n번째 값이 n 바로 앞 숫자를 더한 값인 수열
#       1, 3, 6, 10, 15, 21, 28, ...
def get_triangular_number(n):
    # 기저 조건
    if n == 1:
        return 1

    # 하위 문제: n - 1
    # 하위 문제에 대해 재귀 호출
    return n + get_triangular_number(n - 1)


print(get_triangular_number(7))