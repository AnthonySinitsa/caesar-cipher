from caesar_cipher.corpus_loader import word_list, name_list

# Create an encrypt function that takes in a plain text phrase and a numeric shift.
# the phrase will then be shifted that many letters.
# E.g. encrypt(‘abc’,1) would return ‘bcd’. = E.g. encrypt(‘abc’, 10) would return ‘klm’.
# shifts that exceed 26 should wrap around.
# E.g. encrypt(‘abc’,27) would return ‘bcd’.
# shifts that push a letter out or range should wrap around.
# E.g. encrypt(‘zzz’,1) would return ‘aaa’.
# Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.
# create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
# Devise a method for the computer to determine if code was broken with minimal human guidance.
#have the function ignore numbers and punctuation but keep them in their original positions

def encrypt(plain_text, shift):
  print('plain text', plain_text)
  encrypted_text = ""
  for letter in plain_text:
    new_letter = letter
    if new_letter.isalpha():#if letter is a letter
        if letter.islower():
          offset = 97
        else:
          offset = 65
        new_letter = chr((ord(letter) + shift - offset) % 26 + offset)
    encrypted_text += new_letter#add letter to encrypted text
  return encrypted_text


def decrypt(encrypted_text, shift):
  return encrypt(encrypted_text, -shift)


def crack(encrypted_text):
  for shift in range(26):
    counter = 0
    unencrypted_phrase = encrypt(encrypted_text, shift)
    list_word = unencrypted_phrase.split()
    for letter in list_word:
      if letter in name_list or letter.lower() in word_list:
        counter += 1
    if (counter / len(list_word)) > .5:
        return ' '.join(list_word)
  return ''
