# 990. Satisfiability of Equality Equations

## solution 1

시간복잡도 : O(N)

알고리즘 : Union-Find

풀이 설명 : 우선 등호가 성립하는 방정식에 대해 모두 `union`연산을 하고 등호가 성립하지 않는 방정식은 별도로 저장합니다. 이후 등호가 성립하지 않는 방정식들을 순회하며 하나라도 이미 등호가 성립한 관계에 있었다면 `False`를 반환하고, 모두 순회한 후에도 등식의 모순이 생기지 않는 경우엔 `True`를 반환합니다.

소스코드 : [link](./990-yongjoonseo.py)

