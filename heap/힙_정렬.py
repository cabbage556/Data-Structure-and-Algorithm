from 힙_배열 import Heap

# 힙 정렬
#   모든 값을 힙에 삽입하고, 하나씩 제거하면 항상 정렬된 순서로 값이 제거됨
#   최대 힙의 경우: 내림차순 정렬
#   최소 힙의 경우: 오름차순 정렬

# 최대 힙
max_heap = Heap()

# 배열 순서대로 힙에 삽입
before = [55, 22, 34, 10, 2, 99, 68]
for num in before:
    max_heap.insert(num)

after = list()

# 최대 힙에서 하나씩 제거해 배열에 넣기
#   배열이 내림차순 정렬됨
after.append(max_heap.delete())
after.append(max_heap.delete())
after.append(max_heap.delete())
after.append(max_heap.delete())
after.append(max_heap.delete())
after.append(max_heap.delete())
after.append(max_heap.delete())
print("after:", after)

# 배열 순서대로 힙에 삽입
before = [55, 22, 34, 10]
for num in before:
    max_heap.insert(num)

after = list()

# 최대 힙에서 하나씩 제거해 배열에 넣기
#   배열이 내림차순 정렬됨
after.append(max_heap.delete())
after.append(max_heap.delete())
after.append(max_heap.delete())
after.append(max_heap.delete())
print("after:", after)