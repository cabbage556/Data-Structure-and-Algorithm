# n번째 피보나치 수열 구하기
#       재귀 함수로 구현
#       시간 복잡도: O(N)
#           하위 문제 중첩을 메모이제이션으로 해결
def fib(n, memo=dict()):
    # 호출 횟수 확인
    print('recursion')

    # 기저 조건
    if n == 0 or n == 1:
        return n

    # 해시 테이블을 확인해 fib(n)이 이미 계산되었는지 확인함
    if not memo.get(n):

        # fib(n)이 계산되지 않았다면 재귀로 fib(n) 계산
        # 결과를 해시 테이블에 저장
        memo[n] = fib(n - 2, memo) + fib(n - 1, memo)

    # 해시 테이블에서 fib(n) 결과 리턴
    return memo[n]


print(fib(6))
