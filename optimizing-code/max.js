function max(array) {
    let greatestNumber = array[0];

    array.forEach((number) => {
        // 탐욕 알고리즘은 그 순간에 이용할 수 있는 정보를 바탕으로 최선처럼 보이는 방법을 선택
        if (number > greatestNumber) {
            greatestNumber = number;
        }
    });

    return greatestNumber;
}
