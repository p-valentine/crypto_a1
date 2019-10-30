from collections import Counter
import string

ALHPABET_LENGTH = 26

def main():
  #key = list("LEMON") #enter the key in all caps

  user_key = input("enter a key: ")
  modified_key = list(user_key.upper())

  fff = input("enter file to read from: ")
  user_input = get_text_from_file(fff)
  #user_input = input("Enter text to encrypt: ")
  #while user_input.isalpha() == False: #keep looping until the user enters only 
  #  print("Please only use alphabetical characters!!!!")
  #  user_input = input("Enter text to encrypt: ")
  user_input = user_input.upper()
  user_input_length = len(user_input)
  final_key = generate_key(modified_key, user_input_length)
  encrypted_text = encrypt(user_input, final_key)
  decrypted_text = decrypt(encrypted_text, final_key)
  print("Encrypted text: ", encrypted_text)
  print("Decrypted text: ", decrypted_text.lower())

def encrypt(user_input, key):
  encrypted_text = ""
  for i in range (len(user_input)):
    ascii_char = (ord(user_input[i]) + ord(key[i])) % 26 + ord('A')
    encrypted_text += chr(ascii_char)
  return encrypted_text
  
def decrypt(encrypted_text, key):
  decrypted_text = ""
  for i in range(len(encrypted_text)):
    ascii_char = ((ord(encrypted_text[i]) - ord(key[i])) % 26) + ord('A')
    decrypted_text += chr(ascii_char)
  return decrypted_text

def generate_key(key, length):
  if(len(key) >= length):
    return key
  else:
    for i in range (length - len(key)):
      additional_char = key[i % len(key)]
      key.append(additional_char)
  return key

def get_text_from_file(file_name):
  buffer = []
  with open(file_name, "r") as f:
    for line in f:
      n = line
      buffer.append(n)
  text = "".join(buffer)
  print(text)
  return text


if __name__ == "__main__":
  main()
