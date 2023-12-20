def main():
    number=int(input("Enter a number:"))
    length=calculateLength(number)
    print("Length of number is",length)
def calculateLength(number):
    i=0
    i=int(i)
    while(number>0):
        i=i+1
        number=number//10
    return i
if __name__ == "__main__":
    main()