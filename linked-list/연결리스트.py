"""
연결 리스트의 장점 : 원소 삽입과 삭제를 빈번하게 수행하기에 알맞은 자료 구조
    연결 리스트는 배열과 달리 원소 삽입과 삭제 시 연결 리스트에서 원소들을 시프트할 필요가 없어
    연결 리스트 전체를 훑으며 원소 삽입과 삭제를 빈번하게 수행하기에 알맞은 자료 구조임
"""


# 연결 리스트를 구성하는 노드
class Node:
    def __init__(self, val):
        self.val = val         # 노드에 저장하는 데이터
        self.next_node = None  # 다음 노드에 대한 참조
        return


# 연결 리스트
class LinkedList:
    def __init__(self, head=None):
        # head 노드 : 연결 리스트의 첫 번째 노드를 가리킴
        self.head = head
        return

    # 연결 리스트 읽기
    #       시간 복잡도 : O(N)
    def read_at_index(self, idx):
        # head 노드부터 시작
        current_idx = 0
        current_node = self.head

        # idx에 위치한 노드까지 이동
        while current_idx < idx:

            # idx에 도착하기 전에 다음 노드가 없다는 것 : idx에 해당하는 노드가 없다는 의미이므로 None 리턴
            if current_node is None:
                return None

            current_node = current_node.next_node
            current_idx += 1

        return current_node.val if current_node else None

    # 연결 리스트 검색
    #       시간 복잡도 : O(N)
    def index_of(self, search_val):
        # head 노드부터 시작
        current_idx = 0
        current_node = self.head

        # 연결 리스트에서 search_val을 찾을 때까지 다음 노드로 이동
        while current_node:

            # search_val을 찾았으면 현재 인덱스 리턴
            if current_node.val == search_val:
                return current_idx

            current_node = current_node.next_node
            current_idx += 1

        # 찾지 못했으면 -1 리턴
        return -1

    # 연결 리스트 삽입
    #    맨 앞 삽입 시간 복잡도 : O(1)
    #    맨 뒤 삽입 시간 복잡도 : O(N)
    def insert_at_index(self, idx, value):
        new_node = Node(value)  # 삽입할 노드 생성

        # 앞에 삽입
        if idx == 0:
            new_node.next_node = self.head  # 삽입할 노드의 다음 노드가 현재 head 노드를 가리키게 함
            self.head = new_node            # head 노드에 삽입할 노드를 할당함, 연결 리스트의 앞에 삽입하기 때문
            return

        # 뒤에 삽입
        # head 노드부터 시작
        current_idx = 0
        current_node = self.head

        # 삽입하려는 idx의 바로 이전 노드까지 이동
        while current_idx < idx - 1:

            # 삽입하려는 idx의 바로 이전 노드까지 접근할 수 없으면 종료
            if current_node is None:
                return

            current_idx += 1
            current_node = current_node.next_node

        # 연결 리스트에서 원소들의 next_node를 바꿔서 새로운 노드를 삽입할 수 있음
        #       (current_node) -> (current_node.next_node)
        #                   (new_node)
        new_node.next_node = current_node.next_node  # 삽입할 노드를 idx 위치에 삽입함
        current_node.next_node = new_node            # 삽입할 노드의 앞 노드가 삽입할 노드를 가리키게 함
        return

    # 연결 리스트 삭제
    #    맨 앞 삭제 시간 복잡도 : O(1)
    #    맨 뒤 삭제 시간 복잡도 : O(N)
    def delete_at_index(self, idx):
        if self.head is None:
            return

        # 앞에서 삭제
        if idx == 0:
            node_after_deleted_node = self.head.next_node  # head 노드의 다음 노드 저장
            self.head.next_node = None                     # head 노드와 그 다음 노드의 링크를 끊음
            self.head = node_after_deleted_node            # head 노드의 다음 노드가 새로운 head 노드가 됨
            return

        # 뒤에서 삭제
        # head 노드부터 시작
        current_idx = 0
        current_node = self.head

        # 삽입하려는 idx의 바로 이전 노드까지 이동
        while current_idx < idx - 1:

            # 삽입하려는 idx의 바로 이전 노드까지 접근할 수 없으면 종료
            if current_node is None:
                return

            current_idx += 1
            current_node = current_node.next_node

        # 삭제하려는 노드의 다음 노드 저장
        #       (current_node) -> (삭제하려는 노드) -> (node_after_deleted_node)
        node_after_deleted_node = current_node.next_node.next_node

        # 삭제하려는 노드와 그 다음 노드의 링크를 끊음
        #       (current_node) -> (삭제하려는 노드) (node_after_deleted_node)
        current_node.next_node.next_node = None

        # 현재 노드가 삭제하려는 노드의 다음 노드를 가리키게 함
        #       삭제하려는 노드가 리스트에서 제외됨
        #       (current_node) -> (node_after_deleted_node)
        current_node.next_node = node_after_deleted_node
        return

    # 연결 리스트 내 모든 노드의 값을 출력하는 메서드
    def print_all_nodes(self):
        # head 노드부터 시작
        current_node = self.head

        # 마지막 노드까지 이동
        while current_node:
            # 노드의 값 출력
            print(current_node.val)

            # 다음 노드로 이동
            current_node = current_node.next_node

        return

    # 연결 리스트의 마지막 노드를 리턴하는 메서드
    def get_last_node(self):
        if self.head is None:
            return None

        # head 노드부터 시작
        current_node = self.head

        # 현재 노드의 다음 노드가 존재하면 다음 노드로 이동
        while current_node.next_node:
            current_node = current_node.next_node

        return current_node

    # 연결 리스트를 거꾸로 뒤집는 메서드
    def reverse(self):
        prev_node = None          # 이전 노드
        current_node = self.head  # 현재 노드 : head 노드부터 시작

        while current_node:
            next_node = current_node.next_node  # 다음 노드
            current_node.next_node = prev_node  # 현재 노드의 다음 노드를 이전 노드로 바꿈
            prev_node = current_node            # 이전 노드는 현재 노드를 가리키게 함
            current_node = next_node            # 현재 노드는 다음 노드를 가리키게 함

        # 최종적으로 head 노드는 이전 노드가 가리키는 노드(기존 연결 리스트의 마지막 노드)가 됨
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
print("last node value:", last_node.val if last_node else None)


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
