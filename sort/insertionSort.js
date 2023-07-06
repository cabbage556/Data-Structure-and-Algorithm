function insertionSort(array) {
  // 패스스루
  for (let i = 1; i < array.length; i++) {
    let tempValue = array[i]; // 패스스루의 임시 제거 값
    let position = i - 1; // 임시 제거 값의 바로 왼쪽 인덱스 초기화

    // 시프트 단계
    while (position >= 0) {
      // 왼쪽 인덱스의 값이 임시 제거 값보다 큰 경우
      if (array[position] > tempValue) {
        array[position + 1] = array[position]; // 오른쪽 시프트
        position -= 1; // 인덱스 1 감소
      }
      // 왼쪽 인덱스의 값이 임시 제거 값보다 작은 경우 시프트 단계 종료
      else {
        break;
      }
    }

    // 공백에 임시 제거 값 삽입
    array[position + 1] = tempValue;
  }

  return array;
}

console.log(insertionSort([4, 2, 1, 7, 3]));
