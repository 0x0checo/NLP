### 二叉堆基础知识

二叉堆（Binary Heap）是一种特殊的二叉树数据结构，常用于实现优先队列（如堆排序算法中的关键部分）。它满足**堆序性**（Heap Property）：对于最大堆，父节点的值大于或等于其子节点的值；对于最小堆，反之。下面我从定义、结构、操作等方面逐步介绍基础知识。

#### 1. 基本定义与性质
- **二叉堆**：一个**完全二叉树**（Complete Binary Tree），即除了最后一层外，所有层都完全填充，最后一层从左到右填充。
- **堆序性**：
  - **最大堆（Max-Heap）**：每个节点的值 ≥ 其子节点的值。根节点是最大值。
  - **最小堆（Min-Heap）**：每个节点的值 ≤ 其子节点的值。根节点是最小值。
- **存储方式**：通常用数组实现（无需指针），因为完全二叉树便于数组映射：
  - 根节点索引：0（或1，根据实现）。
  - 对于节点i，其左子节点：2i+1，右子节点：2i+2。
  - 父节点：(i-1)/2（整数除法）。
- **时间复杂度**：
  - 构建堆：O(n)。
  - 插入/删除根节点：O(log n)。
  - 查找最大/最小：O(1)。

#### 2. 常见操作
二叉堆的核心操作包括插入（Heapify Up）、删除（Heapify Down）和构建。下面以Python伪代码说明（假设最大堆，数组从索引0开始）。

##### 2.1 插入元素
- 将新元素添加到数组末尾。
- 通过“上浮”（Heapify Up）调整位置，确保堆序性。
```python
def insert(heap, value):
    heap.append(value)  # 添加到末尾
    i = len(heap) - 1   # 新元素索引
    while i > 0 and heap[(i-1)//2] < heap[i]:  # 上浮
        heap[(i-1)//2], heap[i] = heap[i], heap[(i-1)//2]
        i = (i-1)//2
```

##### 2.2 删除根节点（提取最大/最小）
- 用数组最后一个元素替换根节点。
- 通过“下沉”（Heapify Down）调整根节点位置。
```python
def extract_max(heap):
    if not heap:
        return None
    max_val = heap[0]  # 根节点最大
    heap[0] = heap.pop()  # 末尾替换根
    if heap:  # 下沉调整
        heapify_down(heap, 0)
    return max_val

def heapify_down(heap, i):
    n = len(heap)
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and heap[left] > heap[largest]:
        largest = left
    if right < n and heap[right] > heap[largest]:
        largest = right
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        heapify_down(heap, largest)
```

##### 2.3 构建堆
- 从最后一个非叶子节点开始，逐个下沉调整。
```python
def build_heap(heap):
    n = len(heap)
    for i in range(n//2 - 1, -1, -1):  # 从最后一个非叶子节点倒序
        heapify_down(heap, i)
```

#### 3. 应用场景
- **堆排序（Heap Sort）**：先建最大堆，然后反复提取根节点，实现O(n log n)排序。
- **优先队列**：如Dijkstra算法中的最小堆距离优先。
- **Top-K问题**：用最小堆维护前K大元素。

#### 4. 示例
假设数组 [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]，构建最大堆后变为 [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]。

如果需要代码实现、具体算法推导或最小堆变体，请提供更多细节！
