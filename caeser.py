# Coded By Mohammed Azad

import array
import string

def textToIndex(m, l):
    for i in range(0, len(l)):
        if(l[i] == m):
            return i

def encrypt(text, k, l):
    cipher = []
    for i in range(0, len(text)):
        index = textToIndex(text[i], l)
        cipherIndex = (index + int(k)) % len(l)
        cipher.append(l[cipherIndex])
    return cipher

def decrypt(cipher, k, l):
    text = []
    for i in range(0, len(cipher)):
        index = textToIndex(cipher[i], l)
        textIndex = (index - int(k)) % len(l)
        text.append(l[textIndex])
    return text

def arrayToText(arr):
    s = ""
    for i in range(0, len(arr)):
        s = s + arr[i]
    return s

cipher = []
ASCII = list(string.printable)

while True:
    print("[+] Cesar Cipher")
    k = input("[*] Enter The Secret Key OR Enter (?) to attack ---> ")
    if k == "?":
        e = input("[!] Please enter the Cipher Message: ")
        for i in range(0, len(ASCII)):
            print("[" + str(i) + "] <<KEY - DECRYPTED>> " + arrayToText(decrypt(e, i, ASCII)))
        print("[+] Hopefully the Orginal Message should be in the list above BUT NOTE *** sometimes two keys could be MEANINGFULL but switched to uppercase or lowercase ***")
        print(" ")
        continue
    if int(k) < 1 or int(k) > len(ASCII):
        print("[-] Error, Please Choose a key between 1 to " + str(len(ASCII)))
        print(" ")
        continue
    print("[*] Enter 1 for encryption, Enter 2 for decryption, q for exist")
    option = input("[*] Setting Your Choice ---> ")
    if option == "1":
        text = input("[!] Please enter your message: ")
        text = [*text]
        print("[+] The Message encrypted => " + arrayToText(encrypt(text, k, ASCII)))
    elif option == "2":
        e = input("[!] Please enter the Cipher Message: ")
        print("[+] The Cipher decrypted => " + arrayToText(decrypt(e, k, ASCII)))
    elif option == "q":
        break
    else:
        print("[-] Error, try again")
    print(" ")
