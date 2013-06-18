import random

print "Hello!"

name = raw_input("What is your name? ")
number = random.randint(1, 100)

print "%s, I'm thinking of a number between 1 and 100. Try to guess it!" % name

counter = 1
while True:
	if counter <= 5:
		guess = int(raw_input("Your guess? "))
		if guess < number:
			print "Too low! Try again buddy!"
			counter += 1
			print "You have %d tries left" % (6-counter)
		elif guess > number:
			print "Too high! Try again buddy!"
			counter += 1
			print "You have %d tries left" % (6-counter)
		else:
			print "Congratulations! You guessed right! It took you %d guesses." % counter
			break
	else:
		print "Oops! You've run out of tries!"
		break

