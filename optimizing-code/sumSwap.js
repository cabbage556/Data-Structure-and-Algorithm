function sumSwap(array1, array2) {
    let hashTable = {};
    let sum1 = 0;
    let sum2 = 0;

    // 첫 번째 배열의 합을 구하면서
    // 각 값을 인덱스와 함께 해시 테이블에 저장한다.
    array1.forEach((num, i) => {
        sum1 += num;
        hashTable[num] = i;
    });

    // 두 번째 배열의 합을 구한다.
    array2.forEach((num) => (sum2 += num));

    // 두 번째 배열 내 숫자가 얼만큼 변해야 할지 계산한다.
    const shiftAmount = (sum1 - sum2) / 2;

    // 두 번째 배열의 각 숫자를 순회한다.
    for (let i = 0; i < array2.length; i++) {
        // 현재 숫자에 변해야 하는 양을 더한 보수가
        // 첫 번째 배열에 있는지 해시 테이블에서 확인한다.
        if (hashTable[array2[i] + shiftAmount]) {
            return [hashTable[array2[i] + shiftAmount], i];
        }
    }

    return null;
}

console.log(sumSwap([5, 3, 3, 7], [4, 1, 1, 6]));
