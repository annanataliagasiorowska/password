import random
import string
all_signs = string.ascii_letters + string.digits + string.punctuation
print(all_signs)


password_len = int(input("How many characters should be in your password: "))
password = ''
while len(password) < password_len:
    character = random.choice(all_signs)
    password = password + character 
print(password)
    

    



