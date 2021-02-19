# 145. Binary Tree Postorder Traversal

## solution 1

시간복잡도 : O(N)

알고리즘 : 스택

풀이 설명 : 스택에서 노드를 하나 pop하고 결과 리스트에 넣어줍니다. 이후 각 노드의 왼쪽부터 자식 노드가 있는지 검사하여 자식 노드들을 스택에 저장합니다. 반복문이 모두 수행되면 결과 리스트를 뒤집어서 반환합니다.

소스코드 : [link](./145-yongjoonseo.py)





## solution 2

시간복잡도 : O(N)

알고리즘 : 재귀

풀이 설명 : 각 노드의 왼쪽부터 자식 노드가 있는지 검사합니다. 왼쪽 오른쪽 자식 노드부터 재귀함수를 호출한 후에 값을 결과 리스트에 더하여 반환합니다.

소스코드 : 

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return
        result = []
        if root.left: result.extend(self.postorderTraversal(root.left))
        if root.right: result.extend(self.postorderTraversal(root.right))
        result.append(root.val)
        return result
```



