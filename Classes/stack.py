class Stack():
    def __init__(self, items = None):
        self.__data = items if items else []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
            return None
        else:
            return self.__data.pop()

    def peek(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            return self.__data[-1]

    def is_empty(self):
        return len(self.__data) == 0
    
    def getHistoryAverage(self):
        movementCount = 0
        for kamen in self.__data:
            movementCount += len(kamen.history)
            
        return movementCount / len(self.__data)

    def myLen(self):
        return len(self.__data)

    def __len__(self):
        return len(self.__data)

    def __str__(self):
        return str(self.__data)
