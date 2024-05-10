from 이중연결리스트 import DoublyLinkedList


# 이중 연결 리스트 기반 큐
#   이중 연결 리스트는 큐에 적합한 내부 자료 구조
#       이중 연결 리스트를 큐의 내부 자료 구조로 사용하면 큐의 주요 연산인 끝에 삽입 연산 및 앞에서 삭제 연산이 매우 빠르기 때문
#       이중 연결 리스트 끝에 삽입 시간 복잡도 : O(1)
#       이중 연결 리스트 앞에서 삭제 시간 복잡도 : O(1)
class Queue:
    def __init__(self):
        self.dll = DoublyLinkedList()  # 내부 자료 구조 : 이중 연결 리스트
        return

    # 큐 뒤에 삽입하기
    def enqueue(self, value):
        self.dll.insert_at_end(value)  # 이중 연결 리스트 끝에 삽입
        return

    # 큐 앞에서 삭제하기
    def dequeue(self):
        deleted_node = self.dll.delete_from_front()  # 이중 연결 리스트 앞에서 삭제
        return deleted_node.val if deleted_node else None

    # 큐 앞에 있는 원소 읽기
    def read(self):
        # 이중 연결 리스트 head 노드의 데이터 리턴
        return self.dll.head.val if self.dll.head else None


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
