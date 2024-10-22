
---

### **Documentation**

#### **1. `generate_password(length, use_uppercase=True, use_digits=True, use_special=True)`**

Génère un mot de passe aléatoire basé sur les options fournies par l'utilisateur.

- **Paramètres** :
  - `length` (int) : La longueur souhaitée du mot de passe (minimum de 6 caractères).
  - `use_uppercase` (bool) : Si `True`, inclut des lettres majuscules (défaut : `True`).
  - `use_digits` (bool) : Si `True`, inclut des chiffres (défaut : `True`).
  - `use_special` (bool) : Si `True`, inclut des caractères spéciaux (défaut : `True`).

- **Retourne** :
  - `password` (str) : Le mot de passe généré.

- **Exemple d'utilisation** :
  ```python
  password = generate_password(12, use_uppercase=True, use_digits=True, use_special=False)
  print(password)
