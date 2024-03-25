class MyQueue:
    def __init__(self):
        # 리스트 기반 큐
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        # O(1)
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            # O(N): 리스트 기반
            #       첫 번째 요소 제거 후 반환
            return self.items.pop(0)
        else:
            return None

    def size(self):
        return len(self.items)