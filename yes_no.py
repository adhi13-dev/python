import random
answer = random.choice(range(0,10))
print(answer)
user = int(input("give a number between 0-10:-"))
while user != answer:
	if (user > answer):
		user = int(input("give a number below:-" +str(user)+":"))
	if (user < answer):
		user = int(input("give a number above:-" +str(user)+":"))
else:
	print("you won , the answer is : " + user)