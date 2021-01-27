class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        from collections import deque

        heights, myStack, left = [0] + heights, [[0, 0]], []
        for i in range(1, len(heights)):
            while True:
                if not myStack or myStack[-1][1] < heights[i]:
                    left.append(myStack[-1][0] if myStack else 0)
                    myStack.append([i, heights[i]])
                    break
                myStack.pop()
        myStack, area, ans = [[len(heights), 0]], deque(), -1
        for i in range(len(heights) - 1, 0, -1):
            while True:
                if not myStack or myStack[-1][1] < heights[i]:
                    tmp = ((myStack[-1][0] if myStack else len(heights)) - left[i - 1] - 1) * heights[i]
                    if ans < tmp:
                        ans = tmp
                    area.appendleft(tmp)
                    myStack.append([i, heights[i]])
                    break
                myStack.pop()
        return ans