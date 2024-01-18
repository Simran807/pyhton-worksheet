import random
l = ['A ','a','B' ,'b','C' ,'c','D' ,'d','E', 'e','F' ,'f','G' ,'g','H' ,'h','I' ,'i','J' ,'j','K' ,'k','L' ,'l','M' ,'m','N' ,'n','O' ,'o','P', 'p','Q' ,'q','R' ,'r','S' ,'s','T'  ,'t','U' ,'u','V', 'v','W' ,'w','X' ,'x','Y' ,'y','Z' ,'z']
n = ['0','1','2','3','4','5','6','7','8','9']
s = ['!','@','#','$','%','*','^','&','(',')','+']

print("Welcome to the pypassword generator")
nr_l= int (input("How many letters would you like in your password?\n"))
nr_s = int(input("How many symbol would you like?\n"))
nr_n = int(input("How many numbers would you like?\n"))
p=[]
for c in range(1,nr_l+1):
    p += random.choice(l)


for c in range(1,nr_s+1):
    p += random.choice(s)



for c in range(1,nr_n+1):
    p += random.choice(n)    

print(p)
random.shuffle(p)
print(p)
 
p=""
for c in p:
    p+=c
print(f"Your password is:{p}")    

