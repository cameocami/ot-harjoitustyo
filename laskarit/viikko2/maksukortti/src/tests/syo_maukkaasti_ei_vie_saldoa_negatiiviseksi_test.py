import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        pass

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_maukkaasti()
        
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

        

