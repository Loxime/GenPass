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
    print("Bienvenue dans le générateur de mots de passe")

    length = int(input("Entrez la longueur du mot de passe souhaitée (minimum 8) : "))
    if length < 8 :
        print("La longueur du mot de passe doit être d'au moins 8 caractères.")
        return
    
    use_uppercase = input("Voulez-vous inclure des lettres majuscules ? (oui/non) : ").lower() == 'oui'
    use_digits = input("Voulez-vous inclure des chiffres ? (oui/non) : ").lower() == 'oui'
    use_special = input("Voulez-vous inclure des caractères spéciaux ? (oui/non) : ").lower() == 'oui'

    password = generate_password(length, use_uppercase, use_digits, use_special)
    print("\nVoici votre mot de passe généré :")
    print(password)


main()