# 925. Long Pressed Name

## solution 1

시간복잡도 : O(N)

알고리즘 : 순차 탐색

풀이 설명 : `name`의 인덱스를 별도로 지칭하고 `typed`를 순차적으로 탐색하여 글자가 중복되는 경우 continue, 일치하는 경우 `name`의 인덱스를 늘려가는 식으로 글자를 비교합니다. `typed`를 모두 순회한 후 `name`의 인덱스가 `name`을 모두 순회한 경우에만 `True`를 반환합니다.

소스코드 : [link](./925-yongjoonseo.py)

