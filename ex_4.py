lst1 = ['a','c','e','g']
lst2 = ['b','d','f','h']

while(True):
    square = input("Enter the square: ")
    if square == 'q':
        break
    if len(square) != 2 or square[0] not in lst1+lst2 or (int(square[1]) < 1 or int(square[1]) > 8):
        print("Invalid square!")
    elif square[0] in lst1:
        if int(square[1]) % 2 == 0:
            print(f"{square} is white")
        else:
            print(f"{square} is black")

    elif square[0] in lst2:
        if int(square[1]) % 2 == 0:
            print(f"{square} is black")
        else:
            print(f"{square} is white")