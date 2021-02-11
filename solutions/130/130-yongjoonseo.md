# 130. Surrounded Regions

## solution 1

시간복잡도 : O(NM)

알고리즘 : BFS

풀이 설명 : `board`의 요소가 `'O'`인 지점에서만 너비 우선 탐색을 실행하여 연결된 모든 `'O'`를 `'X'`로 바꿔줍니다. BFS 중에 `board` 밖으로 탐색하지 않는 경우에만 글자를 변환합니다.

소스코드 : [link](./130-yongjoonseo.py)

