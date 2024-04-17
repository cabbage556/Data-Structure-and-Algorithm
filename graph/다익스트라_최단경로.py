from 다익스트라_최단경로_정점 import City


# 다익스트라 최단 경로 알고리즘
#   가중 그래프에서 최단 경로를 찾는 알고리즘
#   시간 복잡도: O(V^2)
#       V: 정점 개수
#   starting_city: 시작 도시(시작 정점)
#   destination: 목적지 도시(도착 정점)
def dijkstra_shortest_path(starting_city, destination):
    # 시작 도시부터 각 도시에 도달하는 최소 비용을 저장하는 해시 테이블
    #   키: 목적지
    #   값: 최소 비용
    cheapest_prices = dict()

    # 시작 도시부터 목적지까지 최소 비용으로 가기 위해 직전에 경유하는 경유지를 저장하는 해시 테이블
    #   키: 목적지
    #   값: 직전 경유지
    cheapest_prev_stopover_city = dict()

    # 아직 방문하지 않은 도시를 저장하는 배열
    unvisited = []

    # 방문했던 도시를 저장하는 해시 테이블
    visited = dict()

    # 시작 도시부터 시작 도시로 가는 비용: 0
    cheapest_prices[starting_city.name] = 0

    # 현재 도시 추적
    current_city = starting_city

    # 방문하지 않은 도시가 남아 있을 때까지
    while current_city:

        # 현재 도시 방문 기록, 방문하지 않은 도시 배열에서 제거
        visited[current_city.name] = True
        if current_city in unvisited:
            unvisited.remove(current_city)

        # 현재 도시의 인접 도시 순회
        #       City 인스턴스의 routes 변수: 해시 테이블
        #           키: 인접 도시
        #           값: 이동 비용
        for adjacent_city, price in current_city.routes.items():

            # 새 도시를 발견하면 unvisited에 추가
            if not visited.get(adjacent_city.name):
                unvisited.append(adjacent_city)

            # 현재 도시를 마지막으로 경유하는 도시로 사용해
            # 시작 도시에서 인접 도시로 가는 비용 계산
            price_through_current_city = (
                cheapest_prices[current_city.name] + price
            )

            # 시작 도시에서 인접 도시로 가는 비용이
            # 위에서 계산한 비용보다 저렴하면 해시 테이블 업데이트
            if (
                not cheapest_prices.get(adjacent_city.name) or
                price_through_current_city < cheapest_prices[adjacent_city.name]
            ):
                cheapest_prices[adjacent_city.name] = price_through_current_city
                cheapest_prev_stopover_city[adjacent_city.name] = current_city.name

        # 방문하지 않은 다음 도시 방문
        # 시작 도시에서 최소 비용으로 갈 수 있는 도시 선택
        current_city = unvisited[0] if len(unvisited) > 0 else None
        for i in range(1, len(unvisited)):
            if cheapest_prices[unvisited[i].name] < cheapest_prices[current_city.name]:
                current_city = unvisited[i]

    # 이제 cheapest_prices는 시작 도시에서 각 도시로 가는 최소 비용을 포함함
    # 시작 도시부터 목적지까지 가는 정확한 경로를 계산해야 함
    shortest_path = []

    # 최소 비용 경로를 구성하려면 목적지부터 거꾸로 이동함
    current_city_name = destination.name

    # 목적지부터 시작 도시에 도달할 때까지
    while current_city_name != starting_city.name:
        shortest_path.append(current_city_name)

        # 직전 경유지를 따라 올라감
        current_city_name = cheapest_prev_stopover_city[current_city_name]

    # 마지막으로 시작 도시를 최소 비용 경로에 추가
    shortest_path.append(starting_city.name)

    # 시작 도시부터 목적지까지 경로를 나타내기 위해 뒤집기
    shortest_path.reverse()
    return shortest_path


# 가중 그래프의 정점 생성
atlanta = City("애틀랜타")
boston = City("보스턴")
chicago = City("시카고")
denver = City("덴버")
el_paso = City("엘파소")

# 간선의 비용 설정
atlanta.add_route(boston, 100)   # 애틀랜타 -> 보스턴: 100
atlanta.add_route(denver, 160)
boston.add_route(chicago, 120)
boston.add_route(denver, 180)
chicago.add_route(el_paso, 80)
denver.add_route(chicago, 40)
denver.add_route(el_paso, 140)

# 애틀랜타부터 엘파소까지의 최소 비용 경로
shortest_path = dijkstra_shortest_path(atlanta, el_paso)
print(shortest_path)