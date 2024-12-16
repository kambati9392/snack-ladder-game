import random
pos=0
def die():
    # global die_roll
      die_roll=random.randrange(1,6) # die rolls it gives random number
      return die_roll
ladder=[]
while len(ladder)<10:
    n=random.randrange(1,91)
    if n not in ladder:
     ladder.append(n)
    print(ladder)

snake=[]
while len(snake)<10:
    m=random.randrange(1,100)
    if m not in ladder and m not in snake:
     snake.append(m)
    print(snake)
count =0
while pos<100:
    count+=1
    print("current position = ",pos )
    check=die()
    if pos+check<=100:
      pos=pos+check
    if pos <100:
        while pos in ladder:
            pos=pos+die()
        while pos in snake:
            pos=pos-die()

        print("current position =",pos)
    if pos<0:
     pos=0
    if pos ==100:
       print("win!!!!!")
       print("number of dies rolled to win!!---->",count)
       



