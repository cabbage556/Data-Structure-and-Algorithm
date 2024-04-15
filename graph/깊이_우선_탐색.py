from 정점 import Vertex


# 깊이 우선 탐색(Depth-First Search)
def dfs(vertex, search_val, visited=dict()):
    # 정점을 찾았으면 정점 리턴
    if search_val == vertex.val:
        return vertex

    # 현재 정점 방문 표시
    visited[vertex.val] = True

    # 인접 정점 순회
    for adjacent in vertex.adjacent_vertices:
        # 이미 방문했다면 무시함
        if visited.get(adjacent.val):
            continue

        # 방문하지 않았으면 dfs 재귀 호출
        vertex_were_searching_for = dfs(adjacent, search_val, visited)

        # 재귀 호출 결과 정점이 있으면 해당 정점 리턴
        if vertex_were_searching_for:
            return vertex_were_searching_for

    # 찾지 못했다면 None 리턴
    return None


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

# 깊이 우선 탐색(DFS)
print("========== 깊이 우선 탐색 ==========")
searched_vertex = dfs(alice, "Fred")
print("Fred 탐색:", searched_vertex.val)

searched_vertex = dfs(alice, "Irena")
print("Irena 탐색:", searched_vertex.val)

searched_vertex = dfs(alice, "Apple")
print("Apple 탐색:", searched_vertex.val if searched_vertex else None)

