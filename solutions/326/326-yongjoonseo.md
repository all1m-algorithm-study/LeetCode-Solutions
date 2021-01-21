# 326. Power of Three

## solution 1

시간복잡도 : O(log<sub>3</sub>n)

알고리즘 : 재귀

풀이 설명 : 3으로 나누었을 때 나머지가 없다면 3으로 나눈 몫을 다시 입력으로 하여 함수를 재귀 호출합니다. 더이상 3으로 나눌 수 없을 때 몫이 0이고 나머지가 1인 경우만 3의 배수이므로 `True`를 반환, 나머지 경우엔 `False`를 반환합니다.

소스코드 : [link](./326-yongjoonseo.py)
