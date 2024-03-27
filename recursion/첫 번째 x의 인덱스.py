# 문자열을 받아 문자 'x'가 들어간 첫 번째 인덱스를 반환하기
def get_first_x_index(s):
    # 기저 조건
    if s[0] == 'x':
        return 0

    # 하위 문제: 첫 번째 문자열을 제외한 나머지 문자열
    # 하위 문제에 대해 재귀 호출
    return 1 + get_first_x_index(s[1:])


print(get_first_x_index("abcxdd"))
print(get_first_x_index("abcddx"))
