from 정점 import Vertex


# 깊이 우선 탐색(DFS) 그래프 순회
def dfs_traverse(vertex, visited=dict()):
    # 현재 정점에 방문 표시
    visited[vertex.val] = True

    # 방문 중인 정점의 값 출력
    print("현재 정점:", vertex.val)

    # 인접 정점 순회
    for adjacent in vertex.adjacent_vertices:
        # 이미 방문했다면 무시함
        if visited.get(adjacent.val):
            continue

        # 방문하지 않았으면 DFS 순회
        dfs_traverse(adjacent, visited)

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

print("========== 깊이 우선 탐색 순회 ==========")
dfs_traverse(alice)

