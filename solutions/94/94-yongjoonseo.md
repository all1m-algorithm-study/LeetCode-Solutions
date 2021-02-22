# 94. Binary Tree Inorder Traversal

## solution 1

시간복잡도 : O(N)

알고리즘 : 스택

풀이 설명 : 각 노드의 왼쪽 자식 노드가 없을 때까지 반복적으로 갱신하며 스택에 넣어줍니다. 이후 스택에서 값을 하나 pop해서 결과 리스트에 더해주고, 꺼낸 것의 오른쪽 자식 노드로 노드를 갱신한 후 반복문을 계속 수행합니다. (오른쪽 자식 노드가 없는 경우 다음 반복문에서 pop연산만 이루어지기 때문에 괜찮습니다.) 반복문을 모두 수행하고 나면 결과 리스트를 반환합니다.

소스코드 : [link](./94-yongjoonseo.py)



## solution 2

시간복잡도 : O(N)

알고리즘 : 재귀

풀이 설명 : 각 노드의 왼쪽 자식 노드에 대한 재귀함수 호출, 결과 리스트에 노드의 값 더하기, 오른쪽 자식 노드에 대한 재귀함수 호출 순으로 작업을 수행한 후 결과 리스트를 반환합니다. 재귀함수 호출은 자식 노드가 있는 경우에만 실행됩니다.

소스코드 : 

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return
        result = []
        if root.left: result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        if root.right: result.extend(self.inorderTraversal(root.right))
        return result
```



