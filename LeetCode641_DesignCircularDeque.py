class MyCircularDeque:

    def __init__(self, k: int):
        self.left = 0
        self.right = 0
        self.arr = [None] * (k + 1)  # Changed to k + 1
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.left = (self.left - 1) % len(self.arr)
        self.arr[self.left] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr[self.right] = value
        self.right = (self.right + 1) % len(self.arr)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.arr[self.left] = None
        self.left = (self.left + 1) % len(self.arr)  # Fixed this line
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.right = (self.right - 1) % len(self.arr)
        self.arr[self.right] = None
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.left]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.right - 1) % len(self.arr)]

    def isEmpty(self) -> bool:
        return self.left == self.right

    def isFull(self) -> bool:
        return (self.right + 1) % len(self.arr) == self.left
