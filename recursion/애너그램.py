# 문자열의 애너그램을 구해 리스트로 반환하기
#       "abc"의 애너그램: "abc", "acb", "bac", "bca", "cab", "cba"
def anagrams_of(s):
    # 기저 조건
    #       문자열 길이가 1 이하일 때 문자열을 담은 리스트 리턴
    if len(s) <= 1:
        return [s]

    # 문자열의 애너그램 리스트
    result = []

    # 문자열 순회
    for i in range(len(s)):
        first_str = s[i]  # 순회하는 문자열
        remaining_str = s[:i] + s[i+1:]  # 순회하는 문자열을 제외한 문자열
        sub_anagrams = anagrams_of(remaining_str)  # 순회하는 문자열을 제외한 문자열의 애너그램 구하기(서브 애너그램)

        # 서브 애너그램 순회
        for anagram in sub_anagrams:
            # 순회 중인 문자열에 서브 애너그램 문자열 합치기
            result.append(first_str + anagram)

    return result


print(anagrams_of("abc"))
print(sorted(anagrams_of("bca")))

print(anagrams_of("abcd"))
print(sorted(anagrams_of("dcba")))
