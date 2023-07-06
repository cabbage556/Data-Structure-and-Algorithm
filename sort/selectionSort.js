function selectionSort(array) {
  for (let i = 0; i < array.length - 1; i++) {
    let lowsestNumberIndex = i;

    for (let j = i + 1; j < array.length; j++) {
      if (array[j] < array[lowsestNumberIndex]) {
        lowsestNumberIndex = j;
      }
    }

    if (lowsestNumberIndex !== i) {
      let temp = array[i];
      array[i] = array[lowsestNumberIndex];
      array[lowsestNumberIndex] = temp;
    }
  }

  return array;
}
