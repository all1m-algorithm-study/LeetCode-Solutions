# 547. Number of Provinces

## solution 1

시간복잡도 : O(N^2)

알고리즘 : Union-Find

풀이 설명 : `isConnected` 행렬을 순회하며 연결된 지점을 `union`합니다. 행렬을 모두 순회한 후 상호 배타 집합의 루트 노드 중 중복되지 않는 노드의 개수를 반환합니다.

소스코드 : [link](./547-yongjoonseo.py)

