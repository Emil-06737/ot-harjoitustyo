import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)

    def test_kortin_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 11.00)

    def test_saldo_vahenee_oikein_kun_saldoa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 9.00)

    def test_saldo_ei_muutu_kun_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)

    def test_rahan_ottaminen_palauttaa_True_kun_rahat_riittavat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100), True)

    def test_rahan_ottaminen_palauttaa_False_kun_rahat_eivat_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100), False)
