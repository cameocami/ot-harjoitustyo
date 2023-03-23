import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_konstruktori_asettaa_saldon_oikein(self):
        # alustetaan maksukortti, jossa on 10 euroa (1000 senttiä)

        kortti = Maksukortti(1000)

        self.assertEqual(str(kortti), "Kortilla on rahaa 9.00 euroa")
