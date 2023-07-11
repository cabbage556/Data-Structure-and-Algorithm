class TrieNode {
    constructor() {
        this.children = {};
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    // 트라이 검색
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

    // 트라이 삽입
    insert(word) {
        let currentNode = this.root;

        for (const char of word) {
            // 현재 노드에 현재 문자를 키로 하는 자식이 있는 경우
            if (currentNode.children[char]) {
                // 자식 노드를 따라간다.
                currentNode = currentNode.children[char];
            }
            // 현재 노드의 자식 중에 현재 문자가 없는 경우
            else {
                // 그 문자를 새 자식 노드를 추가한다.
                const newNode = new TrieNode();
                currentNode.children[char] = newNode;

                // 새 자식 노드를 따라간다.
                currentNode = newNode;
            }
        }

        // 단어 전체를 트라이에 삽입했으면 마지막으로 *를 추가한다.
        currentNode.children["*"] = null;
    }

    // 트라이 내 모든 단어를 배열로 반환하는 메서드
    // 아규먼트로 받은 노드부터 시작되는 모든 단어 나열 가능
    collectAllWords(node = null, word = "", words = []) {
        // node: 자손들에게서 단어를 수집할 노드
        // word: 빈 문자열로 시작해 트라이를 이동하면서 문자 추가
        // words: 빈 배열로 시작해 트라이 내 모든 단어 포함

        // 현재 노드를 첫 번째 아규먼트로 설정한다. 없으면 루트 노드로 설정한다.
        let currentNode = node ?? this.root;

        // 현재 노드의 모든 자식들을 순회한다.
        for (const key in currentNode.children) {
            // 현재 키가 '*'이면 단어 끝에 도달했다는 의미이므로
            // 이 단어를 words 배열에 추가
            if (key === "*") {
                words.push(word);
            }
            // 단어 중간인 경우
            else {
                // 자식 노드에 대해 이 함수를 재귀적으로 호출한다.
                this.collectAllWords(
                    currentNode.children[key],
                    word + key,
                    words
                );
            }
        }

        return words;
    }

    // 자동 완성 메서드
    autocomplete(prefix) {
        let currentNode = this.search(prefix);

        if (!currentNode) {
            return null;
        }

        return this.collectAllWords(currentNode, prefix);
    }
}

const trie = new Trie();
trie.insert("can");
trie.insert("cat");
trie.insert("cap");
trie.insert("captain");
console.log(trie.root.children["c"].children["a"].children["p"]);
console.log(trie.collectAllWords());
