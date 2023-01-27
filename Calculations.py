class Calculation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add(self):
        if self.x > 50:
            return self.x + self.y + 1000
        else:
            return self.y+self.x

    def public_add(self):
        return self.__add()

    def __subtract(self):
        return self.y-self.x  

    def public_subtract(self):
        return self.__subtract()


