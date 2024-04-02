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
        # 새 노드 생성
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
        # 시작 노드가 None인 경우 예외 처리
        if self.head is None:
            return None

        deleted_node = self.head   # 삭제하는 노드
        node_after_deleted_node = deleted_node.next_node  # 삭제하는 노드의 다음 노드

        # 다음 노드가 None인 경우 예외 처리
        if node_after_deleted_node is None:
            self.head = None
            self.tail = None
            return deleted_node

        # 삭제하는 노드와 연결 끊기
        node_after_deleted_node.prev_node = None
        deleted_node.next_node = None

        # 시작 노드 초기화
        self.head = node_after_deleted_node

        # 제거한 노드 리턴
        return deleted_node

    # 이중 연결 리스트 내 모든 노드의 값을 거꾸로 출력하는 메서드
    def print_all_nodes_from_tail(self):
        # 마지막 노드부터 시작
        current_node = self.tail

        # 이중 연결 리스트 내 시작 노드까지 이동
        while current_node:
            # 순회 중인 노드의 값 출력
            print(current_node.data)

            # 이전 노드로 이동
            current_node = current_node.prev_node


# 이중 연결 리스트 인스턴스 생성
doubly_linked_list = DoublyLinkedList()

# 이중 연결 리스트에 노드 추가
doubly_linked_list.insert_at_end("a")
doubly_linked_list.insert_at_end("b")
doubly_linked_list.insert_at_end("c")
doubly_linked_list.insert_at_end("d")

# 거꾸로 출력
print("-------------모든 노드의 값 거꾸로 출력 시작--------------")
doubly_linked_list.print_all_nodes_from_tail()
print("-------------모든 노드의 값 거꾸로 출력 끝--------------")
