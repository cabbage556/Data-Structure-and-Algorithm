class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


# 연결 리스트의 장점
#   배열과 달리 삽입과 삭제 시 데이터를 시프트할 필요가 없어
#   전체 리스트를 훑으며 삽입이나 삭제를 빈번하게 수행하기에 알맞은 자료 구조
class LinkedList:
    def __init__(self, head):
        # head: 연결 리스트의 첫 번째 노드
        self.head = head

    # 연결 리스트 읽기: O(N)
    def read(self, idx):
        # 연결 리스트의 첫 번째 노드부터 시작
        current_node = self.head
        current_idx = 0

        while current_idx < idx:
            # 찾고 있는 인덱스까지 노드의 다음 노드를 계속 따라감
            current_node = current_node.next_node
            current_idx += 1

            # 찾고 있는 인덱스에 도착하기 전에 마지막 노드의 다음 노드(None)에 도착했다면
            # 인덱스에 해당하는 노드가 없다는 의미이므로 None 리턴
            if current_node is None:
                return None

        return current_node.data

    # 연결 리스트 검색: O(N)
    def index_of(self, value):
        # 연결 리스트의 첫 번째 노드부터 시작
        current_node = self.head
        current_idx = 0

        while current_node is not None:
            # 값을 찾았으면 인덱스 리턴
            if current_node.data == value:
                return current_idx

            # 값을 찾지 못했으면 다음 노드로 이동
            current_node = current_node.next_node
            current_idx += 1

        # 연결 리스트에서 값을 찾지 못했으면 None 리턴
        return None

    # 연결 리스트 삽입
    #    맨 앞 삽입: O(1)
    #    맨 뒤 삽입: O(N)
    def insert_at_index(self, index, value):
        new_node = Node(value)  # 삽입할 노드 생성

        # 연결 리스트 앞에 삽입하는 경우
        if index == 0:
            # 새 노드의 다음 노드가 현재 head 노드를 가리키게 함
            new_node.next_node = self.head

            # head 노드에 새 노드 할당
            self.head = new_node
            return

        # 앞이 아닌 곳에 삽입하는 경우
        # 첫 번째 노드부터 시작
        current_node = self.head
        current_idx = 0

        # 삽입하려는 인덱스의 바로 이전 노드까지 접근
        while current_idx < index - 1:
            current_node = current_node.next_node
            current_idx += 1

            # 인덱스의 바로 이전 노드까지 접근할 수 없으면 종료
            if current_node is None:
                return

        # 새 노드를 인덱스 위치에 삽입
        new_node.next_node = current_node.next_node

        # 앞 노드가 새 노드를 가리키게 함
        current_node.next_node = new_node

    # 연결 리스트 삭제
    #    맨 앞 삭제: O(1)
    #    맨 뒤 삭제: O(N)
    def delete_at_index(self, index):
        # 첫 번째 노드를 삭제하는 경우 두 번째 노드가 첫 번째 노드가 되게 함
        if index == 0:
            self.head = self.head.next_node
            return

        current_node = self.head
        current_idx = 0

        # 삭제하려는 인덱스의 바로 이전 노드까지 접근
        while current_idx < index - 1:
            current_node = current_node.next_node
            current_idx += 1

            # 인덱스의 바로 이전 노드까지 접근할 수 없으면 종료
            if current_node is None:
                return

        # 삭제하려는 노드의 바로 뒤 노드
        #       (current_node) -> (삭제하려는 노드) -> (node_after_deleted_node)
        node_after_deleted_node = current_node.next_node.next_node

        # 현재 노드가 삭제하려는 노드의 바로 뒤 노드를 가리키게 함
        #   삭제하려는 노드가 리스트에서 제외됨
        current_node.next_node = node_after_deleted_node


# Node 인스턴스 생성 후 연결
node1 = Node("Once")
node2 = Node("upon")
node3 = Node("a")
node4 = Node("time")
node1.next_node = node2
node2.next_node = node3
node3.next_node = node4

# LinkedList 인스턴스 생성 후 첫 번째 노드 추적
linked_list = LinkedList(node1)

print(linked_list.read(3))  # time
print(linked_list.read(4))  # None

print(linked_list.index_of('time'))  # 3
print(linked_list.index_of('...'))   # None

linked_list.insert_at_index(4, "...")
print(linked_list.read(4))           # ...
print(linked_list.index_of("..."))   # 4

print(linked_list.insert_at_index(10, "There"))  # None

linked_list.delete_at_index(4)
print(linked_list.read(4))           # None
print(linked_list.index_of("..."))   # None












