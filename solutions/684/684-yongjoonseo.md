# 684. Redundant Connection

## solution 1

시간복잡도 : O(N)

알고리즘 : Union-Find

풀이 설명 : find 연산을 통해 두 정점이 이미 연결되어있는지 체크하며 `edges`배열을 순회합니다. 이미 두 정점이 연결되어 있다면 결과값을 갱신하고, 그렇지 않다면 union 연산을 수행합니다. 순회가 끝난 후 결과값을 반환합니다.

소스코드 : [link](./684-yongjoonseo.py)