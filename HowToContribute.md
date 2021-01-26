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



## pull request 제목

pull request 제목은 `{문제 번호1}, {문제 번호2}, ...`와 같이 자신이 푼 문제의 번호가 보이도록 적습니다.

![image](https://user-images.githubusercontent.com/52124204/105846675-dba1d180-601f-11eb-9311-40c7ee86f7d4.png)



## commit 규칙

commit할 때, 다음 규칙을 지킵시다.

1. 커밋 메세지는 `add {파일1, 파일2, ..}`와 같이 **파일 명**이 나오도록 적습니다.

   ex1) `add 1234-iknoom.py, 1234-iknoom.md`

   ex2) `1234-iknoom.cpp 추가`

   ![image](https://user-images.githubusercontent.com/52124204/105846887-2c192f00-6020-11eb-9d38-f92b74178400.png)

   

2. 소스코드와 해설은 `solutions/{문제 번호}/{문제 번호}-{자신의 닉네임 또는 이름}.cpp`과 같이 저장합니다. `{문제 번호}` 디렉토리에 저장하고 파일명은 `{자신의 닉네임 또는 이름}`로 저장합니다.

   ex1) 1234번 문제의 python 풀이 : `solutions/1234/1234-iknoom.py`

   ex2) 1234번 문제의 해설 : `solutions/1234/1234-iknoom.md`

   ![image](https://user-images.githubusercontent.com/52124204/105847002-5f5bbe00-6020-11eb-8023-c5fe61d6c798.png)

   

3. 채점하여 **Accepted**를 받은 소스코드만 업로드합니다. 또한 **문제에서 제시하는 시간복잡도나 공간복잡도**를 만족하는 소스코드를 업로드합니다.

   ![image](https://user-images.githubusercontent.com/52124204/105847359-ddb86000-6020-11eb-91a1-cfbd771a66ce.png)

   

4. `README.md`는 수정하지 않습니다. 위 규칙대로 commit하시면 나중에 운영진이 종합해서 `README.md`를 수정할 예정입니다.



## 해설 적는 방법

어떤 문제를 풀 때 해설은 꼭 적지 않아도 괜찮습니다.

만약 적는다면 다음 4가지에 대해서 적습니다.

- 시간복잡도
- 알고리즘
- 풀이설명
- 소스코드

sally0226님의 풀이 예시입니다.

![image-20210126215104120](C:\Users\Moonki\AppData\Roaming\Typora\typora-user-images\image-20210126215104120.png)



## Issues

다음과 같은 경우 [issues](https://github.com/all1m-algorithm-study/LeetCode-Solutions/issues)를 이용하여 제보합니다.

- merge된 솔루션이 잘못된 경우
- merge된 솔루션이 문제에서 제시하는 시간복잡도나 공간복잡도를 만족하지 못하는 경우
- merge된 해설이 잘못된 경우


