# 문자열에서 첫 번째로 중복되지 않는 문자를 반환하는 함수
def get_only_one_first_char(input_str):
    hash_table = dict()

    for s in input_str:
        val = hash_table.get(s, None)
        if val is None:
            hash_table[s] = 1
        else:
            hash_table[s] += 1

    for s in input_str:
        if hash_table[s] == 1:
            return s

    return None


print(get_only_one_first_char("minimum"))