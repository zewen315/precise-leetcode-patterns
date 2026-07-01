# Data Structure Time Complexity

| Data Structure | Operation | Time |
|----------------|-----------|------|
| **Array (List)** | Access | O(1) |
| | Search | O(n) |
| | Insert/Delete at Tail | O(1) amortized |
| | Insert/Delete at Head | O(n) |
| | Insert/Delete in Middle | O(n) |

| Data Structure | Operation | Time |
|----------------|-----------|------|
| **Linked List** | Access | O(n) |
| | Search | O(n) |
| | Insert/Delete at Head | O(1) |
| | Insert/Delete after Node | O(1) |
| | Insert/Delete at Tail | O(1)\* (with tail pointer) / O(n) |

| Data Structure | Operation | Time |
|----------------|-----------|------|
| **Hash Table** | Search | O(1) average |
| | Insert | O(1) average |
| | Delete | O(1) average |

Worst case: **O(n)**

| Data Structure | Operation | Time |
|----------------|-----------|------|
| **Binary Search Tree (Balanced)** | Search | O(log n) |
| | Insert | O(log n) |
| | Delete | O(log n) |

Unbalanced BST: **O(n)**

| Data Structure | Operation | Time |
|----------------|-----------|------|
| **Heap** | Peek | O(1) |
| | Insert | O(log n) |
| | Pop | O(log n) |
| | Heapify | O(n) |

| Data Structure | Operation | Time |
|----------------|-----------|------|
| **Stack** | Push | O(1) |
| | Pop | O(1) |
| | Peek | O(1) |

| Data Structure | Operation | Time |
|----------------|-----------|------|
| **Queue / Deque** | Enqueue | O(1) |
| | Dequeue | O(1) |
| | Front | O(1) |


| Data Structure | Operation | Time |
|----------------|-----------|------|
| **Trie** | Search | O(m) |
| | Insert | O(m) |
| | Delete | O(m) |
| | Prefix Search | O(m) |

*m = length of the string*
