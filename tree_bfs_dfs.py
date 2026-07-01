from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def runBFS(root: Optional[Node]) -> None:
    if root is None:
        return

    q = deque([root])
    while q:
        print([node.val for node in q])

        newq = deque()
        while q:
            node = q.popleft()
            if node.left is not None:
                newq.append(node.left)
            if node.right is not None:
                newq.append(node.right)
        q = newq


def runDFS(root: Optional[Node]) -> None:
    levels = []
    preorder = []

    def dfs(node, depth):
        if not node:
            return None
        
        preorder.append(node.val)
        if len(levels) == depth:
            levels.append([])

        levels[depth].append(node.val)
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 0)
    print(preorder)
    print(levels)


def _createTree(nodes: List[Optional[int]]) -> Optional[Node]:
    # 1  2 3  4 5 6 7 ...
    # root i, left i * 2, right: i * 2 + 1
    # find parent: i // 2

    # 0  1 2  3 4 5 6 ...
    # root i, left i * 2 + 1, right: i * 2 + 2
    # find parent: (i - 1) // 2
    if len(nodes) == 0:
        return None

    res = [None] * len(nodes)
    for i, val in enumerate(nodes):
        node = Node(val=val) if val else None
        res[i] = node
        if i != 0: 
            p = res[(i - 1) // 2]
            if i % 2 != 0:
                p.left = node
            else:
                p.right = node
    
    return res[0]


if __name__ == "__main__":
    tree = [3, 9, 20, None, None, 15, 7]

    print("Iteratively run bfs:")
    runBFS(_createTree(tree))

    print("Recursively run dfs:")
    runDFS(_createTree(tree))