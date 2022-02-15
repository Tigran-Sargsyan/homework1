while(True):
    faren = input("Enter the Farenhait temparature: ")
    if faren == 'q':
        break
    try:
        celsius = (float(faren)-32)/1.8
        print(f"{float(faren)}F = {celsius}C")
        print("press 'q' to quit")
    except:
        print("Invalid input")
