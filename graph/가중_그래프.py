# 가중 그래프 정점
#   해시 테이블을 사용해 인접 정점을 표현하는 방식을 사용함
class WeightedGraphVertex:
    def __init__(self, val):
        self.val = val

        # 해시 테이블
        #   키: 인접 정점
        #   값: 현재 정점에서 인접 정점으로 이어지는 간선의 가중치
        self.adjacent_vertices = dict()

    def add_adjacent_vertex(self, vertex, weight):
        self.adjacent_vertices[vertex] = weight
        return


dallas = WeightedGraphVertex("dallas")
toronto = WeightedGraphVertex("toronto")

# 댈러스 -> 토론토: 138달러
dallas.add_adjacent_vertex(toronto, 138)

# 토론토 -> 댈러스: 216달러
toronto.add_adjacent_vertex(dallas, 216)
