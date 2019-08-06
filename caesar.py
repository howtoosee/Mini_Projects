def menu():
	print("-"*20)
	print("Menu: ")
	print("1. Encode")
	print("2. Decode")
	print("-"*20)

	choice = int(input("Enter your choice: "))

	while choice not in (1, 2):
		choice = int(input("Invalid, pls re-enter your choice: "))

	return choice



def cipher(char, n):
	new_ascii = ord(char) + n

	if (new_ascii not in range(97, 122+1)) and (new_ascii not in range(65, 90+1)):

		if n > 0:
			new_ascii = new_ascii - 26
			
		else:
			new_ascii = new_ascii + 26

	return chr(new_ascii)



def encode():
	string = input("Msg to be encoded: ")
	n = int(input("Caesar value: "))

	encoded_str = ""

	for char in string:
		if char.isalpha():
			encoded_str += cipher(char, n)

		else:
			encoded_str += char
		
	print(encoded_str)



def decode():
	string = input("Msg to be decoded: ")
	n = int(input("Caesar value: "))*(-1)

	decoded = ""

	for char in string:
		if char.isalpha():
			decoded += cipher(char, n)

		else:
			decoded += char
		
	print(decoded)



if __name__ == "__main__":
	choice = menu()

	if choice == 1:
		encode()
	else:
		decode()

