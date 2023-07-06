function binarySearch(array, searchValue) {
  // 찾으려는 값이 있을 수 있는 상한선과 하한선을 먼저 정한다.
  // 최초의 하한선은 배열의 첫 번째 인덱스, 상한선은 마지막 인덱스이다.
  let lowerBound = 0;
  let upperBound = array.length - 1;

  // 상한선과 하한선 사이의 가운데 값을 계속해서 확인하는 루프를 시작한다.
  while (lowerBound <= upperBound) {
    // 상한선과 하한선 사이에 중간 지점을 찾는다.
    let midPoint = Math.ceil((lowerBound + upperBound) / 2);

    // 중간 지점의 값을 확인한다.
    let valueAtMid = array[midPoint];

    // 중간 지점의 값이 찾으려는 값이면 검색을 끝낸다.
    // 그렇지 않으면 더 클지 작을지 추측한 바에 따라 상한선이나 하한선을 바꾼다.
    if (searchValue === valueAtMid) {
      return midPoint;
    } else if (searchValue < valueAtMid) {
      // 찾으려는 값이 중간 지점 값보다 작은 경우 상한선을 중간 지점 바로 왼쪽 인덱스로 변경
      upperBound = midPoint - 1;
    } else if (searchValue > valueAtMid) {
      // 찾으려는 값이 중간 지점 값보다 큰 경우 하한선을 중간 지점 바로 오른쪽 인덱스로 변경
      lowerBound = midPoint + 1;
    }
  }

  // 찾지 못하면 -1 반환
  return -1;
}

binarySearch([3, 17, 75, 80, 202], 22); // -1
