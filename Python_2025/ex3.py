
import random
number = random.randint(1, 10)
print(number)

found = 0

x= input("Guess a Number:")
while found == 0:
	if int(x) == number:
		found=1
	else:
  		x = input ("Sorry ,guess again:")

print("Congratulations!")
