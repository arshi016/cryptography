alphabets = " abcdefghijklmnopqrstuvwxyz"

def encrypt_casear(plaint_text, key):
    cipher_text = ''
    for i in plaint_text:
        index = (alphabets.find(i) + key) % len(alphabets)
        cipher_text = cipher_text + alphabets[index]
    return cipher_text

def decrypt_caesar(cipher_text, key):
    plaint_text = ''
    for i in cipher_text:
        index = (alphabets.find(i) - key) % len(alphabets)
        plaint_text = plaint_text + alphabets[index]
    return plaint_text

def crack_caesar(cipher_text):
    for key in range(len(alphabets)):
        plaint_text = ''
        for i in cipher_text:
            index = (alphabets.find(i) - key) % len(alphabets)
            plaint_text = plaint_text + alphabets[index]
        print("Key = ", key , "    Decrypted msg = " , plaint_text)
        
def main():
    test = "i am so good"
    test = test.lower()
    print(encrypt_casear(test, 3))
    print(crack_caesar("lcdpcvrcjrrg"))

if __name__ == '__main__':
    main()