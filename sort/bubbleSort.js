function bubbleSort(array) {
  let sorted = false;
  let unsortedUntilIndex = array.length - 1;

  while (!sorted) {
    sorted = true;

    for (let i = 0; i < unsortedUntilIndex; i++) {
      if (array[i] > array[i + 1]) {
        let temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
        sorted = false;
      }
    }

    unsortedUntilIndex -= 1;
  }

  return array;
}

console.log(bubbleSort([4, 2, 7, 1, 3]));
