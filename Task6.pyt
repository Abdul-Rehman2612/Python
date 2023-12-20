def main():
    number=int(input("Enter a number:"))
    likeStatus=likeDislike(number)
    print("The user has pressed:",likeStatus)
def likeDislike(number):
    likeDislikeIn=[]
    likeStatusIn="Nothing"
    i=int(0)
    while(i<number):
        likeDislikeIn.append(input("Enter Like or Dislike:"))
        i=i+1
    for j in range(0,number,1):
        if(likeDislikeIn[j]=="Like" and likeDislikeIn[j]!=likeStatusIn):
            likeStatusIn=likeDislikeIn[j]
        elif(likeDislikeIn[j]=="Dislike" and likeDislikeIn[j]!=likeStatusIn):
            likeStatusIn=likeDislikeIn[j]
        elif(likeDislikeIn[j]==likeStatusIn):
            likeStatusIn="Nothing"
    return likeStatusIn
if __name__ == "__main__":
    main()