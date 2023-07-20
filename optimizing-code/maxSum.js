// 배열의 최대 부분 합을 탐욕 알고리즘으로 구현
function maxSum(array) {
    let currentSum = 0;
    let greatestSum = 0;

    array.forEach((number) => {
        // 현재 합이 음수면 현재 합을 0으로 되돌린다.
        if (currentSum + number < 0) {
            currentSum = 0;
        } else {
            currentSum += number;

            // 현재 합이 지금까지의 최대 합이라면
            // 현재 합을 최대 합이라고 가정한다.
            greatestSum = currentSum > greatestSum ? currentSum : greatestSum;
        }
    });

    return greatestSum;
}

console.log(maxSum([3, -4, 4, -3, 5, -9]));
