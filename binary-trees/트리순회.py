# 트리 중위 순회
#   이진 탐색 트리의 모든 노드를 방문해 오름차순으로 노드의 값을 출력하기
def inorder_traverse(node):
    # 기저 조건: 자식이 없는 노드
    if node is None:
        return

    inorder_traverse(node.left)   # 왼쪽 자식 노드에 대해 재귀 호출
    print(node.val)                 # 현재 노드의 값 출력
    inorder_traverse(node.right)  # 오른쪽 자식 노드에 대해 재귀 호출


# 트리 전위 순회
def preorder_traverse(node):
    if node is None:
        return

    print(node.val)
    preorder_traverse(node.left)
    preorder_traverse(node.right)


# 트리 후위 순회
def postorder_traverse(node):
    if node is None:
        return

    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print(node.val)

