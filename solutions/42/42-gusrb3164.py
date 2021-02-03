class Solution:
    def trap(self, height: List[int]) -> int:
        stack=[] #스택을 이용한 풀이
        volume=0
        
        for i in range(len(height)):
            while stack and height[stack[-1]]<height[i]:
                topIdx=stack.pop()
                
                if not len(stack):
                    break
                
                distance = i- stack[-1]-1
                depth=min(height[stack[-1]],height[i])-height[topIdx]
                
                volume += distance*depth
                
            stack.append(i)
        
        return volume