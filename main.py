'''import random

test_seed = int(input("Create a seed number :"))
random.seed(test_seed)
random_side= random.randint(0,1)
if(random_side==0):
    print("Head")
else:
    print("Tails")    
import random
nameAsCSV = input("Give me everybody's name ,seperated by commas")
name = nameAsCSV.split(",")
print(name)
l =  len(name)
random_choice=random.randint(0,l-1)
pay= name[random_choice]

print(pay)

row1 = ["🖽","🖽","🖽"]
row2 = ["🖽","🖽","🖽"]
row3 = ["🖽","🖽","🖽"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?")
h = int(position[0])
v = int(position[1])
map[v -1][h-1]="X"

print(f"{row1}\n{row2}\n{row3}")'''

import random
rock= "✊"
paper = "✋"
scissor="✌🏼"
game_image=[rock,paper,scissor]
c = int(input("What do you choose?Type 0 for rock,1 for paper or 2 for Scissors"))
print(game_image [c])
   
c_c = random.randint(0,2)
print(f"computer choice{c_c}")
print(game_image[c_c])
if c == 0 and c_c ==2 :
    print("you win")
elif( c>=3 or c<0):
    print("You typed invalid number you lose!")
elif(c_c ==0 and c ==2):
    print("You lose")        
elif c_c > c:
    print("you lose")
elif c_c == c:
    print ("it's a draw")    


