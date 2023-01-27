
def perimeterCalc(w:int, h:int):
    if w < 0:
        raise ValueError("Error! The width %d is negative" %w)
    if h < 0:
        raise ValueError("Error! The height %d is negative" %h)
    return (w + h) * 2


try:
    print("Let's calculate the perimeter of a rectangle!")
    w = int(input("Enter the width:"))
    h = int(input("Enter the height:"))
    p = perimeterCalc(w, h)
    print("The perimeter is: %d" % p)
except ValueError as err:
    print('Invalid input: %s' % err)