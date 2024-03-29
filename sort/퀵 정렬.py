# 배열 분할 함수
#   역할
#       1. 현재 배열에서 피벗이 올바른 곳에 위치하게 함
#       2. 피벗 기준 왼쪽 배열에 피벗보다 작은 값들이 위치하게 함(아직 정렬되지 않은 상태)
#       3. 피벗 기준 오른쪽 배열에 피벗보다 큰 값들이 위치하게 함(아직 정렬되지 않은 상태)
def partition(arr, left_pointer, right_pointer):
    # 피벗: 배열에서 가장 오른쪽 값으로 선택
    pivot_idx = right_pointer
    pivot = arr[pivot_idx]

    # 오른쪽 포인터는 피벗 바로 왼쪽부터 시작
    right_pointer -= 1

    while True:
        # 1단계: 왼쪽 포인터 이동
        #       피벗보다 크거나 같은 값을 가리킬 때까지 1칸씩 오른쪽으로 이동
        while arr[left_pointer] < pivot:
            left_pointer += 1

        # 2단계: 오른쪽 포인터 이동
        #       피벗보다 작거나 같은 값을 가리킬 때까지 1칸씩 왼쪽으로 이동
        while arr[right_pointer] > pivot:
            right_pointer -= 1

        # 3단계: 왼쪽 포인터와 오른쪽 포인터 비교하기
        #       if: 왼쪽 포인터가 오른쪽 포인터보다 크거나 같은 경우
        #       else: 왼쪽 포인터가 오른쪽 포인터보다 작으면 작은 경우
        if left_pointer >= right_pointer:
            # 루프를 빠져나가 왼쪽 포인터의 값과 피벗 교환
            break
        else:
            # 두 포인터의 값 교환 후 다음 비교를 위해 왼쪽 포인터 오른쪽으로 1칸 이동
            arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
            left_pointer += 1

    # 4단계: 왼쪽 포인터의 값과 피벗 교환
    arr[left_pointer], arr[pivot_idx] = arr[pivot_idx], arr[left_pointer]

    # 하위 배열에 대해 왼쪽 포인터가 피벗 인덱스가 되므로 왼쪽 포인터 리턴
    return left_pointer


# 퀵 정렬: 오름차순 정렬
#       배열 분할 후 왼쪽, 오른쪽 하위 배열에 대해 재귀 호출
#       시간 복잡도(최악): O(N^2)
#       시간 복잡도(평균): O(NlogN)
#           평균적인 시나리오, 즉 배열이 적절히 섞여 있을 때가 가장 많이 발생하는 경우이므로 퀵 정렬이 많이 사용됨
def quick_sort(arr, left_idx, right_idx):
    # 기저 조건: 하위 배열 크기가 0 또는 1일 때
    if right_idx <= left_idx:
        return

    # 피벗 인덱스 구하기
    pivot_idx = partition(arr, left_idx, right_idx)

    # 피벗 인덱스를 기준으로 왼쪽, 오른쪽 하위 배열에 대해 재귀 호출
    quick_sort(arr, left_idx, pivot_idx - 1)
    quick_sort(arr, pivot_idx + 1, right_idx)


arr = [0, 5, 2, 1, 6, 3]
quick_sort(arr, 0, len(arr) - 1)
print(arr)

arr = [-1, -10, 5, 1, 3, 10]
quick_sort(arr, 0, len(arr) - 1)
print(arr)







