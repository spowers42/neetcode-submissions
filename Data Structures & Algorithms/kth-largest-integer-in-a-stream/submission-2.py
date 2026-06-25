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
        return self._heap[1]

    def _push(self, value: int):
        # Keep a min heap of the k largest values
        if len(self._heap) == self._k + 1 and value < self._heap[1]:
            return

        if len(self._heap) < self._k + 1:
            # Do a normal heap insert
            self._heap.append(value)
            idx = len(self._heap) - 1

            while idx > 1 and self._heap[idx // 2] > self._heap[idx]:
                self._heap[idx], self._heap[idx // 2] = self._heap[idx // 2], self._heap[idx]
                idx = idx // 2

        else:
            # replace the smallest element with the new element
            self._heap[1] = value

            idx = 1
            while idx * 2 < len(self._heap):
                # if there are both left and right children
                if (
                    idx * 2 + 1 < len(self._heap)
                    and self._heap[idx * 2 + 1] < self._heap[idx * 2]
                    and self._heap[idx * 2 + 1] < self._heap[idx]
                ):
                    self._heap[idx * 2 + 1], self._heap[idx] = (
                        self._heap[idx],
                        self._heap[idx * 2 + 1],
                    )
                    idx = 2 * idx + 1
                elif self._heap[idx * 2] < self._heap[idx]:
                    self._heap[idx * 2], self._heap[idx] = self._heap[idx], self._heap[idx * 2]
                    idx = 2 * idx
                else:
                    break
