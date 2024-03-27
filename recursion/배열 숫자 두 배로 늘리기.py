# 배열의 모든 원소에 2를 곱하기
# 반복 실행 카테고리
#       파라미터를 추가해, 적절한 아규먼트를 전달하기
def double_array(arr, index=0):
    # 기저 조건
    if index >= len(arr):
        return

    arr[index] *= 2
    double_array(arr, index + 1)


arr = [1, 2, 3, 4, 5]
double_array(arr)
print(arr)