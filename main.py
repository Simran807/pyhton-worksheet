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




