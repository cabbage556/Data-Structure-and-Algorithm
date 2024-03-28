# 재귀 연습 문제인 "유일 경로" 문제를 메모이제이션으로 개선하기
def number_of_unique_paths(row, col, memo=dict()):
    # print('recursion')

    # 기저 조건
    # 행이 하나이거나 열이 하나일 때 이동 가능한 경로 수: 1
    #       한 칸 오른쪽, 한 칸 아래로만 이동 가능함
    if row == 1 or col == 1:
        return 1

    # 해시 테이블 키
    k = f"{row}{col}"

    # 해시 테이블 확인
    if not memo.get(k):
        # 해시 테이블에 결과가 없으면 경로 수 계산 후 저장
        # (row - 1) x (col) 크기의 격자에서의 경로 수 + (row) x (col - 1) 크기의 격자에서의 경로 수
        memo[k] = (
                number_of_unique_paths(row - 1, col, memo) +
                number_of_unique_paths(row, col - 1, memo)
        )

    # 해시 테이블에서 값 리턴
    return memo[k]


print(number_of_unique_paths(3, 7))
