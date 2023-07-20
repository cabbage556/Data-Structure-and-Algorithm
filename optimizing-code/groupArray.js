function groupArray(array) {
    const hashTable = {};
    const newArray = [];

    // 각 문자열의 합계를 해시 테이블에 저장
    array.forEach((value) => {
        if (hashTable[value]) {
            hashTable[value] += 1;
        } else {
            hashTable[value] = 1;
        }
    });

    // 해시 테이블을 순회하며 각 문자열의 개수만큼 새 배열에 붙이기
    for (const key in hashTable) {
        for (let i = 0; i < hashTable[key]; i++) {
            newArray.push(key);
        }
    }

    return newArray;
}

groupArray(["a", "b", "c", "b", "c"]);
