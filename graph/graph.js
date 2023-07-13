// 그래프의 정점(vertex) 클래스
class Vertex {
    constructor(value) {
        this.value = value; // 자신의 값
        this.adjacentVertices = []; // 인접 정점들 저장 배열
    }

    // 인접 정점 추가 메서드(연결 그래프)
    addAdjacentVertex(vertex) {
        this.adjacentVertices.push(vertex);
    }

    // 인접 정점 추가 메서드(무방향 그래프)
    addAdjacentVertexInUndirectedGraph(vertex) {
        if (this.adjacentVertices.includes(vertex)) {
            return;
        }

        this.adjacentVertices.push(vertex);
        vertex.addAdjacentVertexInUndirectedGraph(this);
    }
}

// 그래프 순회(해시 테이블을 사용하는 깊이 우선 탐색)
function dfsTraverse(vertex, visitedVertices = {}) {
    // 정점을 해시 테이블에 추가해 방문했다고 표시
    visitedVertices[vertex.value] = true;

    // 정점의 값을 출력해 제대로 순회하는지 확인
    console.log(vertex.value);

    // 현재 정점의 인접 정점을 순회
    vertex.adjacentVertices.forEach((adjacentVertex) => {
        // 이미 방문했던 인접 정점은 무시
        // 인접 정점에 대해 메서드를 재귀적으로 호출
        if (!visitedVertices[adjacentVertex.value]) {
            dfsTraverse(adjacentVertex, visitedVertices);
        }
    });
}

// 그래프에서 특정 값 탐색(해시 테이블을 사용하는 깊이 우선 탐색)
function dfs(vertex, searchValue, visitedVertices = {}) {
    // 찾고 있던 정점이라면 원래 vertex 리턴
    if (vertex.value === searchValue) {
        return vertex;
    }

    // 방문 표시
    visitedVertices[vertex.value] = true;

    // 현재 정점의 인접 정점 순회
    for (let i = 0; i < vertex.adjacentVertices.length; i++) {
        // 이미 방문한 인접 정점 무시
        if (visitedVertices[vertex.adjacentVertices[i].value]) {
            continue;
        }

        // 인접 정점이 찾고 있던 정점이면
        // 그 인접 정점 리턴
        if (vertex.adjacentVertices[i].value === searchValue) {
            return vertex.adjacentVertices[i];
        }

        // 인접 정점에 메서드를 재귀 호출해
        // 찾고 있던 정점을 계속 찾는다.
        const vertexWereSearchingFor = dfs(
            vertex.adjacentVertices[i],
            searchValue,
            visitedVertices
        );

        // 올바른 정점을 찾았다면 그 정점 리턴
        if (vertexWereSearchingFor) {
            return vertexWereSearchingFor;
        }
    }

    // 찾고 있던 정점을 찾지 못한 경우 null 리턴
    return null;
}

const alice = new Vertex("Alice");
const bob = new Vertex("Bob");
const cynthia = new Vertex("Cynthia");

// 앨리스가 밥과 신시아를 팔로우
alice.addAdjacentVertex(bob);
alice.addAdjacentVertex(cynthia);

// 밥이 신시아를 팔로우
bob.addAdjacentVertex(cynthia);

// 신시아가 밥을 팔로우
cynthia.addAdjacentVertex(bob);

// 앨리스가 밥을 친구 목록에 추가하면 밥의 친구 목록에도 앨리스가 추가됨(무방향 그래프)
// alice.addAdjacentVertexInUndirectedGraph(bob);

// console.log(alice);
// console.log(bob);
// console.log(cynthia);

console.log("dfsTravers alice");
dfsTraverse(alice); // 깊이 우선 탐색으로 앨리스의 인접 정점들 순회

console.log("dfsTravers bob");
dfsTraverse(bob); // 깊이 우선 탐색으로 앨리스의 인접 정점들 순회

console.log("dfsTravers cynthia");
dfsTraverse(cynthia); // 깊이 우선 탐색으로 앨리스의 인접 정점들 순회

console.log("dfs searchValue: Bob");
console.log(dfs(alice, "Bob")); // 깊이 우선 탐색으로 정점의 값이 'Bob'인 정점 탐색, 시작 정점은 앨리스.
