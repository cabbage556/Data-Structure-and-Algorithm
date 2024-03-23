# 선택 정렬: 오름차순 정렬
#       시간 복잡도: O(N^2)
def selection_sort(arr):
    # 패스스루
    #       시작 인덱스 설정
    #       오름차순으로 값이 올바른 인덱스에 위치하도록 정렬
    for i in range(len(arr) - 1):
        min_index = i  # 최솟값 인덱스: 패스스루 시작 시 시작 인덱스 할당

        # 시작 인덱스의 다음 인덱스부터 오른쪽으로 이동하면서 비교 진행
        #       값을 비교해 최솟값 인덱스 업데이트
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # 패스스루 종료
        #       시작 인덱스와 최솟값 인덱스가 다르면 교환
        #       최솟값이 올바른 인덱스에 있지 않으면 교환하는 것
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


print(selection_sort([4, 2, 7, 1, 3]))