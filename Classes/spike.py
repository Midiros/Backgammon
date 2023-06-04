from stone import Stone

class Spike():
    def __init__(self, index, items = None):
        self.__data = items if items else []
        self.index = index

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        return self.__data.pop(-1)
        
    def my_index(self) -> int:
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


    #input hrac ktery chce krast
    def isStealable(self, player_number):
        if self.__data:
            if self.__data[0].owner() != player_number and len(self.__data) < 2:
                # print('STEALABLE')
                return True
            # print('NOT STEALABLE')
            return False
        # print('SPIKE IS EMPTY')    
        return True
