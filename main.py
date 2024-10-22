import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase
    """
    Création de la boucle d'ajout des majuscules en uppercase, 
    chiffres (digits) et des caractères spéciaux (punctuation) 
    selon les options choisit par l'utilisateur dans le main. 
    """
    if use_uppercase:
        characters = characters + string.ascii_uppercase
    if use_digits:
        characters = characters + string.digits
    if use_special:
        characters = characters + string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def main():
    pass


main()