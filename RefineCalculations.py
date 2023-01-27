from Calculations import Calculation as Calc

def calcAll(x,y):
    nX = int(x)
    nY = int(y)
    addResult = Calc(nX, nY).public_add()
    subResult = Calc(nX, nY).public_subtract()
    return addResult + subResult

