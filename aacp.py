import random 
import string

def randPass(length):
    
    lowercases = string.ascii_lowercase
    uppercases = string.ascii_uppercase
    digits = string.digits
    puntuations = string.punctuation
    
    password = [random.choice(lowercases), random.choice(uppercases), random.choice(digits), random.choice(puntuations)]
    
    characters = lowercases + uppercases + digits + puntuations
    
    password = password + random.choice(characters, k = length - len(password))
    random.shuffle(password)
    
    return "".join(password)

passLength = random.randint(6, 10)
password = randPass(passLength)

print(f"Password: {password}")