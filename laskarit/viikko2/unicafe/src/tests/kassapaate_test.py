import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    """
    Kassapaatteen luonti toimii oikein
    """
    def test_kassapaateen_saldo_oikein_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassapaatteen_myydyt_edulliset_lounaat_oikein_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassapaatteen_myydyt_maukkaat_lounaat_oikein_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
        

    """
    Kateisosto toimii edullisten lounaiden osalta 
    """

    def test_edullisen_lounaan_kateisosto_palautussumma_oikein(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(palautus, 260)
    
    def test_edullisen_lounaan_kateisosto_lisaa_kassan_saldoa_oikein(self): 
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullisen_lounaan_kateisosto_lisaa_myytyja_edullisia_lounaita(self): 
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisen_lounaan_kateisosto_ei_toimi_jos_maksu_liian_pieni(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullisen_lounaan_kateisosto_palautussumma_oikein_jos_maksu_liian_pieni(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(palautus, 200)
    
    def test_edullisen_lounaan_kateisosto_ei_muuta_kassan_saldoa_jos_maksu_liian_pieni(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    """
    Kateisosto toimii maukkaiden lounaiden osalta 
    """

    def test_maukkaan_lounaan_kateisosto_palautussumma_oikein(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(palautus, 100)
    
    def test_maukkaan_lounaan_kateisosto_lisaa_kassan_saldoa_oikein(self): 
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukkaan_lounaan_kateisosto_lisaa_myytyja_maukkaita_lounaita(self): 
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_lounaan_kateisosto_ei_toimi_jos_maksu_liian_pieni(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukkaan_lounaan_kateisosto_palautussumma_oikein_jos_maksu_liian_pieni(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(palautus, 200)

    def test_maukkaan_lounaan_kateisosto_ei_muuta_kassan_saldoa_jos_maksu_liian_pieni(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    """
    Korttiosto toimii edullisten lounaiden osalta
    """

    def test_edullisen_lounaan_korttiosto_toimii_jos_saldo_riittaa(self):
        metodin_arvo = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(metodin_arvo, True)

    def test_edullisen_lounaan_korttiosto_veloittaa_oikean_summan_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")

    def test_edullisen_lounaan_korttiosto_lisaa_myytyja_edullisia_lounaita(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisen_lounaan_korttiosto_ei_toimi_jos_saldo_ei_riita(self):
        kortti = Maksukortti(100)
        metodin_arvo = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(metodin_arvo, False)

    def test_edullisen_lounaan_korttiosto_ei_muuta_saldoa_jos_saldo_ei_riita(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
    
    def test_edullisen_lounaan_korttiosto_ei_lisaa_myytyja_edullisia_lounaita_jos_saldo_ei_riita(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0) 
    
    def test_edullisen_lounaan_kateisosto_ei_muuta_kassan_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    """
    Korttiosto toimii maukkauiden lounaiden osalta
    """

    def test_maukkaan_lounaan_korttiosto_toimii_jos_saldo_riittaa(self):
        metodin_arvo = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(metodin_arvo, True)

    def test_maukkaan_lounaan_korttiosto_veloittaa_oikean_summan_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")

    def test_maukkaan_lounaan_korttiosto_lisaa_myytyja_maukkaita_lounaita(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_lounaan_korttiosto_ei_toimi_jos_saldo_ei_riita(self):
        kortti = Maksukortti(100)
        metodin_arvo = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(metodin_arvo, False)

    def test_maukkaan_lounaan_korttiosto_ei_muuta_saldoa_jos_saldo_ei_riita(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
    
    def test_maukkaan_lounaan_korttiosto_ei_lisaa_myytyja_maukkaita_lounaita_jos_saldo_ei_riita(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0) 
    
    def test_maukkaan_lounaan_kateisosto_ei_muuta_kassan_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    """
    Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamaara kasvaa ladatulla summalla
    """

    def test_rahan_lataus_kortille_nostaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 250)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.50 euroa")

    def test_rahan_lataus_kortille_lisaa_kassan_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100250)
    
    def test_rahan_lataus_kortille_ei_muuta_kassan_saldoa_jos_ladattava_summa_alle_nolla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_rahan_lataus_kortille_ei_muuta_kortin_saldoa_jos_ladattava_summa_alle_nolla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
     

