# 107. Binary Tree Level Order Traversal II

## solution 1

시간복잡도 : O(N)

알고리즘 : 트리, BFS

풀이 설명 : 주어진 트리를 너비 우선 탐색하여 각 노드의 값을 결과 리스트에 추가합니다. 큐의 길이 만큼 반복문을 사용하여 BFS 사이클을 구분합니다. 트리의 바닥부터 출력하기 위해 결과 리스트를 다시 역순으로 재배치합니다.

소스코드 : [link](./107-yongjoonseo.py)

