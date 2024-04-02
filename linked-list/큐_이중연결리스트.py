from 이중연결리스트 import DoublyLinkedList


# 이중 연결 리스트 기반 큐
#   이중 연결 리스트는 큐에 적합한 내부 자료 구조
#       리스트 끝에 삽입: O(1)
#       리스트 시작에서 삭제: O(1)
class Queue:
    def __init__(self):
        self.doubly_ll = DoublyLinkedList()

    def enqueue(self, value):
        self.doubly_ll.insert_at_end(value)

    def dequeue(self):
        deleted_node = self.doubly_ll.delete_from_front()
        if deleted_node is None:
            return None

        return deleted_node.data

    def read(self):
        if self.doubly_ll.head is None:
            return None

        return self.doubly_ll.head.data


q = Queue()
print(q.read())  # None

q.enqueue('a')
q.enqueue('b')

print(q.read())     # a
print(q.dequeue())  # a
print(q.read())     # b
print(q.dequeue())  # b

print(q.read())          # None
print(q.doubly_ll.head)  # None
print(q.doubly_ll.tail)  # None
