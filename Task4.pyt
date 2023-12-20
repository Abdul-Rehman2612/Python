def main():
    ballsBowled=int(input("Enter a number:"))
    overs=float(calculateOvers(ballsBowled))
    print("Number of overs bowled by the bowler:",overs)
def calculateOvers(ballsBowled):
    count = float(0)
    count = count + (ballsBowled%6)/10 + ballsBowled//6
    return count
if __name__ == "__main__":
    main()