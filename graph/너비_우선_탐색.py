from 정점 import Vertex
from collections import deque


# 너비 우선 탐색(Breadth-First Search)
#   그래프 탐색 시 시작 정점과 가까운 정점들부터 탐색하고 싶은 경우 너비 우선 탐색을 사용하는 것이 좋음
#   시간 복잡도: O(V + E)
#       V: 정점 수
#       E: 간선 수
def bfs(vertex, search_val):
    q = deque([])
    visited = dict()

    visited[vertex.val] = True
    q.append(vertex)

    while q:
        current_vtx = q.popleft()
        if current_vtx.val == search_val:
            return current_vtx

        for adjacent in current_vtx.adjacent_vertices:
            if visited.get(adjacent.val):
                continue

            visited[adjacent.val] = True
            q.append(adjacent)

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

print("========== 너비 우선 탐색 ==========")
searched_vertex = bfs(alice, "Fred")
print("Fred 탐색:", searched_vertex.val)

searched_vertex = bfs(alice, "Irena")
print("Irena 탐색:", searched_vertex.val)

searched_vertex = bfs(alice, "Apple")
print("Apple 탐색:", searched_vertex.val if searched_vertex else None)
