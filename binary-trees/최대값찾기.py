# 이진 탐색 트리에서 최대 값을 찾기
def find_max(node):
    # 이진 트리에서 최대 값을 갖는 노드는 항상 오른쪽 바닥에 존재함
    # 오른쪽 바닥까지 이동함
    if node.right:
        return find_max(node.right)
    # 오른쪽 자식이 없다면 오른쪽 바닥에 있는 노드에 도달했으므로 그 노드의 값 리턴
    else:
        return node.val