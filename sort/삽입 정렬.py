# 삽입 정렬: 오름차순 정렬
#       시간 복잡도: O(N^2)
def insertion_sort(arr):
    # 패스스루
    #       '정렬하는' 인덱스 설정, 1부터 시작
    for i in range(1, len(arr)):
        temp_val = arr[i]  # 패스스루마다 '정렬하는' 인덱스의 값
        pos = i - 1  # '정렬하는' 인덱스의 바로 왼쪽 인덱스: temp_val와 비교할 값의 인덱스

        while pos >= 0:
            # pos에 위치한 값과 temp_val 값 비교
            #       pos에 위치한 값이 더 크면 오른쪽으로 시프트
            #       다음 pos 왼쪽 값과 temp_val 값을 비교할 수 있도록 pos 값 1 감소
            if arr[pos] > temp_val:
                arr[pos + 1] = arr[pos]
                pos -= 1
            #       pos에 위치한 값이 더 작으면 temp_val을 공백에 삽입하기 위해 while 루프 종료
            else:
                break

        # 패스스루 종료
        #       temp_val을 공백에 삽입
        arr[pos + 1] = temp_val

    return arr


print(insertion_sort([4, 2, 7, 1, 3]))