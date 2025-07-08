 Working on caesar cipher with some help from GPT


 alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



 output_text2 = ""
 last_shift_used = 0
 has_encoded_once = False

 def caesar(original_text, shift_amount, encode_or_decode):
     output_text = ""

     if encode_or_decode == "decode":
         shift_amount *= -1

     for letter in original_text:
         if letter not in alphabet:
             output_text += letter
#***** I got stuck in this part of the code due to not using index properly but GPT goes a long way when one needs clarity*********** 
         else:
             shifted_position = alphabet.index(letter) + shift_amount
             shifted_position %= len(alphabet)
             output_text += alphabet[shifted_position]
     print(f"\nHere is the  {encode_or_decode}d result: {output_text}\n")
     return output_text
#***************************************************************************************
 should_continue = True
 while should_continue:
     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or type 'last' to 'decode' the last:\n").lower()


     if direction == "last":
         if has_encoded_once:
             decode = caesar(original_text=last_encoded_message, shift_amount=last_shift_used, encode_or_decode="decode")
         else:
             print("No message has been encoded yet.\n")
         continue

     text = input("Type your message:\n").lower()
     shift = int(input("Type the shift number:\n"))

     result = caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

     if direction =="encode":
         last_encoded_message = result
         last_shift_used = shift
         has_encoded_once = True

     restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
     if restart == "no":
         should_continue = False
         print("Goodbye")
