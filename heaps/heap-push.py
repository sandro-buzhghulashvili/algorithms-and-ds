class Heap:
    def __init__(self):
        self.heap = [0]
    def push(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1
        
        while self.heap[index // 2] > self.heap[index]:
            tmp = self.heap[index]
            self.heap[index] = self.heap[index // 2]
            self.heap[index // 2] = tmp
            index = index // 2
    def __str__(self):
        return self.heap.__str__()

example_heap = Heap()

example_heap.push(15)
example_heap.push(12)
example_heap.push(16)

print(example_heap)