# 다익스트라 최단 경로 알고리즘에서 사용하는 가중 그래프 정점
class City:
    def __init__(self, name):
        self.name = name      # 정점 이름
        self.routes = dict()  # 정점에서 인접 정점으로의 비용을 저장하는 해시 테이블

    def add_route(self, city, price):
        # 이 정점에서 인접 정점으로의 비용을 저장함
        self.routes[city] = price
