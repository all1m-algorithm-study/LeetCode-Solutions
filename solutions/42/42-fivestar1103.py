class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        leftMaxArr, rightMaxArr, leftMaxIdx, rightMaxIdx = [height[0]], [height[-1]], 0, len(height) - 1
        for i in range(1, len(height)):
            if height[i] > leftMaxArr[-1]:
                leftMaxArr.append(height[i])
                leftMaxIdx = i
            else:
                leftMaxArr.append(leftMaxArr[-1])
        for i in range(len(height) - 2, -1, -1):
            if height[i] > rightMaxArr[-1]:
                rightMaxArr.append(height[i])
                rightMaxIdx = i
            else:
                rightMaxArr.append(rightMaxArr[-1])
        ret = 0
        for i in range(1, leftMaxIdx):
            ret += leftMaxArr[i] - height[i]
        rightMaxArr.reverse()
        for i in range(rightMaxIdx + 1, len(height) - 1):
            ret += rightMaxArr[i] - height[i]
        for i in range(leftMaxIdx + 1, rightMaxIdx):
            ret += leftMaxArr[-1] - height[i]
        return ret