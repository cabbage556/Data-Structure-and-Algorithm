function twoSum(array) {
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array.length; j++) {
            if (i !== j && array[i] + array[j] === 10) {
                return true;
            }
        }
    }

    return false;
}

function twoSum2(array) {
    let hashTable = {};

    for (let i = 0; i < array.length; i++) {
        // 현재 숫자와 더했을 때 더해서 10이 되는 숫자가
        // 해시 테이블의 키로 있는지 확인한다.
        if (hashTable[10 - array[i]]) {
            return true;
        }

        hashTable[array[i]] = true;
    }

    return false;
}
