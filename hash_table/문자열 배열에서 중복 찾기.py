# 문자열 배열에서 첫 번째 중복 문자열을 찾아 반환하는 함수
def get_duplication_string(arr):
    hash_table = dict()

    for s in arr:
        val = hash_table.get(s, None)
        if val is None:
            hash_table[s] = True
        else:
            return s

    return None


print(get_duplication_string(['a', 'b', 'c']))
print(get_duplication_string(['a', 'b', 'c', 'a', 'b']))
print(get_duplication_string(['a', 'b', 'c', 'b', 'a']))
