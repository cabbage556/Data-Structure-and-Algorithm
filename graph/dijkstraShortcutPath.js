const City = require("./city");

function dijkstraShortcutPath(startingCity, finalDestination) {
    const cheapestPricesTable = {};
    const cheapestPreviousStopoverCityTable = {};

    // 코드가 복잡해지지 않도록
    // 아직 방문하지 않은 알려진 도시를 배열에 기록
    let unvisitedCities = [];

    // 방문했던 도시를 해시 테이블에 기록
    const visitedCities = {};

    // cheapestPricesTable의 첫 번째 키로 시작 도시 이름 추가
    // 시작 도시로 가는 비용은 없으니 값은 0
    cheapestPricesTable[startingCity.name] = 0;

    // 현재 도시
    let currentCity = startingCity;

    // 방문하지 않은 도시가 남아 있는 동안 실행
    while (currentCity) {
        // visitedCities 해시에 currentCity 이름을 추가해 방문했음을 표시
        // unvisitedCities 리스트에서는 제거
        visitedCities[currentCity.name] = true;
        unvisitedCities = unvisitedCities.filter(
            (city) => city !== currentCity
        );

        // currentCity의 인접 도시 순회
        currentCity.routes.forEach((price, adjacentCity) => {
            // 새 도시를 발견하면 unvisitedCities에 추가
            if (!visitedCities[adjacentCity.name]) {
                unvisitedCities.push(adjacentCity);
            }

            // currentCity를 마지막으로 경유하는 도시로 사용
            // startingCity에서 adjacentCity로 가는 비용 계산
            const priceThroughCurrentCity =
                cheapestPricesTable[currentCity.name] + price;

            // startingCity에서 adjacentCity로 가는 비용이
            // 현재까지 계산한 비용보다 저렴하면
            if (
                !cheapestPricesTable[adjacentCity.name] ||
                priceThroughCurrentCity < cheapestPricesTable[adjacentCity.name]
            ) {
                // 두 표를 업데이트
                cheapestPricesTable[adjacentCity.name] =
                    priceThroughCurrentCity;
                cheapestPreviousStopoverCityTable[adjacentCity.name] =
                    currentCity.name;
            }
        });

        // 방문하지 않은 도시를 방문
        // startingCity에서 갈 수 있는 가장 저렴한 도시로 선택
        currentCity = unvisitedCities.reduce((prev, cur) => {
            return cheapestPricesTable[prev.name] <
                cheapestPricesTable[cur.name]
                ? prev
                : cur;
        }, unvisitedCities[0]);
    }

    // 단순 배열로 최단 경로 생성
    const shortestPath = [];

    // 최단 경로를 구성하려면 finalDestination부터 거슬러 올라가야 한다.
    // currentCityName을 finalDestination으로 시작한다.
    let currentCityName = finalDestination.name;

    // startingCity에 도달할 때까지 루프를 실행
    while (currentCityName !== startingCity.name) {
        // 도시가 나올 때마다 각 currentCityName을 shortestPath에 추가
        shortestPath.push(currentCityName);

        // cheapestPreviousStopoverCityTable을 사용해 바로 이전 경유 도시를 따라간다.
        currentCityName = cheapestPreviousStopoverCityTable[currentCityName];
    }

    // startingCity를 shortestPath에 추가한다.
    shortestPath.push(startingCity.name);

    // 시작부터 끝까지 순서대로 경로를 나타내기 위해 출력을 뒤집는다.
    return shortestPath.reverse();
}

const atlanta = new City("Atlanta");
const boston = new City("Boston");
const chicago = new City("Chicago");
const denver = new City("Denver");
const elPaso = new City("El Paso");

atlanta.addRoute(boston, 100);
atlanta.addRoute(denver, 160);
boston.addRoute(chicago, 120);
boston.addRoute(denver, 180);
chicago.addRoute(elPaso, 80);
denver.addRoute(chicago, 40);
denver.addRoute(elPaso, 140);
elPaso.addRoute(boston, 100);

console.log(dijkstraShortcutPath(atlanta, elPaso));
