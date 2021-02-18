# 945. Minimum Increment to Make Array Unique

## solution 1

시간복잡도 : O(NlogN)

알고리즘 : 정렬

풀이 설명 : 주어진 배열을 오름차순 정렬한 후 중복하여 나타나지 않는 숫자를 먼저 체크합니다. 중복하여 나왔던 숫자(a)와 나오지 않았던 숫자들 중 작은 것(b)의 차이(b-a)를 구해 결과값에 더합니다. 이때 b는 a보다 큰 숫자가 되도록 합니다.

소스코드 : [link](./945-yongjoonseo.py)

