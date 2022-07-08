import unittest
from empClass import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp5 = Employee("kal", 'Abs', 5000)
        self.emp6 = Employee("Sal", "Mus", 7000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp5.email, 'kal.Abs@nigga.com')
        self.assertEqual(self.emp6.email, "Sal.Mus@nigga.com")

        self.emp5.first = 'bib'
        self.emp6.first = "fat"

        self.assertEqual(self.emp5.email, "bib.Abs@nigga.com")
        self.assertEqual(self.emp6.email, "fat.Mus@nigga.com")

    def test_apply_raise(self):
        self.emp5 = Employee("kal", 'Abs', 5000)
        self.emp6 = Employee("Sal", "Mus", 7000)

        self.emp5.apply_raise()
        self.emp6.apply_raise()

        self.assertEqual(self.emp5.pay, 7500)
        self.assertEqual(self.emp6.pay, 10500)


if __name__ == "__main__":
    unittest.main()
