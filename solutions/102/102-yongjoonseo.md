# 102. Binary Tree Level Order Traversal

## solution 1

시간복잡도 : O(N)

알고리즘 : BFS

풀이 설명 : 큐의 길이 만큼 순회하여 BFS사이클을 구분하고, 큐에서 뽑은 노드의 값을 임시 리스트에 더합니다. BFS사이클 마다 만든 임시 리스트를 결과값에 더해주어 탐색이 끝나면 결과 리스트를 반환합니다.

소스코드 : [link](./102-yongjoonseo.py)

