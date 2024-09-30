class CustomStack:

    def __init__(self, maxSize: int):
        self.stackPosition = 0
        self.maxSize = maxSize
        self.stackArray = [0] * maxSize

    def push(self, x: int) -> None:
        if self.stackPosition < self.maxSize:
            self.stackArray[self.stackPosition] = x
            self.stackPosition += 1

    def pop(self) -> int:
        if self.stackPosition > 0:
            self.stackPosition -= 1
            return self.stackArray[self.stackPosition]
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        limit = min(k, self.stackPosition)
        for i in range(limit):
            self.stackArray[i] += val
