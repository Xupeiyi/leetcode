from math import inf
from TreeBuilder import TreeNode


class Codec:
    def serialize(self, root: TreeNode) -> str:
        arr = []
        def postOrder(root: TreeNode) -> None:
            if root is None:
                return
            postOrder(root.left)
            postOrder(root.right)
            arr.append(root.val)
        postOrder(root)
        return ' '.join(map(str, arr))

    def deserialize(self, data: str) -> TreeNode:
        arr = list(map(int, data.split()))
        def construct(lower: int, upper: int) -> TreeNode:
            if arr == [] or arr[0] < lower or arr[0] > upper:
                return None
            val = arr.pop()
            root = TreeNode(val)
            root.left = construct(lower, val)
            root.right = construct(val, upper)
            return root
        return construct(-inf, inf)
