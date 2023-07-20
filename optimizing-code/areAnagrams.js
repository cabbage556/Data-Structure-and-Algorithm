// O(N * M)
function areAnagrams(firstString, secondString) {
    const secondStringArray = secondString.split("");

    for (let i = 0; i < firstString.length; i++) {
        // firstString 순회 중에 secondStringArray가 빈 경우
        // 두 문자열이 애너그램이 아니다.
        if (!secondStringArray.length) {
            return false;
        }

        for (let j = 0; j < secondStringArray.length; j++) {
            // firstString과 secondStringArray에 같은 문자가 있으면
            if (firstString[i] === secondStringArray[j]) {
                // 두 번째 배열에서 그 문자를 삭제하고 바깥 루프로 돌아가기
                secondStringArray.splice(j, 1);
                break;
            }
        }
    }

    // firstString을 모두 순회했을 때
    // secondStringArray에 남은 문자가 없어야 두 문자열이 애너그램이다.
    return secondStringArray.length === 0;
}

function areAnagrams2(firstString, secondString) {
    const firstWordHashTable = {};
    const secondWordHashTable = {};

    // 첫 번째 문자열의 해시 테이블 생성
    for (const char of firstString) {
        if (firstWordHashTable[char]) {
            firstWordHashTable[char] += 1;
        } else {
            firstWordHashTable[char] = 1;
        }
    }

    // 두 번째 문자열의 해시 테이블 생성
    for (const char of secondString) {
        if (secondWordHashTable[char]) {
            secondWordHashTable[char] += 1;
        } else {
            secondWordHashTable[char] = 1;
        }
    }

    for (const char in firstWordHashTable) {
        if (firstWordHashTable[char] !== secondWordHashTable[char]) {
            return false;
        }
    }

    return true;
}

console.log(areAnagrams("IM FEARLESS", "LE SSERAFIM"));
console.log(areAnagrams2("IM FEARLESS", "LE SSERAFIM"));
