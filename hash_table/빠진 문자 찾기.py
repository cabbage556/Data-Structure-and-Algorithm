# 알파벳 문자를 한 글자만 제외하고 모두 포함하는 문자열을 입력 받아 빠진 문자 하나를 반환하는 함수
def get_one_missing_alphabet(input_str):
    hash_table = dict()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for s in input_str:
        if s != " ":
            hash_table[s] = True

    for s in alphabet:
        val = hash_table.get(s, None)
        if val is None:
            return s

    return None

print(get_one_missing_alphabet("the quick brown box jumps over a lazy dog"))
print(get_one_missing_alphabet("abcdefghijklmnopqrstuvwxyz"))
