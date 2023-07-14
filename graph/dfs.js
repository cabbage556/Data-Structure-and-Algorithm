const Vertex = require("./graph");

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

console.log("dfsTravers alice");
dfsTraverse(alice); // 깊이 우선 탐색으로 앨리스의 인접 정점들 순회

console.log("dfsTravers bob");
dfsTraverse(bob); // 깊이 우선 탐색으로 앨리스의 인접 정점들 순회

console.log("dfsTravers cynthia");
dfsTraverse(cynthia); // 깊이 우선 탐색으로 앨리스의 인접 정점들 순회

console.log("dfs searchValue: Bob");
console.log(dfs(alice, "Bob")); // 깊이 우선 탐색으로 정점의 값이 'Bob'인 정점 탐색, 시작 정점은 앨리스.
