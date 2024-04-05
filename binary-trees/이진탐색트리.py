# 이진 탐색 트리를 구성하는 노드
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val      # 실제 데이터
        self.left = left    # 왼쪽 자식
        self.right = right  # 오른쪽 자식


# 이진 탐색 트리
#   조건
#       각 노드마다 왼쪽 자식 최대 1개, 오른쪽 자식 최대 1개
#       한 노드의 왼쪽 자손들은 그 노드 보다 작은 값을 가짐
#       한 노드의 오른쪽 자손들은 그 노드 보다 큰 값을 가짐

# 이진 탐색 트리 검색
#   시간 복잡도: O(logN)
def search_binary_tree(search_val, node):
    # 기저 조건
    #       노드가 없거나, 찾는 값인 경우
    if node is None or node.val == search_val:
        return node
    # 찾는 값이 현재 노드의 값보다 작으면 왼쪽 자식 검색
    elif search_val < node.val:
        return search_binary_tree(search_val, node.left)
    # 찾는 값이 현재 노드의 값보다 크면 오른쪽 자식 검색
    else:
        return search_binary_tree(search_val, node.right)


# 이진 탐색 트리 삽입
#   시간 복잡도: O(logN)
def insert_binary_tree(val, node):
    # 삽입하는 값이 현재 노드의 값보다 작은 경우
    if val < node.val:
        # 왼쪽 자식이 없으면 왼쪽 자식으로 삽입
        if node.left is None:
            node.left = TreeNode(val)
        else:
            insert_binary_tree(val, node.left)
    # 삽입하는 값이 현재 노드의 값보다 큰 경우
    elif val > node.val:
        # 오른쪽 자식이 없으면 오른쪽 자식으로 삽입
        if node.right is None:
            node.right = TreeNode(val)
        else:
            insert_binary_tree(val, node.right)


# 이진 탐색 트리 삭제 알고리즘
#   삭제할 노드에 자식이 없으면 그냥 삭제한다.
#   삭제할 노드에 자식이 하나면 노드를 삭제하고, 자식을 삭제할 노드가 있던 위치에 넣는다.
#   자식이 둘인 노드를 삭제할 때는 삭제할 노드를 후속자 노드로 대체한다.
#       후속자 노드를 찾으려면 삭제할 노드의 오른쪽 자식을 먼저 방문한다.
#       방문한 오른쪽 자식의 왼쪽 자식들을 계속 따라 방문해 더 이상 왼쪽 자식이 없을 때까지 내려간다.
#       더 이상 왼쪽 자식이 없는 노드가 후속자 노드이다.
#       후속자 노드에 오른쪽 자식이 있는 경우
#           먼저 후속자 노드를 삭제할 노드가 있는 자리에 넣는다.
#           그리고 후속자 노드의 오른쪽 자식을 후속자 노드의 원래 부모의 왼쪽 자식으로 넣는다.

# 이진 탐색 트리 삭제
#   시간 복잡도: O(logN)
def delete_binary_tree(value_to_delete, node):
    # 기저 조건: 트리 바닥에 도달해 자식 노드가 없는 경우
    if node is None:
        return None

    # 삭제하려는 노드가 현재 노드보다 작은 경우
    #   현재 노드의 왼쪽 하위 트리에 삭제하려는 노드가 존재함
    elif value_to_delete < node.val:

        # 현재 노드의 왼쪽 하위 트리에 대한 재귀 호출의 반환값을
        # 현재 노드의 왼쪽 자식에 할당함
        node.left = delete_binary_tree(value_to_delete, node.left)

        # 현재 노드와 그 하위 트리를 반환하여
        # 현재 노드의 부모 노드의 왼쪽 자식으로 쓰이게 함
        return node

    # 삭제하려는 노드가 현재 노드보다 큰 경우
    #   현재 노드의 오른쪽 하위 트리에 삭제하려는 노드가 존재함
    elif value_to_delete > node.val:

        # 현재 노드의 오른쪽 하위 트리에 대한 재귀 호출의 반환값을
        # 현재 노드의 오른쪽 자식에 할당함
        node.right = delete_binary_tree(value_to_delete, node.right)

        # 현재 노드와 그 하위 트리를 반환하여
        # 현재 노드의 부모 노드의 오른쪽 자식으로 쓰이게 함
        return node

    # 현재 노드가 삭제하려는 노드인 경우
    elif value_to_delete == node.val:

        # 현재 노드에 왼쪽 자식이 없는 경우
        #   현재 노드의 오른쪽 자식(+ 그 하위 트리)을 현재 노드의 부모 노드에 반환하여 현재 노드를 삭제함
        #   현재 노드의 오른쪽 자식(+ 그 하위 트리)가 없더라도 None을 반환하므로 현재 노드가 삭제됨
        if node.left is None:
            return node.right

        # 현재 노드에 오른쪽 자식이 없는 경우
        #   현재 노드의 왼쪽 자식(+ 그 하위 트리)을 현재 노드의 부모 노드에 반환하여 현재 노드를 삭제함
        #   현재 노드의 왼쪽 자식(+ 그 하위 트리)가 없더라도 None을 반환하므로 현재 노드가 삭제됨
        elif node.right is None:
            return node.left

        # 현재 노드에 왼쪽, 오른쪽 자식이 모두 있는 경우
        #   오른쪽 자식을 방문해 후속자 노드를 찾고,
        #   현재 노드를 후속자 노드로 대체해 현재 노드를 삭제함
        else:
            node.right = lift(node.right, node)
            return node


# 후속자 노드를 찾고, 삭제하려는 노드를 후속자 노드로 대체하기
def lift(node, node_to_delete):

    # 현재 노드에 왼쪽 자식이 있는 경우
    #   왼쪽 하위 트리로 계속 내려가도록 재귀 호출하여
    #   후속자 노드를 찾음
    if node.left:
        node.left = lift(node.left, node_to_delete)
        return node

    # 현재 노드에 왼쪽 자식이 없는 경우
    #   현재 노드가 후속자 노드라는 의미
    else:
        # 후속자 노드를 삭제하려는 노드가 위치한 자리에 넣음
        #   후속자 노드로 삭제하려는 노드를 대체하는 것
        node_to_delete.val = node.val

        # 후속자 노드의 오른쪽 자식를 반환하여
        # 후속자 노드의 오른쪽 자식이 후속자 노드의 부모 노드의 왼쪽 자식으로 쓰일 수 있게 함
        return node.right









