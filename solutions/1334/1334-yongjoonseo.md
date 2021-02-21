# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

## solution 1

시간복잡도 : O(N^3)

알고리즘 : 플로이드-와샬

풀이 설명 : 플로이드-와샬 알고리즘을 통해 모든 정점 사이의 최소 거리를 구해준 다음, 정점 사이의 거리가 `distanceThreshold`를 넘지 않는 도시의 개수가 가장 적은 도시를 반환합니다.

소스코드 : [link](./1334-yongjoonseo.py)

