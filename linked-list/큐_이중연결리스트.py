from 이중연결리스트 import DoublyLinkedList


# 이중 연결 리스트 기반 큐
#   이중 연결 리스트는 큐에 적합한 내부 자료 구조
#       리스트 끝에 삽입: O(1)
#       리스트 시작에서 삭제: O(1)
class Queue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def enqueue(self, value):
        self.data.insert_at_end(value)

    def dequeue(self):
        removed_node = self.data.delete_from_front()
        return removed_node.data

    def read(self):
        if self.data.head is None:
            return None

        return self.data.head.data


q = Queue()
q.enqueue('a')
q.enqueue('b')

print(q.read())  # a

print(q.dequeue())  # a
print(q.read())  # b
