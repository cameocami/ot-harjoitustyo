import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.kortti.lataa_rahaa(-2500)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")
