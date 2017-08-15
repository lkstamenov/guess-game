num=input('Enter the number')
attempt=1
print('Guess a value from 0 to 100:')
num=int(num)
while (attempt<4):
  print("Attempt is: {}".format(attempt))
  attempt += 1
  if num==6:
  	print('Your guess is correct')
  	break
  elif num!= 6 and attempt < 4:
  	print("Enter another number")
  	num=input()
  	num=int(num)
  elif (attempt==4):
  		print('You have run out of attempts')
  
print("Run guess.py again")
