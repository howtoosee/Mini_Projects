from random import randint as rand


def genChar():
	if rand(0,1):
		return chr(rand(65,90))

	else:
		return str(rand(0,9))


def genCode():
	s = ""

	for i in range(6):
		s += genChar()

	return s


if __name__ == "__main__":

	with open("codes.csv", 'w') as myfile:
		codes = []

		for i in range(30000):
			c = genCode()
			while c in codes:
				c = genCode()
				print("collided")

			myfile.write(c + "\n")
			codes.append(c)

	myfile.close()


