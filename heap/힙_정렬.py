import random
from 힙_배열 import Heap

"""
    힙 정렬
        모든 값을 힙에 삽입하고 하나씩 제거하면 항상 정렬된 순서로 값이 제거됨
        최대 힙 : 내림차순 정렬
        최소 힙 : 오름차순 정렬
"""

# 최대 힙
max_heap = Heap()

# 배열 순서대로 최대 힙에 삽입
before = [random.randint(1, 100) for _ in range(10)]
for num in before:
    max_heap.insert(num)


# 최대 힙에서 하나씩 제거해 배열에 넣기
#   배열이 내림차순 정렬됨
after = list()
for _ in range(len(before)):
    after.append(max_heap.delete())

print("before:", before)
print("after:", after)

# 배열 순서대로 최대 힙에 삽입
before = [random.randint(1, 100) for _ in range(10)]
for num in before:
    max_heap.insert(num)

# 최대 힙에서 하나씩 제거해 배열에 넣기
#   배열이 내림차순 정렬됨
after = list()
for _ in range(len(before)):
    after.append(max_heap.delete())

print("before:", before)
print("after:", after)
