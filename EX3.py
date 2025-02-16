from EX1 import MinHeap


class MaxHeap(MinHeap):
    def _heapify_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self._parent(i)]:
            self.heap[i], self.heap[self._parent(i)] = self.heap[self._parent(i)], self.heap[i]
            i = self._parent(i)

    def _heapify_down(self, i):
        largest = i
        left = self._left_child(i)
        right = self._right_child(i)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)

# Testando com o array fornecido
heap = MaxHeap()
for val in [50, 30, 40, 10, 20, 35]:
    heap.insert(val)

heap.insert(45)
print("Nova estrutura do MaxHeap após inserção:", heap.heap)