import unittest

#to jest commit beata prywata 3

def pole_kwadratu(bok):
    if bok <= 0: return "Bok nie może być mniejszy od zera"
    else:
        if bok > 100: return "Nie ma takich dużych kwadratów"
    return bok*bok

class MyTestCase(unittest.TestCase):

    def test_pole_kwadaratu_bok_2(self):
        self.assertEqual(pole_kwadratu(2), 4)

    def test_pole_kwadratu_bok_0(self):
        self.assertEqual(pole_kwadratu(0), "Bok nie może być mniejszy od zera")

    def test_pole_kwadratu_bok_minus_2(self):
        self.assertEqual(pole_kwadratu(-2), "Bok nie może być mniejszy od zera")

    def test_pole_kwadratu_bok_101(self):
        self.assertEqual(pole_kwadratu(110), "Nie ma takich dużych kwadratów")

    def test_pole_kwadratu_bok_110(self):
        self.assertEqual(pole_kwadratu(110), "Nie ma takich dużych kwadratów")

if __name__ == '__main__':
    unittest.main()
