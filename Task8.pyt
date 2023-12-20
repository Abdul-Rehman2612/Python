import os.path
def main():
    number=int(input("Enter a number:"))
    takeInput(number)
def takeInput(number):
    Name=[]
    i=int(0)
    while(i<number):
        Name.append(input("Enter Name:"))
        i=i+1
    fileHandeling(Name,number)
def fileHandeling(Name,number):
    f = open("data.txt", 'w')
    for i in range (0,number,1):
        f.write(Name[i]+";\n")
    f.close()
if __name__ == "__main__":
    main()