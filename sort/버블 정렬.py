# 버블 정렬: 오름차순 정렬
#       시간 복잡도: O(N^2)
def bubble_sort(arr):
    bubble_index = len(arr) - 1  # 버블의 인덱스: 아직 정렬되지 않은 배열의 가장 오른쪽 인덱스
    sorted = False  # 배열 정렬 여부

    # 배열이 정렬될 때까지 while 루프 실행
    while not sorted:
        sorted = True  # 교환이 일어나기 전까지 배열이 정렬되었음을 가정함

        # 패스스루 시작
        for i in range(bubble_index):
            # 모든 인접 값 쌍을 비교
            #       순서가 뒤바뀌었다면 교환
            #       순서가 뒤바뀌었다면 배열이 정렬되지 않았으므로 sorted에 False 할당
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False

        # 패스스루 종료 -> 버블(패스스루에서 가장 큰 값)이 올바르게 정렬됨
        #       버블이 올바르게 정렬되었으므로 버블의 인덱스 1 감소
        bubble_index -= 1

    return arr


print(bubble_sort([4, 2, 7, 1, 3]))