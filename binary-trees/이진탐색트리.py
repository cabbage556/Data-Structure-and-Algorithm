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