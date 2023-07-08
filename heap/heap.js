// 배열 기반 힙
// 힙으로 우선순위 큐 구현
class Heap {
  constructor() {
    this.data = [];
  }

  rootNode() {
    return this.data[0];
  }

  lastNode() {
    return this.data[this.data.length - 1];
  }

  leftChildIndex(index) {
    return index * 2 + 1;
  }

  rightChildIndex(index) {
    return index * 2 + 2;
  }

  parentIndex(index) {
    return Math.floor((index - 1) / 2);
  }

  // 힙 삽입
  insert(value) {
    // value를 배열 끝에 삽입해 마지막 노드로 만든다.
    this.data.push(value);

    // 새로 삽입한 노드의 인덱스를 저장한다.
    let newNodeIndex = this.data.length - 1;

    // "위로 트리클링" 알고리즘 실행
    // 새 노드가 루트 자리에 없고 새 노드가 부모 노드보다 크면
    while (
      newNodeIndex > 0 &&
      this.data[newNodeIndex] > this.data[this.parentIndex(newNodeIndex)]
    ) {
      // 새 노드와 부모 노드를 스왑한다.
      let temp = this.data[this.parentIndex(newNodeIndex)];
      this.data[this.parentIndex(newNodeIndex)] = this.data[newNodeIndex];
      this.data[newNodeIndex] = temp;

      // 새 노드의 인덱스 업데이트
      newNodeIndex = this.parentIndex(newNodeIndex);
    }
  }

  // 힙 삭제
  delete() {
    // 힙에서는 루트 노드만 삭제한다.
    // 배열에서 마지막 노드를 팝해 루트 노드로 넣는다.
    this.data[0] = this.data.pop();

    // 트리클링 노드의 현재 인덱스(현재 루트 노드에 위치) 기록
    let tricleNodeIndex = 0;

    // "아래로 트리클링" 알고리즘 실행
    // 트리클 노드에 자기보다 큰 자식이 있으면 루프 실행
    while (this.hasGreaterChild(tricleNodeIndex)) {
      // 더 큰 자식의 인덱스를 변수에 저장
      let largerChildIndex = this.calculateLargerChildIndex(tricleNodeIndex);

      // 트리클 노드와 더 큰 자식 노드 스왑
      let temp = this.data[largerChildIndex];
      this.data[largerChildIndex] = this.data[tricleNodeIndex];
      this.data[tricleNodeIndex] = temp;

      // 트리클 노드의 새 인덱스 업데이트
      tricleNodeIndex = largerChildIndex;
    }
  }

  // 자기보다 큰 자식이 있으면 루프 실행
  hasGreaterChild(index) {
    // index에 있는 노드에 왼쪽 자식이나 오른쪽 자식이 있는지
    // 어느 한 자식이라도 index에 있는 노드보다 큰지 확인
    return (
      (this.data[this.leftChildIndex(index)] &&
        this.data[this.leftChildIndex(index)] > this.data[index]) ||
      (this.data[this.rightChildIndex(index)] &&
        this.data[this.rightChildIndex(index)] > this.data[index])
    );
  }

  calculateLargerChildIndex(index) {
    // 오른쪽 자식이 없으면 왼쪽 자식 인덱스 리턴
    if (!this.data[this.rightChildIndex(index)]) {
      return this.leftChildIndex(index);
    }

    // 오른쪽 자식의 값이 왼쪽 자식의 값보다 크면
    // 오른쪽 자식 인덱스 리턴
    if (
      this.data[this.rightChildIndex(index)] >
      this.data[this.leftChildIndex(index)]
    ) {
      return this.rightChildIndex(index);
    }
    // 왼쪽 자식의 값이 오른쪽 자식의 값보다 크거나 같으면
    // 왼쪽 자식 인덱스 리턴
    else {
      return this.leftChildIndex(index);
    }
  }
}

const heap = new Heap();

heap.insert(100);
heap.insert(80);
heap.insert(105);
heap.insert(120);
heap.delete();

console.log(heap);
