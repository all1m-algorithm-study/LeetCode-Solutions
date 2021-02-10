# 515. Find Largest Value in Each Tree Row

## solution 1

시간복잡도 : O(N)

알고리즘 : 트리, BFS

풀이 설명 : 트리를 너비 우선 탐색하여 각 BFS 사이클 마다의 최댓값을 리스트에 더하고, 트리 순회를 모두 마친 후 결과 리스트를 반환합니다. 큐의 길이 만큼 반복문을 사용하여 BFS 사이클을 구분합니다.

소스코드 : [link](./515-yongjoonseo.py)

