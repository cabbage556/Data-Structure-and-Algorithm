# 수 배열을 받아 그 합을 반환하되, 합이 100을 초과하게 만드는 수는 제외함
#       어떤 수를 더해 합이 100이 넘으면 그 수는 무시함
def add_until_100(arr):
    # 기저 조건
    if len(arr) == 0:
        return 0

    # 재귀 호출의 결과를 변수에 저장해 불필요한 재귀 호출을 방지함
    current_sum = add_until_100(arr[1:])

    if arr[0] + current_sum > 100:
        return current_sum
    else:
        return arr[0] + current_sum


print(add_until_100([1, 100, 2, 3]))
