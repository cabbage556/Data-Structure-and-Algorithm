function linearSearch(array, searchValue) {
  // 배열의 모든 원소 순회
  for (let i = 0; i < array.length; i++) {
    if (array[i] === searchValue) {
      return i;
    }
    // 정렬된 배열에 사용하는 검색임을 가정함
    else if (array[i] > searchValue) {
      break;
    }
  }

  return -1;
}
