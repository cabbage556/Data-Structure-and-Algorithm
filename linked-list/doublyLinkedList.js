// 이중 연결 리스트의 노드
class Node {
  constructor(data) {
    this.data = data; // 노드가 저장하는 데이터
    this.nextNode = null; // 다음 노드로의 링크
    this.prevNode = null; // 이전 노드로의 링크
  }
}

// 이중 연결 리스트
class DoublyLinkedList {
  constructor(firstNode = null, lastNode = null) {
    this.firstNode = firstNode; // 이중 연결 리스트의 첫 번째 노드
    this.lastNode = lastNode; // 이중 연결 리스트의 마지막 노드
  }

  insertAtEnd(value) {
    const newNode = new Node(value);

    // 연결 리스트에 아직 원소가 없을 때
    if (!this.firstNode) {
      this.firstNode = newNode;
      this.lastNode = newNode;
    }
    // 연결 리스트에 원소가 하나 이상 있을 때
    else {
      newNode.prevNode = this.lastNode; // 새 노드의 이전 노드가 현재 마지막 노드를 가리키게 함
      this.lastNode.nextNode = newNode; // 현재 마지막 노드의 다음 노드가 새 노드를 가리키게 함
      this.lastNode = newNode; // 마지막 노드에 새 노드를 할당함
    }
  }

  removeFromFront() {
    const removedNode = this.firstNode; // 이중 연결 리스트의 첫 번째 노드 제거
    this.firstNode = this.firstNode.nextNode; // 현재 첫 번째 노드의 다음 노드가 첫 번째 노드가 됨
    return removedNode; // 첫 번째 노드 리턴
  }
}

// 이중 연결 리스트 기반 큐
class Queue {
  constructor() {
    this.list = new DoublyLinkedList();
  }

  enqueue(element) {
    this.list.insertAtEnd(element); // 이중 연결 리스트 마지막에 노드 삽입
  }

  dequeue() {
    const removedNode = this.list.removeFromFront(); // 이중 연결 리스트 첫 번째 노드 제거
    return removedNode.data; // 첫 번째 노드가 저장한 데이터 리턴
  }

  read() {
    if (!this.list.firstNode) {
      return null;
    }

    return this.list.firstNode.data;
  }
}
