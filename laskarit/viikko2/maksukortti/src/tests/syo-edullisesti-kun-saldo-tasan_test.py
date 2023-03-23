import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_konstruktori_asettaa_saldon_oikein(self):
        kortti = Maksukortti(250)
        kortti.syo_edullisesti()


        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")
