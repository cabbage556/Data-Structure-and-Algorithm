class TreeNode {
  constructor(value, left = null, right = null) {
    this.value = value;
    this.leftChild = left;
    this.rightChild = right;
  }
}

const treeNode1 = new TreeNode(25);
const treeNode2 = new TreeNode(75);
const rootNode = new TreeNode(50, treeNode1, treeNode2);

// 이진 탐색 트리 검색
function searchInBinaryTree(searchValue, node) {
  // 기저 조건: 노드가 없거나 찾고 있는 값이면
  if (node === null || node.value === searchValue) {
    return node;
  }
  // 찾고 있는 값이 현재 노드보다 작으면 왼쪽 자식 검색
  else if (searchValue < node.value) {
    return search(searchValue, node.leftChild);
  }
  // 찾고 있는 값이 현재 노드보다 크면 오른쪽 자식 검색
  else {
    return search(searchValue, node.rightChild);
  }
}

// 이진 탐색 트리 삽입
function insertInBinaryTree(value, node) {
  if (value < node.value) {
    // 왼쪽 자식이 없으면 왼쪽 자식으로서 값 삽입
    if (!node.leftChild) {
      node.leftChild = new TreeNode(value);
    } else {
      insert(value, node.leftChild);
    }
  } else if (value > node.value) {
    // 오른쪽 자식이 없으면 오른쪽 자식으로서 값 삽입
    if (!node.rightChild) {
      node.rightChild = new TreeNode(value);
    } else {
      insert(value, node.rightChild);
    }
  }
}

// 이진 탐색 트리 삭제
function deleteInBinaryTree(valueToDelete, node) {
  // 기저 조건: 트리 바닥에 도달하여 노드가 실제로 없는 경우(재귀 호출에서 존재하지 않는 자식 노드에 접근하는 경우)
  if (!node) {
    return null;
  }
  // 삭제하려는 값이 현재 노드보다 작은 경우
  // 현재 노드의 왼쪽 하위 트리에 삭제하려는 값이 있다.
  else if (valueToDelete < node.value) {
    // 현재 노드의 왼쪽 하위 트리에 대한 재귀 호출의 반환값을 현재 노드의 왼쪽 자식에 할당한다.
    // 재귀 호출 결과가 결과적으로 노드를 반환하므로 현재 노드의 왼쪽 자식으로 넣는 것이다.
    node.leftChild = deleteInBinaryTree(valueToDelete, node.leftChild);

    // 현재 노드(와 존재한다면 그 하위 트리)를 반환해서
    // 현재 노드의 부모의 왼쪽 또는 오른쪽 자식의 새로운 값으로 쓰이게 한다.
    return node;
  }
  // 삭제하려는 값이 현재 노드보다 크면
  // 현재 노드의 오른쪽 하위 트리에 대한 재귀 호출의 반환값을 오른쪽 자식에 할당한다.
  else if (valueToDelete > node.value) {
    node.rightChild = deleteInBinaryTree(valueToDelete, node.rightChild);
    return node;
  }
  // 현재 노드가 삭제하려는 노드인 경우
  else if (valueToDelete === node.value) {
    // 현재 노드에 왼쪽 자식이 없으면
    // 오른쪽 자식(과 존재한다면 그 하위 트리)을
    // 현재 노드의 부모의 새 하위 트리로 반환함으로써 현재 노드를 삭제한다.
    // 현재 노드의 오른쪽 자식이 없더라도 null을 리턴하므로 문제 없이 현재 노드가 삭제된다.
    if (!node.leftChild) {
      return node.rightChild;
    }
    // 현재 노드에 오른쪽 자식이 없으면
    // 왼쪽 자식(과 존재한다면 그 하위 트리)을
    // 현재 노드의 부모의 새 하위 트리로 반환함으로써 현재 노드를 삭제한다.
    else if (!node.rightChild) {
      return node.leftChild;
    }
    // 현재 노드에 자식이 둘이면
    // 현재 노드의 값을 후속자 노드의 값으로 바꾸는
    // lift 함수를 호출함으로써 현재 노드를 삭제한다.
    else {
      node.rightChild = lift(node.rightChild, node);
      return node;
    }
  }
}

function lift(node, nodeToDelete) {
  // 이 함수의 현재 노드에 왼쪽 자식이 있으면
  // 왼쪽 하위 트리로 계속해서 내려가도록 함수를 재귀적으로 호출하여
  // 후속자 노드를 찾는다.
  if (node.leftChild) {
    node.leftChild = lift(node.leftChild, nodeToDelete);
    return node;
  }
  // 현재 노드에 왼쪽 자식이 없으면
  // 이 함수의 현재 노드가 후속자 노드라는 뜻이므로
  // 현재 노드의 값을 삭제하려는 노드의 새로운 값으로 할당한다.
  else {
    nodeToDelete.value = node.value;
    // 후속자 노드의 오른쪽 자식이 후속자 노드의 부모의 왼쪽 자식으로 쓰일 수 있도록 반환한다.
    return node.rightChild;
  }
}

// 중위 순회
function traverseAndPrint(node) {
  if (!node) {
    return;
  }

  traverseAndPrint(node.leftChild); // 왼쪽 자식 노드에 대해 재귀 호출
  console.log(node.value); // 현재 노드의 값 출력
  traverseAndPrint(node.rightChild); // 오른쪽 자식 노드에 대해 재귀 호출
}
