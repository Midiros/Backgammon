from stone import Stone

class Spike():
    def __init__(self, items = None, index = None):
        self.__data = items if items else []
        self.index = index

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        return self.__data.pop(-1)
        
    def my_index(self):
        return self.index

    def peek(self):
        if self.__data:
            # print(self.__data[-1])
            return self.__data[-1]
        else:
            return None
    
    
    def is_empty(self):
        return not self.__data

    def __len__(self):
        return len(self.__data)

    def __str__(self):
        return str(self.__data)
    
    def list_of_stones(self):
        for kamen in self.__data:
            print(kamen)
