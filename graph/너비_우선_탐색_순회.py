from 정점 import Vertex
from collections import deque


# 너비 우선 탐색(BFS) 그래프 순회
def bfs_traverse(vertex):
    q = deque([])     # BFS에 사용할 큐 생성
    visited = dict()  # 방문 기록을 저장하기 위한 해시 테이블 생성

    visited[vertex.val] = True  # 현재 정점에 방문 표시
    q.append(vertex)            # 큐에 현재 정점 추가

    # 큐가 빌 때까지 while 루프 실행
    while q:
        current_vtx = q.popleft()  # 현재 정점
        print(current_vtx.val)

        # 현재 정점의 인접 정점 순회
        for adjacent in current_vtx.adjacent_vertices:
            # 이미 방문했다면 무시함
            if visited.get(adjacent.val):
                continue

            # 방문하지 않았다면 방문 표시 후 큐에 추가
            visited[adjacent.val] = True
            q.append(adjacent)

    return


# 정점 생성
alice = Vertex("Alice")
bob = Vertex("Bob")
candy = Vertex("Candy")
derek = Vertex("Derek")
elaine = Vertex("Elaine")
fred = Vertex("Fred")
gina = Vertex("Gina")
helen = Vertex("Helen")
irena = Vertex("Irena")

# 앨리스 인접 정점 추가
alice.add_adjacent_vertex_in_undirected_graph(bob)
alice.add_adjacent_vertex_in_undirected_graph(candy)
alice.add_adjacent_vertex_in_undirected_graph(derek)
alice.add_adjacent_vertex_in_undirected_graph(elaine)

# 밥 인접 정점 추가
bob.add_adjacent_vertex_in_undirected_graph(fred)

# 캔디 인접 정점 추가
candy.add_adjacent_vertex_in_undirected_graph(alice)
candy.add_adjacent_vertex_in_undirected_graph(helen)

# 데릭 인접 정점 추가
derek.add_adjacent_vertex_in_undirected_graph(alice)
derek.add_adjacent_vertex_in_undirected_graph(elaine)
derek.add_adjacent_vertex_in_undirected_graph(gina)

# 일레인 인접 정점 추가
elaine.add_adjacent_vertex_in_undirected_graph(alice)
elaine.add_adjacent_vertex_in_undirected_graph(derek)

# 프레드 인접 정점 추가
fred.add_adjacent_vertex_in_undirected_graph(bob)
fred.add_adjacent_vertex_in_undirected_graph(helen)

# 지나 인접 정점 추가
gina.add_adjacent_vertex_in_undirected_graph(derek)
gina.add_adjacent_vertex_in_undirected_graph(irena)

# 헬렌 인접 정점 추가
helen.add_adjacent_vertex_in_undirected_graph(helen)
helen.add_adjacent_vertex_in_undirected_graph(candy)

# 이레나 인접 정점 추가
irena.add_adjacent_vertex_in_undirected_graph(gina)

print("========== 너비 우선 탐색 순회 ==========")
bfs_traverse(alice)
