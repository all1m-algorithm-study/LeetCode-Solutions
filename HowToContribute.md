# LeetCode Solution에 기여하는 방법

간단하게 Pull Request로 기여하면 됩니다.



1. 일단 github 계정이 없다면 계정을 생성합시다.

2. [LeetCode-Solutions](https://github.com/all1m-algorithm-study/LeetCode-Solutions) 저장소를 fork합니다.
3. 그 후 fork한 저장소를 clone합니다.
4. 소스코드(cpp, python, java) 또는 해설을 작성하고 clone한 저장소에 저장합니다.
5. commit합니다.
6. 원본 저장소에 Pull Request를 보냅니다.
7. 그럼 운영진이 확인한 후 merge합니다.



git에 익숙하지 않으신 분들을 위해서 더 자세한 내용을 추가할 예정이며

그래도 모르겠다면 AL林 slack에 많이 물어보세요.



#### PR(Pull Requeset) 관련 참고 자료

- https://www.secmem.org/blog/2019/04/10/git_pr/
- https://wayhome25.github.io/git/2017/07/08/git-first-pull-request-story/
- https://www.slideshare.net/jungseobshin/github-pull-request
- 그 외에도 검색하면 많이 나옵니다.



## commit 규칙

commit할 때, 다음 규칙을 지킵시다.

1. 커밋 메세지는 `add {파일1, 파일2, ..}`와 같이 **파일 명**이 나오도록 적습니다.

   ex1) `add 1234.py, 1234.md`

   ex2) `1234.cpp 추가`

2. 소스코드와 해설은 `solutions/{문제 번호}/{문제 번호}.cpp`과 같이 저장합니다. `{문제 번호}` 디렉토리에 저장하고 파일명은 `{문제 번호}`로 저장합니다.

   ex1) 1234번 문제의 python 풀이 : `solutions/1234/1234.py`

   ex2) 1234번 문제의 해설 : `solutions/1234/1234.md`

3. **Accepted**를 받은 소스코드만 업로드합니다.

4. 이미 업로드된 Accepted를 받은 소스코드보다 더 효율적인 소스코드가 있을 경우에는 해설에 소스코드를 추가합니다.

   ex) A가 올린 `1234.py`가 O(N^2)인데 B가 더 빠른 O(N) 풀이를 찾음 => 새로운 `1234.py`를 업로드하거나 `1234.py`를 수정하는게 아니라 해설(`1234.md`)의 내용에 추가합니다. 

5. `README.md`는 수정하지 않습니다. 위 규칙대로 commit하시면 나중에 운영진이 종합해서 `README.md`를 수정할 예정입니다.



## 해설 적는 방법

어떤 문제를 풀 때 해설은 꼭 적지 않아도 괜찮습니다.

만약 적는다면 다음 4가지에 대해서 적습니다.

- 시간복잡도
- 알고리즘
- 풀이설명
- 소스코드







