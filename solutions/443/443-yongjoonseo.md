# 443. String Compression

## solution 1

시간복잡도 : O(N)

알고리즘 : 완전 탐색

풀이 설명 : chars에 있는 값을 순차적으로 방문하며 글자가 바뀔 때마다 해당 글자를 추가하고 똑같은 글자가 나올 때마다 숫자를 늘리는 방식을 사용합니다.

소스코드 : [link](./443-yongjoonseo.py)