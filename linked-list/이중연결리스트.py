# 이중 연결 리스트를 구성하는 노드
#   연결 리스트의 노드와 달리 이전 노드까지 참조함
class DoublyLinkedNode:
    def __init__(self, val, prev_node=None, next_node=None):
        self.val = val              # 노드에 저장하는 데이터
        self.prev_node = prev_node  # 이전 노드에 대한 참조
        self.next_node = next_node  # 다음 노드에 대한 참조
        return


# 이중 연결 리스트
#   연결 리스트와 달리 마지막 노드까지 추적함
#   마지막 노드를 추적하므로 이중 연결 리스트의 끝에서 읽기, 삽입, 삭제도 O(1)에 가능
class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head  # head 노드 : 이중 연결 리스트의 첫 번째 노드를 가리킴
        self.tail = tail  # tail 노드 : 이중 연결 리스트의 마지막 노드를 가리킴
        return

    # 이중 연결 리스트의 끝에 삽입
    def insert_at_end(self, value):
        # 삽입할 노드 생성
        new_node = DoublyLinkedNode(value)

        # 노드가 없는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 노드가 있는 경우
        else:
            new_node.prev_node = self.tail  # 삽입할 노드의 이전 노드가 현재 tail 노드를 가리키게 함
            self.tail.next_node = new_node  # 현재 tail노드의 다음 노드가 삽입할 노드를 가리키게 함
            self.tail = new_node            # tail 노드에 삽입할 노드를 할당함, 이중 연결 리스트의 가장 뒤에 삽입하기 때문
        return

    # 이중 연결 리스트의 앞에서 삭제
    def delete_from_front(self):
        # 시작 노드가 None인 경우 예외 처리
        if self.head is None:
            return None

        deleted_node = self.head                          # 삭제할 노드 : head 노드
        node_after_deleted_node = deleted_node.next_node  # 삭제할 노드의 다음 노드를 저장함

        # 삭제할 노드의 다음 노드가 None인 경우
        if node_after_deleted_node is None:
            # head 노드를 삭제하는데, 그 다음 노드가 None이면 이중 연결 리스트에 노드가 없다는 의미이므로 head, tail 노드에 None을 할당함
            self.head = None
            self.tail = None

            # 삭제한 head 노드 리턴
            return deleted_node

        # 삭제하는 노드와 연결 끊기
        node_after_deleted_node.prev_node = None
        deleted_node.next_node = None

        # head 노드 초기화
        self.head = node_after_deleted_node

        # 삭제한 head 노드 리턴
        return deleted_node

    # 이중 연결 리스트의 모든 노드의 값을 거꾸로 출력
    def print_all_nodes_from_tail(self):
        # tail 노드부터 head 노드까지 이동
        current_node = self.tail
        while current_node:
            # 순회 중인 노드의 값 출력
            print(current_node.val)
            current_node = current_node.prev_node

        return


dll = DoublyLinkedList()

print("==============  ==============")
dll.delete_from_front()
print("head:", dll.head)
print("tail:", dll.tail)
print()

dll.insert_at_end('a')
dll.insert_at_end('b')
dll.insert_at_end('c')

print("============== [a] <-> [b] <-> [c] ==============")
print("head.value:", dll.head.val)
print("head.next_node.value:", dll.head.next_node.val)
print("tail.value:", dll.tail.val)
print("tail.prev_node.value:", dll.tail.prev_node.val)
print()

print("============== print_all_nodes_from_tail ==============")
print("============== [a] <-> [b] <-> [c] ==============")
dll.print_all_nodes_from_tail()
print()

print("============== [b] <-> [c] ==============")
dll.delete_from_front()
print("head.value:", dll.head.val)
print("head.next_node.value:", dll.head.next_node.val)
print("tail.value:", dll.tail.val)
print("tail.prev_node.value:", dll.tail.prev_node.val)
print()

print("============== print_all_nodes_from_tail ==============")
print("============== [b] <-> [c] ==============")
dll.print_all_nodes_from_tail()
print()

print("==============  ==============")
dll.delete_from_front()
dll.delete_from_front()
print("head:", dll.head)
print("tail:", dll.tail)
print()
