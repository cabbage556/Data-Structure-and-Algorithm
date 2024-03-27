# 유일 경로 문제
#       행과 열로 이뤄진 격자판이 있다.
#       한 번 움직일 때마다 한 칸 오른쪽 또는 한 칸 아래로 이동 가능하다.
#       행 수와 열 수를 받아 왼쪽 맨 윗칸에서 오른쪽 맨 아랫칸까지 가는 "최단 경로"의 개수를 구하기
def number_of_unique_paths(row, col):
    # 기저 조건
    # 행이 하나이거나 열이 하나일 때 이동 가능한 경로 수: 1
    #       한 칸 오른쪽, 한 칸 아래로만 이동 가능함
    if row == 1 or col == 1:
        return 1

    # (row - 1) x (col) 크기의 격자에서의 경로 수 + (row) x (col - 1) 크기의 격자에서의 경로 수
    return number_of_unique_paths(row - 1, col) + number_of_unique_paths(row, col - 1)


print(number_of_unique_paths(3, 7))
print(number_of_unique_paths(2, 2))
