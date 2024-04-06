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
        return

    def dequeue(self):
        deleted_node = self.doubly_ll.delete_from_front()
        return deleted_node.value if deleted_node else None

    def read(self):
        return self.doubly_ll.head.value if self.doubly_ll.head else None


q = Queue()

print("============== 이중 연결 리스트 기반 큐 ==============")
print("==============  ==============")
print("read:", q.read())
print()

q.enqueue('a')
q.enqueue('b')

print("============== [a], [b] ==============")
print("read:", q.read())
print("dequeue:", q.dequeue())
print()

print("============== [b] ==============")
print("read:", q.read())
print("dequeue:", q.dequeue())
print()

print("==============  ==============")
print("read:", q.read())
print("dequeue:", q.dequeue())
print()
