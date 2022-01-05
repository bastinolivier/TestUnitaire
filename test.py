import unittest
from main import TestUnit


class TestPassword(unittest.TestCase):
    def test_passwordToSimple(self):
        password = TestUnit()
        self.assertFalse(password.passwordValid("azertyuiop@0A"), "mot de passe trop simple")
        self.assertFalse(password.passwordValid("qwertyuiop@0A"), "mot de passe trop simple")
        self.assertFalse(password.passwordValid("1234567890@0Ac"), "mot de passe trop simple")
        self.assertFalse(password.passwordValid("password@0A"), "mot de passe trop simple")

    def test_longError(self):
        password = TestUnit()
        self.assertFalse(password.passwordValid("e@B"),"mot de passe trop court")
        self.assertFalse(password.passwordValid("ejkvb@ejbveJB1sdfgxwdfggxdffgsdfgsdfg"), "mot de passe trop long")

    def test_containtCaracter(self):
        password = TestUnit()
        self.assertEqual(password.passwordValid("ejkvbejbveJB1"), False)

    def test_containtmin(self):
        password = TestUnit()
        self.assertEqual(password.passwordValid("@DFDFDFJB1"), False)

    def test_containtmaj(self):
        password = TestUnit()
        self.assertEqual(password.passwordValid("@sdhhgezd1"), False)

if __name__ == '__main__':
    unittest.main()