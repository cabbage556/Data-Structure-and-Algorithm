# 재귀를 사용해 "골롬 수열"이라는 수열의 n번째 수를 계산하는 함수를
# 메모이제이션을 활용해 재귀를 최적화하기
def golomb(n, memo=dict()):
    # print("golomb")

    # 기저 조건
    if n == 1:
        return 1

    # 해시 테이블 확인
    if not memo.get(n):
        # 해시 테이블에 결과가 없으면 골롬 수열 계산 후 결과 저장
        memo[n] = 1 + golomb(n - golomb(golomb(n - 1, memo), memo), memo)

    # 해시 테이블에서 값 리턴
    return memo[n]


print(golomb(10))