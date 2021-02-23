# 슬라이싱 사용
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()  # 소문자 만들기
        # 문자열 필터링: re.sub('바꾸고 싶은 문자', '해당 문자로 바꾸기', 전체 문자열) 참고: https://dojang.io/mod/page/view.php?id=2438
        # 정규식 참고: https://cheatography.com/davechild/cheat-sheets/regular-expressions/
        s = re.sub('[^a-z0-9]', '', s)
        # print(s)
        # 문자열을 뒤집어서 같은 문자열인지 대조, 팰린드롬이면 true, 아니면 false return
        return s == s[::-1]
