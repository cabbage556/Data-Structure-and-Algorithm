class WeightedGraphVertex {
    constructor(value) {
        this.value = value;
        this.adjacentVertices = {};
    }

    addAdjacentVertex(vertex, weight) {
        this.adjacentVertices[vertex] = weight;
    }
}

const seoul = new WeightedGraphVertex("Seoul");
const busan = new WeightedGraphVertex("Busan");

// 인접 정점 추가 시 인접 정점과 가중치를 함께 전달
seoul.addAdjacentVertex(busan, 100);
busan.addAdjacentVertex(seoul, 200);
