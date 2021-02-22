# 1162. As Far from Land as Possible

## solution 1

시간복잡도 : O(N^2)

알고리즘 : BFS

풀이 설명 : 우선 `grid` 를 모두 순회하여 땅만 (`grid`가 1인 위치) 모두 큐에 넣어주고 방문처리합니다. 그 큐를 가지고 물이 있는 부분 (`grid`가 0인 지점)에 대한 너비 우선 탐색을 진행합니다. BFS가 완료될 때의 사이클의 횟수를 반환합니다.

소스코드 : [link](./1162-yongjoonseo.py)

