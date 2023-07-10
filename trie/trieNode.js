class TrieNode {
    constructor() {
        this.children = {};
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    search(word) {
        let currentNode = this.root;

        for (const char of word) {
            // 현재 노드에 현재 문자를 키로 갖는 자식이 있으면
            if (currentNode.children[char]) {
                // 자식 노드를 따라간다
                currentNode = currentNode.children[char];
            } else {
                // 현재 노드의 자식 중에 현재 문자가 없으면
                // 검색하려는 단어가 트라이에 없는 것이다.
                return null;
            }
        }

        return currentNode;
    }
}
