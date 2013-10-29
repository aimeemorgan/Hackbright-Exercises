import arithmetic

while True:
	data = raw_input("> ")
	tokens = data.split(" ")

	if tokens[0] == "q":
		break
	elif tokens[0] == "+":
		print arithmetic.add(int (tokens[1]), int (tokens[2]))
	elif tokens[0] == "-":
		print arithmetic.subtract(int (tokens[1]), int (tokens[2]))
	elif tokens[0] == "*":
		print arithmetic.multiply(int (tokens[1]), int (tokens[2]))
	elif tokens[0] == "/":
		print arithmetic.divide(int (tokens[1]), int (tokens[2]))
	elif tokens[0] == "square":
		print arithmetic.square(int (tokens[1]))
	elif tokens[0] == "cube":
		print arithmetic.cube(int (tokens[1]))
	elif tokens[0] == "pow":
		print arithmetic.power(int (tokens[1]), int (tokens[2]))
	elif tokens[0] == "mod":
		print arithmetic.mod(int (tokens[1]), int (tokens[2]))
