### DFS vs. BFS: Why is DFS usually recursive while BFS is iterative?

The key difference lies in the underlying data structure.

* **DFS naturally uses a stack.** Recursive calls are simply an implicit stack managed by the language runtime, which makes recursion the most natural way to implement DFS. An iterative DFS is equivalent—it just manages the stack explicitly.

* **BFS naturally uses a queue.** Since BFS must process nodes level by level in **first-in, first-out (FIFO)** order, it is almost always implemented iteratively using a queue. While recursive BFS is theoretically possible, it is much more complicated and rarely used in practice.

> **DFS = Stack (recursion is just an implicit stack)**
> **BFS = Queue (FIFO is required for level-order traversal)**
