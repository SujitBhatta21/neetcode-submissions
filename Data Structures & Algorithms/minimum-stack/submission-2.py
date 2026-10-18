class MinStack:

    def __init__(self):
        self.minStack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if len(self.minimum) == 0 or val < self.minimum[-1]:
            self.minimum.append(val)
        else:
            self.minimum.append(self.minimum[-1])


    def pop(self) -> None:
        if self.minStack:
            self.minStack.pop()
            self.minimum.pop()

    def top(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return -1

    def getMin(self) -> int:
        return self.minimum[-1]
        
