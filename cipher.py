# Cipher coding

"""
  This is a python code for caesar cipher for my own liking
  This messages only includes alphabetical order and does not include any other characters. 
  Made by: Jiwon Sin
"""

def encryption(message, shift_number):
	encrypt_message = ""
	for i in range(len(message)):
		original = ord(message[i])
		ascii_element = original + shift_number
		if original >= 65 and original <= 90:
			if ascii_element > 90:
				ascii_element -= 26
		elif original >=97 and original <= 122:
			if ascii_element > 122:
				ascii_element -= 26
		encrypt_message += chr(ascii_element)
	return encrypt_message

def decryption(message, shift_number):
	decrypt_message=""
	for i in range(len(message)):
		original = ord(message[i])
		ascii_element = original - shift_number
		if original >= 65 and original <= 90:
			if ascii_element < 65:
				ascii_element += 26
		elif original >=97 and original <= 122:
			if ascii_element < 97:
				ascii_element += 26
		decrypt_message += chr(ascii_element)
	return decrypt_message

choice = input("Encrypt or decrypt?: ")
original_message = input("What is the message: ")
shift_value = int(input("The shift value: "))

if choice == "encrypt":
	txt = encryption(message=original_message, shift_number=shift_value)
elif choice == "decrypt":
	txt = decryption(message=original_message, shift_number=shift_value)

print(txt)

