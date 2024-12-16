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
print("current position = ",pos )
check=die()
pos=pos+check
while pos in ladder:
    pos=pos+die()
while pos in snake:
    pos=pos-die()

print("current position =",pos)

       



