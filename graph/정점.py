# 그래프의 정점(vertex) 클래스
class Vertex:
    def __init__(self, val):
        self.val = val  # 정점이 포함하는 값
        self.adjacent_vertices = []  # 인접 정점들을 포함하는 배열

    # 방향 그래프에서 정점의 인접 정점 추가
    def add_adjacent_vertex_in_directed_graph(self, vertex):
        self.adjacent_vertices.append(vertex)

    # 무방향 그래프에서 정점의 인접 정점 추가
    def add_adjacent_vertex_in_undirected_graph(self, vertex):
        # 이미 인접 정점에 추가했다면 종료
        if vertex in self.adjacent_vertices:
            return

        # 메서드를 호출한 정점의 인접 정점을 추가
        self.adjacent_vertices.append(vertex)

        # 인접 정점의 인접 정점으로 메서드를 호출한 정점을 추가
        vertex.add_adjacent_vertex_in_undirected_graph(vertex=self)


# 방향 그래프
#   관계의 방향을 갖는 그래프
alice = Vertex("Alice")
bob = Vertex("Bob")
cynthia = Vertex("cynthia")

# 앨리스 -> 밥, 신시아
alice.add_adjacent_vertex_in_directed_graph(bob)
alice.add_adjacent_vertex_in_directed_graph(cynthia)

# 밥 <-> 신시아
bob.add_adjacent_vertex_in_directed_graph(cynthia)
cynthia.add_adjacent_vertex_in_directed_graph(bob)

print("========== 방향 그래프 인접 정점 확인 ==========")
# 앨리스의 인접 정점 확인
for vtx in alice.adjacent_vertices:
    print("앨리스가 팔로우한 사람", vtx.val)

# 밥의 인접 정점 확인
for vtx in bob.adjacent_vertices:
    print("밥이 팔로우한 사람", vtx.val)

# 신시아의 인접 정점 확인
for vtx in cynthia.adjacent_vertices:
    print("신시아가 팔로우한 사람", vtx.val)

# 무방향 그래프
#   관계의 방향을 갖지 않는 그래프
alice2 = Vertex("Alice2")
bob2 = Vertex("Bob2")
cynthia2 = Vertex("cynthia2")

# 앨리스 - 밥
alice2.add_adjacent_vertex_in_undirected_graph(bob2)

# 밥 - 신시아
bob2.add_adjacent_vertex_in_undirected_graph(cynthia2)

# 신시아 - 앨리스
cynthia2.add_adjacent_vertex_in_undirected_graph(alice2)

print("========== 무방향 그래프 인접 정점 확인 ==========")
# 앨리스의 인접 정점 확인
for vtx in alice2.adjacent_vertices:
    print("엘리스가 팔로우한 사람", vtx.val)

# 밥의 인접 정점 확인
for vtx in bob2.adjacent_vertices:
    print("밥이 팔로우한 사람", vtx.val)

# 신시아의 인접 정점 확인
for vtx in cynthia2.adjacent_vertices:
    print("신시아가 팔로우한 사람", vtx.val)
