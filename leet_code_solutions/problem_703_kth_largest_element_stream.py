from typing import List
import heapq

# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.key = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > self.key:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.key:
            heapq.heappop(self.heap)
        return self.heap[0]


kth = KthLargest(3, [4, 5, 8, 2])
print(kth.add(3))
print(kth.add(5))
print(kth.add(10))
print(kth.add(9))
print(kth.add(4))

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
