count,arithm_mean,sum = 0,0,0
while (True):
    current = input("Enter a number: ")
    try:
        sum+=float(current)
        count+=1
    except:
        print("Invalid data")
    if current == "done":
        break

if count != 0:
    arithm_mean = sum / count

print(f"The sum is: {sum}")
print(f"You entered {count} numbers")
print(f"The arithmetic mean is: {arithm_mean}")

