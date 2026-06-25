class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self._heap = [0]
        self._k = k
        for num in nums:
            self._push(num)

    def add(self, val: int) -> int:
        self._push(val)
        return self.kth()

    def kth(self) -> int:
        max_idx = 2**self._k
        subarray = self._heap[1:max_idx]
        subarray.sort(reverse=True)
        return subarray[self._k - 1]

    def _push(self, value: int):
        self._heap.append(value)
        idx = len(self._heap) - 1

        while idx > 1 and self._heap[idx // 2] < self._heap[idx]:
            self._heap[idx], self._heap[idx // 2] = self._heap[idx // 2], self._heap[idx]
            idx = idx // 2
