import unittest
from main import TestUnit


class TestPassword(unittest.TestCase):
    def test_passwordValid(self):
        password = TestUnit()
        self.assertFalse(password.passwordValid("azertyuiop"), "Easy password are not allowed !")
        self.assertFalse(password.passwordValid("qwertyuiop"), "Easy password are not allowed !")
        self.assertFalse(password.passwordValid("1234567890"), "Easy password are not allowed !")
        self.assertFalse(password.passwordValid("motdepasse"), "Easy password are not allowed !")
        self.assertFalse(password.passwordValid("ejkvbejbveJB"), "Password must contain at least 1 digit and 1 special character")
        self.assertFalse(password.passwordValid("ejkvbejbveJB1"), "Password must contain at least 1 digit")
        self.assertTrue(password.passwordValid("ejkvbejbveJB1/"))
        self.assertFalse(password.passwordValid("toto"), "Password must contain at 10 characters and max 25 characters")
        self.assertEqual(password.passwordValid("ejkvbejbveJB1"), False)

if __name__ == '__main__':
    unittest.main()