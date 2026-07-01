from collections import deque
from typing import List, Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def runBFS(node: Optional[Node]) -> None:
    if node is None:
        return

    visited = {node}
    q = deque([node])

    while q:
        level = [n.val for n in q]
        print(level)

        newq = deque()
        for n in q:
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    newq.append(neighbor)
        q = newq


def runDFS(node: Optional[Node]) -> None:
    visited = set()

    def helper(node: Node) -> None:
        if node in visited:
            return
        visited.add(node)
        print(node.val)
        for neighbor in node.neighbors:
            helper(neighbor)
    
    if node is None:
        return
    helper(node)


def _createGraph(edges: List[List[int]]) -> Optional[Node]:
    mapping = {}

    for edge in edges:
        a, b = (edge[0], edge[1])
        if a not in mapping:
            mapping[a] = Node(val=a)
        if b not in mapping:
            mapping[b] = Node(val=b)
        mapping[a].neighbors.append(mapping[b])
        mapping[b].neighbors.append(mapping[a])
    
    return mapping[1]

if __name__ == "__main__":
    # undirected graph example
    #
    # 1 - 2
    # | \ |
    # 3 - 4 - 5
    edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 1], [4, 5]]

    print("Iteratively run bfs:")
    runBFS(_createGraph(edges))

    print("Recursively run dfs:")
    runDFS(_createGraph(edges))