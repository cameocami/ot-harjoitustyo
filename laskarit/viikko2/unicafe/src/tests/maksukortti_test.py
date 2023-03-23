import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self): # Kortin saldo alussa oikein
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_kortille_voi_ladata_rahaa(self): # Rahan lataaminen kasvattaa saldoa oikein
        self.maksukortti.lataa_rahaa(3000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 40.00 euroa")

    def test_kortilta_voi_ottaa_rahaa(self): # Rahan ottaminen toimii: Saldo vähenee oikein, jos rahaa on tarpeeksi
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_kortilta_ei_voi_ottaa_yli_saldon_rahaa(self): # Rahan ottaminen toimii: Saldo ei muutu, jos rahaa ei ole tarpeeksi
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahanottometodi_palautta_True_kun_rahat_riittavat(self): # Metodi palauttaa True, jos rahat riittivät ja muuten False
        
        self.assertTrue(self.maksukortti.ota_rahaa(500)) 
    
    def test_rahanottometodi_palautta_False_kun_rahat_eivat_riita(self): # Metodi palauttaa True, jos rahat riittivät ja muuten False
        
        self.assertFalse(self.maksukortti.ota_rahaa(5000)) 

    