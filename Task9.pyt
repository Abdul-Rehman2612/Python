import os.path
def main():
    name=[]
    if(os.path.exists("data.txt")):
        f = open("data.txt", 'r')
        lines = f.read()
        name.append(lines)
        f.close()
        print(lines)
    else:
        print("File does not exist")
    print(name)
if __name__ == "__main__":
    main()