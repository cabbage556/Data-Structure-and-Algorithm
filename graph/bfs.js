const Queue = require("../stack_queue/queue");

// 그래프 순회(해시 테이블을 사용하는 너비 우선 탐색)
function bfsTraverse(startingVertex) {
    const queue = new Queue();
    const visitedVertices = {};
    visitedVertices[startingVertex.value] = true;
    queue.enqueue(startingVertex);

    // 큐가 빌 때까지 실행
    while (queue.read()) {
        // 큐에서 첫 번째 정점을 삭제해 현재 정점으로 만든다.
        const currentVertex = queue.dequeue();

        // 현재 정점의 값 출력
        console.log(currentVertex.value);

        // 현재 정점의 인접 정점 순회
        currentVertex.adjacentVertices.forEach((adjacentVertex) => {
            // 아직 방문하지 않은 인접 정점이면
            if (!visitedVertices[adjacentVertex.value]) {
                // 방문했다고 표시
                visitedVertices[adjacentVertex.value] = true;

                // 큐에 추가
                queue.enqueue(adjacentVertex);
            }
        });
    }
}
