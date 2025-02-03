class Heap:
    def __init__(self):
        self.heap = [0]
    
    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        peak = self.heap[1]
        self.heap[1] = self.heap.pop()
        index = 1

        while index * 2 < len(self.heap):
            if index * 2 + 1 < len(self.heap) and self.heap[index * 2 + 1] < self.heap[index * 2] and self.heap[index] > self.heap[index * 2 + 1]:
                tmp = self.heap[index]
                self.heap[index] = self.heap[index * 2 + 1]
                self.heap[index * 2 + 1] = tmp
                index = index * 2 + 1
            elif self.heap[index] > self.heap[index * 2]:
                tmp = self.heap[index]
                self.heap[index] = self.heap[index * 2]
                self.heap[index * 2] = tmp
                index = index * 2
            else:
                break
        
        return peak
    
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
example_heap.push(2)
example_heap.push(7)
example_heap.push(9)
example_heap.push(12)
example_heap.push(13)
example_heap.push(11)

example_heap.pop()
example_heap.pop()
example_heap.pop()


print(example_heap)