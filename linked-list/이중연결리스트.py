# 노드
#   이중 연결 리스트를 구성하는 노드
#   연결 리스트와 달리 이전 노드까지 참조함
class Node:
    def __init__(self, data):
        self.data = data
        self.prev_node = None  # 이전 노드를 참조함
        self.next_node = None  # 다음 노드를 참조함


# 이중 연결 리스트
#   연결 리스트와 달리 마지막 노드까지 추적함
#   마지막 노드를 추적하므로 끝에서 읽기, 삽입, 삭제도 O(1)에 가능
class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head  # 시작 노드
        self.tail = tail  # 마지막 노드

    # 이중 연결 리스트 마지막에 삽입하는 메서드
    def insert_at_end(self, value):
        new_node = Node(value)

        # 연결 리스트에 노드가 없는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 연결 리스트에 노드가 존재하는 경우
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    # 이중 연결 리스트 시작에서 삭제하는 메서드
    def delete_from_front(self):
        # 시작 노드 제거
        deleted_node = self.head
        self.head = self.head.next_node  # 현재 시작 노드의 다음 노드가 시작 노드가 되게 함

        # 제거하는 노드와 시작 노드의 연결을 끊음
        deleted_node.next_node = None
        self.head.prev_node = None

        return deleted_node
