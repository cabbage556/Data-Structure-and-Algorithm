# 연결 리스트를 구성하는 노드
class Node:
    def __init__(self, value):
        self.value = value     # 노드가 저장하는 실제 데이터
        self.next_node = None  # 다음 노드로의 링크


# 연결 리스트의 장점
#   배열과 달리 삽입과 삭제 시 데이터를 시프트할 필요가 없어
#   전체 리스트를 훑으며 삽입이나 삭제를 빈번하게 수행하기에 알맞은 자료 구조
class LinkedList:
    def __init__(self, head=None):
        self.head = head  # 첫 번째 노드 추적

    # 연결 리스트 읽기: O(N)
    def read_at_index(self, idx):
        # 첫 번째 노드부터 시작
        current_idx = 0
        current_node = self.head

        # 인덱스에 위치한 노드까지 이동
        while current_idx < idx:

            # 찾고 있는 인덱스에 도착하기 전에 마지막 노드의 다음 노드(None)에 도착했다면
            # 인덱스에 해당하는 노드가 없다는 의미이므로 None 리턴
            if current_node is None:
                return None

            current_node = current_node.next_node
            current_idx += 1

        return current_node.value if current_node else None

    # 연결 리스트 검색: O(N)
    def index_of(self, value):
        # 첫 번째 노드부터 시작
        current_idx = 0
        current_node = self.head

        # 값을 찾을 때까지 다음 노드로 이동
        while current_node:
            if current_node.value == value:
                return current_idx

            current_idx += 1
            current_node = current_node.next_node

        # 찾지 못했으면 -1 리턴
        return -1

    # 연결 리스트 삽입
    #    맨 앞 삽입: O(1)
    #    맨 뒤 삽입: O(N)
    def insert_at_index(self, index, value):
        new_node = Node(value)  # 삽입할 노드 생성

        # 앞에 삽입: O(1)
        if index == 0:
            new_node.next_node = self.head  # 새 노드의 다음 노드가 현재 head 노드를 가리키게 함
            self.head = new_node  # head 노드에 새 노드 할당
            return

        # 뒤에 삽입: O(N)
        # 첫 번째 노드부터 시작
        current_idx = 0
        current_node = self.head

        # 삽입하려는 위치의 바로 이전 노드까지 이동
        while current_idx < index - 1:

            # 인덱스의 바로 이전 노드까지 접근할 수 없으면 종료
            if current_node is None:
                return

            current_idx += 1
            current_node = current_node.next_node

        # (current_node) -> (current_node.next_node)
        #           (new_node)
        new_node.next_node = current_node.next_node  # 새 노드를 인덱스 위치에 삽입
        current_node.next_node = new_node  # 앞 노드가 새 노드를 가리키게 함
        return

    # 연결 리스트 삭제
    #    맨 앞 삭제: O(1)
    #    맨 뒤 삭제: O(N)
    def delete_at_index(self, index):
        if self.head is None:
            return

        # 앞에서 삭제: O(1)
        if index == 0:
            node_after_deleted_node = self.head.next_node
            self.head.next_node = None
            self.head = node_after_deleted_node
            return

        # 뒤에서 삭제: O(N)
        # 첫 번째 노드부터 시작
        current_idx = 0
        current_node = self.head

        # 삽입하려는 위치의 바로 이전 노드까지 이동
        while current_idx < index - 1:

            # 인덱스의 바로 이전 노드까지 접근할 수 없으면 종료
            if current_node is None:
                return

            current_idx += 1
            current_node = current_node.next_node

        # (current_node) -> (삭제하려는 노드) -> (node_after_deleted_node)
        node_after_deleted_node = current_node.next_node.next_node

        # 삭제하려는 노드의 다음 노드 링크를 끊음
        #       (current_node) -> (삭제하려는 노드) (node_after_deleted_node)
        current_node.next_node.next_node = None

        # 현재 노드가 삭제하려는 노드의 바로 뒤 노드를 가리키게 함
        #       삭제하려는 노드가 리스트에서 제외됨
        #       (current_node) -> (node_after_deleted_node)
        current_node.next_node = node_after_deleted_node
        return

    # 연결 리스트 내 모든 노드의 값 출력하는 메서드
    def print_all_nodes(self):
        # 첫 번째 노드부터 시작
        current_node = self.head

        # 연결 리스트 내 마지막 노드까지 이동
        while current_node:
            # 순회 중인 노드의 값 출력
            print(current_node.value)

            # 다음 노드로 이동
            current_node = current_node.next_node

        return

    # 연결 리스트의 마지막 노드를 리턴하는 메서드
    def get_last_node(self):
        if self.head is None:
            return None

        # 첫 번째 노드부터 시작
        current_node = self.head

        # 다음 노드가 존재하면 다음 노드로 이동
        #   다음 노드가 없는 마지막 노드까지 이동하는 것
        while current_node.next_node:
            current_node = current_node.next_node

        return current_node

    # 연결 리스트를 거꾸로 뒤집는 메서드
    def reverse(self):
        prev_node = None  # 이전 노드
        current_node = self.head  # 현재 노드: 첫 번째 노드부터 시작

        while current_node:
            next_node = current_node.next_node  # 다음 노드
            current_node.next_node = prev_node  # 현재 노드의 다음 노드로의 링크를 이전 노드로 바꿈
            prev_node = current_node  # 이전 노드는 현재 노드를 가리키게 함
            current_node = next_node  # 현재 노드는 다음 노드를 가리키게 함

        # 최종적으로 첫 번째 노드는 이전 노드가 가리키는 노드(기존 연결 리스트의 마지막 노드)가 됨
        self.head = prev_node
        return


linked_list = LinkedList()
linked_list.insert_at_index(0, 'a')
linked_list.insert_at_index(1, 'b')

print("============== [a] -> [b] ==============")
print("read at index 0:", linked_list.read_at_index(0))
print("read at index 1:", linked_list.read_at_index(1))
print()

print("============== [b] -> [c] -> [d] ==============")
linked_list.delete_at_index(0)
linked_list.insert_at_index(1, 'c')
linked_list.insert_at_index(2, 'd')
print("read at index 0:", linked_list.read_at_index(0))
print("read at index 1:", linked_list.read_at_index(1))
print("read at index 2:", linked_list.read_at_index(2))
print("read at index 3:", linked_list.read_at_index(3))
print()

print("============== index_of ==============")
print("============== [b] -> [c] -> [d] ==============")
print("index of 'd':", linked_list.index_of('d'))
print("index of 'e':", linked_list.index_of('e'))
print()

print("============== reverse ==============")
print("============== [d] -> [c] -> [b] ==============")
linked_list.reverse()
print("read at index 0:", linked_list.read_at_index(0))
print("read at index 1:", linked_list.read_at_index(1))
print("read at index 2:", linked_list.read_at_index(2))
print("read at index 3:", linked_list.read_at_index(3))
print()

print("============== print_all_node ==============")
print("============== [d] -> [c] -> [b] ==============")
linked_list.print_all_nodes()
print()

print("============== get_last_node ==============")
print("============== [d] -> [c] -> [b] ==============")
last_node = linked_list.get_last_node()
print("last node value:", last_node.value if last_node else None)


# 연결 리스트 인스턴스에 접근할 수 없고, 중간 노드에만 접근할 수 있을 때
# 연결 리스트에서 접근 가능한 중간 노드를 삭제하는 함수
#   접근 가능한 중간 노드를 제거하지 않고, 그 다음 노드를 제거하는 것
def delete_middle_node(node):
    # 현재 접근 중인 노드의 다음 노드
    next_node = node.next_node

    # 현재 접근 중인 노드의 값을 다음 노드의 값으로 변경
    node.data = next_node.data

    # 현재 접근 중인 노드의 다음 노드가 next_node의 다음 노드를 가리키게 함
    node.next_node = next_node.next_node

    # next_node를 연결 리스트에서 제외시킴
    next_node.next_node = None
