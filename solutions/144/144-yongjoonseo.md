# 144. Binary Tree Preorder Traversal

## solution 1

시간복잡도 : O(N)

알고리즘 : 스택

풀이 설명 : 스택에서 노드를 하나 뽑아 그 값을 결과 리스트에 더합니다. 그 후 오른쪽부터 자식 노드가 있는지 검사하여 자식 노드가 있다면 스택에 더해주고 같은 작업을 스택이 없어질 때까지 반복합니다. 작업이 모두 끝나면 결과 리스트를 반환합니다.

소스코드 : [link](./144-yongjoonseo.py)



## solution 2

시간복잡도 : O(N)

알고리즘 : 재귀

풀이 설명 : 각 노드의 값을 먼저 결과 리스트에 더한 후에 왼쪽부터 자식 노드가 있는지 검사합니다. 자식 노드가 있다면 재귀함수를 호출하여 결과 리스트에 다시 더해주어 반환합니다.

소스코드 : 

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return
        result = []
        result.append(root.val)
        if root.left: result.extend(self.preorderTraversal(root.left))
        if root.right: result.extend(self.preorderTraversal(root.right))
        return result
```



