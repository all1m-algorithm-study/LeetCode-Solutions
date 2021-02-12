class CustomStack:
    def __init__(self, maxSize):
        self.size = 0
        self.maxSize = maxSize
        self.data = []

    def push(self, x):
        if self.size == self.maxSize:
            return
        self.data.append(x)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return -1
        self.size -= 1
        return self.data.pop()

    def increment(self, k, val):
        if self.size <= k:
            for i in range(self.size):
                self.data[i] += val
        else:
            for i in range(k):
                self.data[i] += val