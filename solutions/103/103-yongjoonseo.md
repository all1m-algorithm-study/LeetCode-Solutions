# 103. Binary Tree Zigzag Level Order Traversal

## solution 1

시간복잡도 : O(N)

알고리즘 : 트리, BFS

풀이 설명 : 큐를 사용하여 노드의 값을 임시 리스트에 append하고 자식 노드가 있는 경우 큐에 넣습니다. BFS 한 사이클 만큼의 임시 리스트를 결과로 반환할 리스트에 append 하는데, 이때 `xor` 연산을 통해 임시 리스트를 역순으로 넣을지 결정합니다. BFS를 모두 돌면 결과 리스트를 반환합니다.

소스코드 : [link](./103-yongjoonseo.py)

