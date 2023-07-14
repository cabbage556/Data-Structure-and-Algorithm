const Queue = require("../stack_queue/queue");

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

module.exports = Vertex;
