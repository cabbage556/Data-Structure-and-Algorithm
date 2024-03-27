# 주어진 문자열에서 x의 개수 세기
# 하향식 재귀
#       이미 함수가 구현되어 있다고 가정하고 하위 문제 찾기
#       하위 문제에 대해 재귀 호출하기
def count_x(string):
    # 기저 조건
    if len(string) == 0:
        return 0

    # 하위 문제: 첫 번째 문자열을 제외한 나머지 문자열
    # 하위 문제에 대해 재귀 호출
    if string[0] == 'x':
        return 1 + count_x(string[1:])
    else:
        return count_x(string[1:])


print(count_x("axbxcxd"))