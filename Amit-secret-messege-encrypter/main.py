"""
Project: Basic String Encryptor
Author: Amit kumar
Language: Python 3.12
Description: A tool to encrypt and decrypt messages using String Slicing Logic.
"""
a=input("Enter a messege to Encrypt: ")
encrypted_msg=a[::-1] + "hgghvtgfhdfbdf fhbfhbfvnjbmfe fjhfrjibfr ghbvjbfrjkvf gtjibhgtr jhjt njtgbgtrt gtrjgjigtr gtrjbgtjnjgtj gtrjrhgigt tjbgj"
print("Encrypted messege is:",encrypted_msg)


b=input("want to decrypt the messege(yes/no): ")
if b=="yes":
    c=input("Enter the encrypted messege: ")
    if c==encrypted_msg:
        print("Correct encrypted messege")
        remove_msg=encrypted_msg[:-120]
        decrypted_msg=remove_msg[::-1]
    
        print("Your decrypted messege is :",decrypted_msg)
    else:
        print("Invalid messege")
    

    
else:
    print("Thank you for using the messege encrypter/decrypter")


