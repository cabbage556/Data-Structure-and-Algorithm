# 주어진 문자열을 뒤집기
# 하향식 재귀
#       이미 함수가 구현되어 있다고 가정하고 하위 문제 찾기
#       하위 문제에 대해 재귀 호출하기
def reverse(string):
    # 기저 조건
    if len(string) == 1:
        return string

    # 하위 문제: 첫 번째 문자열을 제외한 나머지 문자열
    # 하위 문제에 대해 재귀 호출
    return reverse(string[1:]) + string[0]


print(reverse("abcde"))