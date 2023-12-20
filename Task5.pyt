def main():
    number=int(input("Enter a number:"))
    numStatus=evenishOrOddish(number)
    print("The number is:",numStatus)
def evenishOrOddish(number):
    i=0
    i=int(i)
    while(number>0):
        i=i+number
        number=number//10
    if(i%2==0):
        return "Evenish"
    else:
        return "Oddish"
if __name__ == "__main__":
    main()