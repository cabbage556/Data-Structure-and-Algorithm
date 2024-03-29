# 양수 배열에서 세 수의 가장 큰 곱을 반환하기
#       정렬을 사용해 O(NlogN) 시간 복잡도로 구현하기
def greatest_product_of_three(arr):
    # 정렬 후 마지막 세 원소의 곱 리턴
    arr.sort()
    return arr[-1] * arr[-2] * arr[-3]


print(greatest_product_of_three([1, 9, 4, 3, 2, 7]))