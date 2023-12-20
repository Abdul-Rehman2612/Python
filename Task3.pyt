def main():
    number=int(input("Enter a number:"))
    length=calculateLength(number)
    print("Length of number is",length)
def calculateLength(number):
    count = 0
    count = int (count)
    for i in range(int(number),0,number//10):
        count+=1
    return count
if __name__ == "__main__":
    main()