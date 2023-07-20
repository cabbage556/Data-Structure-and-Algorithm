// 배열에 상승세 주가 3개가 존재하는지 확인하는 함수를 탐욕 알고리즘으로 구현
function increasingTriplet(array) {
    let lowestPrice = array[0];
    let middlePrice = Infinity;

    for (let i = 0; i < array.length; i++) {
        const price = array[i]; // 현재 주가

        // 현재 주가가 최저가보다 작은 경우(상승세 최저가)
        if (price <= lowestPrice) {
            lowestPrice = price;
        }
        // 현재 주가가 최저가보다 크지만 중간 주가보다 작은 경우(상승세 중간 주가)
        else if (price <= middlePrice) {
            middlePrice = price;
        }
        // 현재 주가가 중간 주가보다 큰 경우(상승세 최고가)
        else {
            return true;
        }
    }

    return false;
}
