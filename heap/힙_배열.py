# 힙: 우선순위 큐의 기반 자료 구조
#   우선순위 큐는 큐에서 가장 높은 우선순위를 갖는 항목을 가장 먼저 치라함
#   힙에서는 가장 높은 우선순위를 갖는 항목이 루트 노드에 존재하므로 바로 접근할 수 있음
#   또한 가장 높은 우선순위를 갖는 항목을 처리할 때마다 그 다음으로 높은 우선순위를 갖는 항목이 루트 노드로 오면서 다음으로 처리할 수 있는 준비가 됨

# 정렬된 배열보다 힙을 우선순위 큐의 기반 자료 구조에 적합한 이유
#   힙은 정렬된 배열보다 삽입 시간이 매우 빠름
#   삽입 시간 복잡도
#       정렬된 배열: O(N)
#       힙: O(logN)
#   삭제 시간 복잡도
#       정렬된 배열: O(1)
#       힙: O(logN)

# 배열 기반 힙(최대 힙)
#   힙 삽입, 삭제 연산의 핵심은 마지막 노드 찾기
#       마지막 노드를 사용해 삽입, 삭제 연산을 처리하는 이유
#           균형 잡힌 힙을 유지해 삽입, 삭제 연산을 O(logN)만에 처리하기 위함
#   마지막 노드를 효율적으로 찾기 위해 내부적으로 배열을 사용할 수 있음
#       힙을 배열로 구현하는 이유
#           마지막 노드 문제 해결: 마지막 노드를 항상 배열의 마지막 원소로 저장하기 때문
#               배열의 마지막 원소에 접근만하면 마지막 노드를 쉽게 찾을 수 있음
class Heap:
    def __init__(self):
        self.data = []  # 힙의 내부 자료 구조: 배열

    # 루트 노드 반환
    def get_root_node(self):
        return self.data[0]

    # 마지막 노드 반환
    def get_last_node(self):
        return self.data[-1]

    # 왼쪽 자식 노드의 인덱스 반환
    #   부모 노드의 인덱스를 받아 왼쪽 자식 노드의 인덱스를 반환함
    def get_left_child_index(self, index):
        # 왼쪽 자식 노드의 인덱스 구하기 공식: 부모 노드 인덱스 * 2 + 1
        return index * 2 + 1

    # 오른쪽 자식 노드의 인덱스 반환
    #   부모 노드의 인덱스를 받아 오른쪽 자식 노드의 인덱스를 반환함
    def get_right_child_index(self, index):
        # 오른쪽 자식 노드의 인덱스 구하기 공식: 부모 노드 인덱스 * 2 + 2
        return index * 2 + 2

    # 부모 노드의 인덱스 반환
    #   자식 노드의 인덱스를 받아 부모 노드의 인덱스를 반환함
    def get_parent_index(self, index):
        # 부모 노드 인덱스 구하기 공식: (자식 노드 인덱스 - 1) / 2 (소수점 버림)
        return (index - 1) // 2

    # 힙 삽입 알고리즘
    #   노드를 생성하고, 마지막 노드로 삽입함
    #   새로 삽입한 노드와 그 부모 노드를 비교함
    #       새로 삽입한 노드가 더 크다면 부모 노드와 스왑함
    #   새로 삽입한 노드보다 큰 부모 노드를 만날 때까지 스왑을 반복해 새로 삽입한 노드를 힙 위로 올림
    #   시간 복잡도: O(logN)
    def insert(self, value):
        # 마지막 노드로 삽입
        self.data.push(value)

        # 새로 삽입한 노드의 인덱스(마지막 인덱스)
        new_node_idx = len(self.data) - 1

        # 그 부모 노드의 인덱스
        parent_idx = self.get_parent_index(new_node_idx)

        # 힙 위로 올리기(트리클링)
        while (new_node_idx > 0 and
               self.data[new_node_idx] > self.data[parent_idx]):

            # 새로 삽입한 노드가 더 크다면 부모 노드와 스왑함
            self.data[parent_idx], self.data[new_node_idx] = self.data[new_node_idx], self.data[parent_idx]

            # 새로 삽입한 노드 인덱스 업데이트
            new_node_idx = parent_idx

            # 그 부모 노드 인덱스 업데이트
            parent_idx = self.get_parent_index(new_node_idx)

        return

    # 힙 삭제 알고리즘
    #   삭제 알고리즘은 힙 자료 구조 특성상 항상 루트 노드를 삭제함
    #       우선순위 큐의 기반 자료 구조로 활용하기 위함
    #   루트 노드를 마지막 노드로 대체함
    #       기존의 루트 노드가 삭제됨
    #   루트 노드가 된 마지막 노드(트리클 노드)를 적절한 자리까지 아래로 트리클링함
    #   시간 복잡도: O(logN)
    def delete(self):
        deleted_node = self.data[0]

        # 루트 노드를 마지막 노드로 대체함
        self.data[0] = self.data.pop()

        # '트리클 노드'의 인덱스
        trickle_node_idx = 0

        # 힙 아래로 내리기(트리클링)
        while self.has_greater_child(trickle_node_idx):
            # 더 큰 값을 갖는 자식 노드의 인덱스
            larger_child_idx = self.get_larger_child_index(trickle_node_idx)

            # 트리클 노드와 더 큰 자식 노드 스왑
            self.data[trickle_node_idx], self.data[larger_child_idx] = self.data[larger_child_idx], self.data[trickle_node_idx]

            # 트리클 노드 인덱스 업데이트
            trickle_node_idx = larger_child_idx

        return deleted_node

    # 두 자식 노드가 있는지, index에 위치한 노드보다 큰 값을 갖는지 확인
    def has_greater_child(self, index):
        left_child_idx = self.get_left_child_index(index)
        right_child_idx = self.get_right_child_index(index)
        return ((self.data[left_child_idx] and self.data[left_child_idx] > self.data[index]) or
                (self.data[right_child_idx]) and self.data[right_child_idx] > self.data[index])

    # 두 자식 노드 중 더 큰 값을 갖는 자식 노드의 인덱스 반환
    def get_larger_child_index(self, index):
        right_child_idx = self.get_right_child_index(index)
        left_child_idx = self.get_left_child_index(index)

        # 오른쪽 자식 노드가 없으면 왼쪽 자식 노드의 인덱스 반환
        if self.data[right_child_idx] is None:
            return left_child_idx

        # 오른쪽 자식 노드가 더 크면 오른쪽 자식 노드 인덱스 반환
        if self.data[right_child_idx] > self.data[left_child_idx]:
            return right_child_idx
        # 왼쪽 자식 노드가 더 크면 왼쪽 자식 노드 인덱스 반환
        else:
            return left_child_idx


