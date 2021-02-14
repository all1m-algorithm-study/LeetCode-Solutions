# 111. Minimum Depth of Binary Tree

## solution 1

시간복잡도 : O(N)

알고리즘 : 트리, BFS

풀이 설명 : 트리를 너비 우선 탐색하면서 자식 노드가 모두 없는 경우에 BFS 사이클을 돌았던 횟수를 반환합니다. 큐의 길이 만큼 반복문을 사용하여 BFS 사이클을 세어줍니다.

소스코드 : [link](./111-yongjoonseo.py)

