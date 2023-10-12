#LINK
https://replit.com/join/txcvuwespk-maria-fernan901

current_age= int(input( "What is your current age? "))
retire_age= int(input("In which age fo you want to retire?"))
retire_amount=int(input("What is the desired amount you want to achieve?"))#this is FV 
r = 0.25 #25% annual , divided by 12 to be monthly
n = (retire_age - current_age)*12
t = retire_age - current_age
upper = retire_amount*r
lower = (((1+r)**n)-1)*((1+r)**(-t))
PMT=upper/lower
print("The mothly payment required to reach the retirement goal is",PMT)
