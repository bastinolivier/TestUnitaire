import re


class TestUnit:

    def passwordValid(self, password):
        special_characters = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        password_list = ["1234567890", "azertyuiop", "qwertyuiop", "000000", "password",
                         "12345678", "abcdef", "wxcvbn", "poiuytreza", "mlkjhgfdsq", "nbvcxw"]

        password_len = len(password)

        if password_len < 10:
            print("mot de passe trop court.")
            return False
        if password_len > 25:
            print("mot de passe trop long.")
            return False

        if not re.search(r"[\d]+", password) or not re.search(r"[A-Z]+", password) or not re.search(r"[a-z]+", password) or not any(c in special_characters for c in password):
            print("Le mot de passe doit contenir au minimum une majuscule, une minuscule, un nombre et un caractère spécial.")
            return False

        if password in password_list or any(word for word in password_list if word in password):
            print("Mot de passe trop faible.")
            return False

        else:
            print("Mot de passe valide")
            return True

password = TestUnit()
password.passwordValid("Tototatatutu@4")