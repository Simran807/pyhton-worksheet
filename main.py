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




