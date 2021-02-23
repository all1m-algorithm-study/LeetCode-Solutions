# 리스트 사용
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = []  # dictionary는 {}
        for i in s:
            if i.isalnum():             # 영문자, 숫자 여부 판별하는 함수
                str.append(i.lower())   # isalnum()은 대소문자 상관x, 소문자로 list 추가
                # print(str)
        # 펠린드롬 판단
        while len(str) > 1:
            if str.pop(0) != str.pop():
                return False
        return True
