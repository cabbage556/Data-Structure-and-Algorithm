// 연결 리스트의 노드
class Node {
  constructor(data) {
    this.data = data; // 노드가 저장하는 데이터
    this.nextNode = null; // 다음 노드로의 링크
  }
}

// 연결 리스트
class LinkedList {
  constructor(firstNode) {
    this.firstNode = firstNode; // 연결 리스트의 첫 번째 노드
  }

  // 연결 리스트 읽기
  read(index) {
    // 첫 번째 노드부터 시작
    let currentNode = this.firstNode;
    let currentIndex = 0;

    while (currentIndex < index) {
      // 읽으려는 인덱스에 도착할 때까지 각 노드의 링크를 계속 따라감
      currentNode = currentNode.nextNode;
      currentIndex += 1;

      // 연결 리스트 끝에 도착했으면 찾고 있는 인덱스가 없다는 의미이므로 null 반환
      if (!currentNode) {
        return null;
      }
    }

    // 현재 노드가 저장하는 데이터 반환
    return currentNode.data;
  }

  // 연결 리스트 검색
  indexOf(value) {
    // 첫 번재 노드부터 시작
    let currentNode = this.firstNode;
    let currentIndex = 0;

    do {
      // 찾고 있는 값을 찾으면 인덱스 반환
      if (currentNode.data === value) {
        return currentIndex;
      }

      // 못찾으면 다음 노드로 이동
      currentNode = currentNode.nextNode;
      currentIndex += 1;
    } while (currentNode);

    // 값을 찾지 못한 체 리스트를 모두 순회하면 null 반환
    return null;
  }

  // 삽입
  insertAtIndex(index, value) {
    // 전달받은 value를 저장하는 새 노드 생성
    const newNode = new Node(value);

    // 리스트 앞에 삽입하는 경우
    if (index === 0) {
      newNode.nextNode = this.firstNode; // 새 노드의 링크가 현재 첫 번째 노드를 가리키게 한다.
      this.firstNode = newNode; // 첫 번째 노드를 새 노드로 변경
      return;
    }

    // 앞이 아닌 다른 위치에 삽입하는 경우
    let currentNode = this.firstNode;
    let currentIndex = 0;

    // 삽입하려는 인덱스의 바로 앞 노드까지 접근
    while (currentIndex < index - 1) {
      currentNode = currentNode.nextNode;
      currentIndex += 1;
    }

    newNode.nextNode = currentNode.nextNode; // 새 노드의 링크가 다음 노드를 가리키게 함
    currentNode.nextNode = newNode; // 새 노드를 가리키도록 앞의 노드의 링크를 수정함
  }

  // 삭제
  deleteAtIndex(index) {
    // 첫 번째 노드를 삭제하는 경우
    if (index === 0) {
      this.firstNode = this.firstNode.nextNode;
      return;
    }

    let currentNode = this.firstNode;
    let currentIndex = 0;

    // 삭제하려는 노드의 바로 앞 노드까지 찾아가 currentNode에 할당
    while (currentIndex < index - 1) {
      currentNode = currentNode.nextNode;
      currentIndex -= 1;
    }

    // 삭제하려는 노드의 바로 뒤 노드를 찾음
    // 현재 노드 - 삭제하려는 노드 - 뒤 노드
    const nodeAfterDeletedNode = currentNode.nextNode.nextNode;

    // currentNode의 링크가 nodeAfterDeleteNode를 가리키도록 수정
    // 현재 노드의 링크가 삭제하려는 노드의 바로 뒤 노드륵 가리키도록
    // 삭제하려는 노드가 리스트에서 제외됨
    currentNode.nextNode = nodeAfterDeletedNode;
  }
}
