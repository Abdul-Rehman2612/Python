def main():
    height=int(input("Enter height:"))
    width=int(input("Enter width:"))
    character=input("Enter a character:")
    printShap(height,width,character)
def printShap(height,width,character):
    for i in range (0,height,1):
        shape=""
        for j in range (0,width,1):
            shape=shape+character
        print(shape)
if __name__ == "__main__":
    main()