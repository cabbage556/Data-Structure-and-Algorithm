class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


# 연결 리스트의 장점
#   배열과 달리 삽입과 삭제 시 데이터를 시프트할 필요가 없어
#   전체 리스트를 훑으며 삽입이나 삭제를 빈번하게 수행하기에 알맞은 자료 구조
class LinkedList:
    def __init__(self, head = None):
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

    # 연결 리스트 내 모든 노드의 값 출력하는 메서드
    def print_all_nodes(self):
        # 첫 번째 노드부터 시작
        current_node = self.head

        # 연결 리스트 내 마지막 노드까지 이동
        while current_node:
            # 순회 중인 노드의 값 출력
            print(current_node.data)

            # 다음 노드로 이동
            current_node = current_node.next_node

    # 연결 리스트의 마지막 노드를 리턴하는 메서드
    def get_last_node(self):
        # 첫 번째 노드부터 시작
        current_node = self.head
        if current_node is None:
            return None

        # 연결 리스트 내 마지막 노드의 이전 노드까지 이동
        while current_node.next_node:
            # 다음 노드로 이동
            current_node = current_node.next_node

        # 마지막 노드 리턴
        return current_node

    # 연결 리스트를 거꾸로 뒤집는 메서드
    def reverse(self):
        prev_node = None  # 이전 노드
        current_node = self.head  # 현재 노드: 첫 번째 노드부터 시작

        while current_node:
            next_node = current_node.next_node  # 다음 노드

            # 현재 노드의 다음 노드로의 링크를 이전 노드로 바꿈
            current_node.next_node = prev_node

            # 한 칸씩 오른쪽으로 이동
            prev_node = current_node  # 이전 노드는 현재 노드를 가리키게 함
            current_node = next_node  # 현재 노드는 다음 노드를 가리키게 함

        # 최종적으로 첫 번째 노드는 이전 노드가 가리키는 노드(기존 연결 리스트의 마지막 노드)가 됨
        self.head = prev_node


# LinkedList 인스턴스 생성 후 첫 번째 노드 추적
linked_list = LinkedList()
linked_list.insert_at_index(0, 'a')
linked_list.insert_at_index(1, 'b')
linked_list.insert_at_index(2, 'c')

# LinkedList 인스턴스 내부의 모든 노드의 값 출력
print("-------------모든 노드의 값 출력 시작--------------")
linked_list.print_all_nodes()
print("-------------모든 노드의 값 출력 끝--------------")

# LinkedList 인스턴스 내부의 마지막 노드의 값 확인
print("-------------마지막 노드의 값 확인 시작--------------")
last_node = linked_list.get_last_node()
print(last_node.data)
print("-------------마지막 노드의 값 확인 끝--------------")

# LinkedList 인스턴스 내부 노드 뒤집기 확인
print("-------------노드 뒤집기 확인 시작--------------")
linked_list.reverse()
linked_list.print_all_nodes()
print("-------------노드 뒤집기 값 확인 끝--------------")


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
