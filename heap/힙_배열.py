"""
    우선순위 큐의 기반 자료 구조로 '힙'이 적합한 이유
        우선순위 큐는 가장 높은 우선순위를 갖는 항목을 가장 먼저 처리하는 자료 구조
        힙에서는 가장 높은 우선순위를 갖는 항목이 루트 노드에 존재하므로 루트 노드에 접근하면 가장 높은 우선순위를 갖는 항목에 바로 접근할 수 있음
        또한 힙에서 가장 높은 우선순위를 갖는 항목을 처리할 때마다 그 다음으로 높은 우선순위를 갖는 항목이 루트 노드로 오면서 다음으로 처리할 수 있는 준비가 됨


    정렬된 배열보다 '힙'이 우선순위 큐의 기반 자료 구조에 적합한 이유
        우선순위 큐는 삽입 연산과 삭제 연산이 비슷한 비율로 수행되므로 두 연산이 모두 빠르게 동작해야 함
        두 자료 구조의 삽입 연산 시간 복잡도 비교
            정렬된 배열 : O(N)
            힙 : O(logN)
        두 자료 구조의 삭제 연산 시간 복잡도 비교
            정렬된 배열 : O(1)
            힙 : O(logN)
        정렬된 배열의 삽입보다 힙의 삽입이 훨씬 빠르기 때문에 우선순위 큐의 기반 자료 구조로 힙이 더 적합함

    힙의 두 가지 조건
        힙은 '힙 조건'을 만족하는 '완전 트리'이다.
        1. 힙 조건
           최대 힙 조건 : 각 노드의 값은 모든 자손 노드의 값보다 커야 함
           최소 힙 조건 : 각 노드의 값은 모든 자손 노드의 값보다 작아야 함
        2. 완전 트리
           빠진 노드 없이 노드가 완전히 채워진 트리를 말함
                트리의 모든 레벨을 왼쪽에서 오른쪽으로 봤을 때 모든 자리마다 노드가 존재해야 함
           예외적으로 바닥 레벨에는 빈 자리가 있을 수 있음
                이때 바닥 레벨의 빈 자리를 기준으로 오른쪽에는 노드가 없어야 함
"""


# 최대 힙
class Heap:
    """
        힙의 기반 자료 구조로 '배열'을 사용하는 이유
            힙 삽입, 삭제 연산의 핵심은 마지막 노드를 찾는 것
                마지막 노드를 사용해 삽입, 삭제 연산을 처리하는 이유
                    균형 잡힌 힙을 유지해 삽입, 삭제 연산을 O(logN)만에 처리하기 위함
                    힙의 균형이 깨지면 삽입, 삭제 연산을 O(logN)에 처리할 수 없고, 힙 조건 중 하나인 '완전 트리'에도 부합하지 않음
            마지막 노드를 효율적으로 찾기 위해 내부적으로 배열을 사용할 수 있음
                힙을 배열로 구현하는 이유
                    마지막 노드 문제 해결 : 마지막 노드를 항상 배열의 마지막 원소로 저장함
                        배열의 마지막 원소에 접근만하면 마지막 노드를 쉽게 찾을 수 있음
    """
    def __init__(self):
        self.data = []  # 내부 자료 구조 : 배열
        return

    # 루트 노드 반환
    def get_root_node(self):
        return self.data[0]

    # 마지막 노드 반환
    def get_last_node(self):
        return self.data[-1]

    '''
        왼쪽 자식 노드의 인덱스 반환
            부모 노드의 인덱스를 받아 왼쪽 자식 노드의 인덱스를 반환함
            왼쪽 자식 노드의 인덱스 = 부모 노드 인덱스 * 2 + 1
    '''
    def get_left_child_index(self, parent_idx):
        return parent_idx * 2 + 1

    '''
        오른쪽 자식 노드의 인덱스 반환
            부모 노드의 인덱스를 받아 오른쪽 자식 노드의 인덱스를 반환함
            오른쪽 자식 노드의 인덱스 = 부모 노드 인덱스 * 2 + 2
    '''
    def get_right_child_index(self, parent_idx):
        return parent_idx * 2 + 2

    '''
        부모 노드의 인덱스 반환
            자식 노드의 인덱스를 받아 부모 노드의 인덱스를 반환함
            부모 노드 인덱스 = (자식 노드 인덱스 - 1) / 2
                2로 나눌 때 소수점 버림
    '''
    def get_parent_index(self, child_idx):
        return (child_idx - 1) // 2

    '''
        힙 삽입 알고리즘
            삽입할 노드를 생성하고 마지막 노드로 삽입함
            삽입한 노드와 그 부모 노드를 비교함
                삽입한 노드의 데이터가 더 크다면 삽입한 노드와 부모 노드를 스왑함
            삽입한 노드의 데이터보다 큰 데이터를 갖는 부모 노드를 만날 때까지 스왑을 반복해서 삽입한 노드를 힙 위로 끌어 올림
            시간 복잡도 : O(logN)
    '''
    def insert(self, value):
        # 마지막 노드로 삽입
        self.data.append(value)

        # 삽입한 노드의 인덱스 : 마지막 인덱스
        new_node_idx = len(self.data) - 1

        # 삽입한 노드의 부모 노드 인덱스
        parent_idx = self.get_parent_index(new_node_idx)

        # 트리클링 : 힙 위로 올리기
        while (new_node_idx > 0 and
               self.data[new_node_idx] > self.data[parent_idx]):

            # 삽입한 노드의 데이터가 부모 노드의 데이터보다 크다면 부모 노드와 스왑함
            self.data[parent_idx], self.data[new_node_idx] = (
                self.data[new_node_idx], self.data[parent_idx]
            )

            # 삽입한 노드 인덱스 업데이트
            #   스왑 결과 삽입한 노드가 기존의 부모 노드가 있던 곳에 위치하게 됨
            new_node_idx = parent_idx

            # 삽입한 노드의 부모 노드 인덱스 업데이트
            #   삽입한 노드가 기존의 부모 노드가 있던 곳에 위치하므로 부모 노드 인덱스를 업데이트해야 함
            parent_idx = self.get_parent_index(new_node_idx)

        return

    '''
        힙 삭제 알고리즘
            힙 삭제 알고리즘은 힙 자료 구조 특성상 항상 루트 노드를 삭제함
                우선순위 큐의 기반 자료 구조로 활용하기 위함
            루트 노드 삭제 방법 : 루트 노드를 마지막 노드로 대체함
            루트 노드가 된 마지막 노드(트리클 노드)를 적절한 자리까지 아래로 트리클링함(끌어내림)
            시간 복잡도 : O(logN)
    '''
    def delete(self):
        # 힙에 노드가 1개만 있다면 바로 삭제
        if len(self.data) == 1:
            return self.data.pop()

        # 삭제할 노드 : 루트 노드
        deleted_node = self.data[0]

        # 루트 노드 삭제 : 루트 노드를 마지막 노드로 대체함
        self.data[0] = self.data.pop()

        # 트리클 노드(루트 노드가 된 마지막 노드)의 인덱스
        trickle_node_idx = 0

        # 트리클링 : 힙 아래로 내리기
        while self.has_greater_child(trickle_node_idx):
            # 두 자식 노드 중에서 더 큰 데이터를 갖는 자식 노드의 인덱스
            larger_child_idx = self.get_larger_child_index(trickle_node_idx)

            # 트리클 노드와 더 큰 자식 노드 스왑
            self.data[trickle_node_idx], self.data[larger_child_idx] = (
                self.data[larger_child_idx], self.data[trickle_node_idx]
            )

            # 트리클 노드 인덱스 업데이트
            #   스왑 결과 트리클 노드가 기존의 자식 노드가 있던 곳에 위치하게 됨
            trickle_node_idx = larger_child_idx

        # 삭제한 노드 리턴
        return deleted_node

    # 트리클 노드의 두 자식 노드가 있는지, 있다면 트리클 노드보다 큰 데이터를 갖는지 확인
    def has_greater_child(self, index):
        left_child_idx = self.get_left_child_index(index)
        right_child_idx = self.get_right_child_index(index)

        return ((left_child_idx < len(self.data) and self.data[left_child_idx] > self.data[index]) or
                (right_child_idx < len(self.data) and self.data[right_child_idx] > self.data[index]))

    # 트리클 노드의 두 자식 노드 중 더 큰 값을 갖는 자식 노드의 인덱스 반환
    def get_larger_child_index(self, index):
        left_child_idx = self.get_left_child_index(index)
        right_child_idx = self.get_right_child_index(index)

        # 오른쪽 자식 노드가 없으면 왼쪽 자식 노드의 인덱스 반환
        if right_child_idx >= len(self.data):
            return left_child_idx

        # 오른쪽 자식 노드가 더 크면 오른쪽 자식 노드 인덱스 반환
        if self.data[right_child_idx] > self.data[left_child_idx]:
            return right_child_idx
        # 왼쪽 자식 노드가 더 크면 왼쪽 자식 노드 인덱스 반환
        else:
            return left_child_idx


