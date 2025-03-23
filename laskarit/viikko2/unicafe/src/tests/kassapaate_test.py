import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassapaatteen_rahamaara_on_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_kassapaatteen_myytyjen_edullisten_lounaiden_maara_on_alussa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassapaatteen_myytyjen_maukkaiden_lounaiden_maara_on_alussa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_kateisosto_nostaa_kassapaatteen_rahamaaraa_oikein_kun_maksu_on_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)

    def test_edullisen_lounaan_kateisoston_vaihtorahan_suuruus_on_oikea_kun_maksu_on_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(1000)

        self.assertEqual(vaihtoraha, 760)

    def test_edullisen_lounaan_kateisosto_kasvattaa_myytyjen_edullisten_lounaiden_maaraa_yhdella_kun_maksu_on_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaan_lounaan_kateisosto_nostaa_kassapaatteen_rahamaaraa_oikein_kun_maksu_on_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)

    def test_maukkaan_lounaan_kateisoston_vaihtorahan_suuruus_on_oikea_kun_maksu_on_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(1000)

        self.assertEqual(vaihtoraha, 600)

    def test_maukkaan_lounaan_kateisosto_kasvattaa_myytyjen_maukkaiden_lounaiden_maaraa_yhdella_kun_maksu_on_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullisen_lounaan_kateisosto_ei_muuta_kassapaatteen_rahamaaraa_kun_maksu_ei_ole_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_edullisen_lounaan_kateisoston_vaihtorahan_suuruus_on_maksun_suuruinen_kun_maksu_ei_ole_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(vaihtoraha, 100)

    def test_edullisen_lounaan_kateisosto_ei_muuta_myytyjen_edullisten_lounaiden_maaraa_kun_maksu_ei_ole_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaan_lounaan_kateisosto_ei_muuta_kassapaatteen_rahamaaraa_kun_maksu_ei_ole_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_maukkaan_lounaan_kateisoston_vaihtorahan_suuruus_on_maksun_suuruinen_kun_maksu_ei_ole_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(vaihtoraha, 100)

    def test_maukkaan_lounaan_kateisosto_ei_muuta_myytyjen_maukkaiden_lounaiden_maaraa_kun_maksu_ei_ole_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_korttiosto_veloittaa_summan_oikein_kun_kortilla_on_tarpeeksi_rahaa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo_euroina(), 7.6)

    def test_edullisen_lounaan_korttiosto_palauttaa_True_kun_kortilla_on_tarpeeksi_rahaa(self):
        maksukortti = Maksukortti(1000)
        tulos = self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(tulos, True)

    def test_edullisen_lounaan_korttiosto_kasvattaa_myytyjen_edullisten_lounaiden_maaraa_yhdella_kun_maksu_on_riittava(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaan_lounaan_korttiosto_veloittaa_summan_oikein_kun_kortilla_on_tarpeeksi_rahaa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo_euroina(), 6)

    def test_maukkaan_lounaan_korttiosto_palauttaa_True_kun_kortilla_on_tarpeeksi_rahaa(self):
        maksukortti = Maksukortti(1000)
        tulos = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(tulos, True)

    def test_maukkaan_lounaan_korttiosto_kasvattaa_myytyjen_maukkaiden_lounaiden_maaraa_yhdella_kun_maksu_on_riittava(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullisen_lounaan_korttiosto_ei_muuta_kortin_rahamaaraa_kun_kortilla_ei_ole_tarpeeksi_rahaa(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo_euroina(), 1)

    def test_edullisen_lounaan_korttiosto_palauttaa_False_kun_kortilla_ei_ole_tarpeeksi_rahaa(self):
        maksukortti = Maksukortti(100)
        tulos = self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(tulos, False)

    def test_edullisen_lounaan_korttiosto_ei_muuta_myytyjen_edullisten_lounaiden_maaraa_kun_maksu_ei_ole_riittava(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaan_lounaan_korttiosto_ei_muuta_kortin_rahamaaraa_kun_kortilla_ei_ole_tarpeeksi_rahaa(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo_euroina(), 1)

    def test_maukkaan_lounaan_korttiosto_palauttaa_False_kun_kortilla_ei_ole_tarpeeksi_rahaa(self):
        maksukortti = Maksukortti(100)
        tulos = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(tulos, False)

    def test_maukkaan_lounaan_korttiosto_ei_muuta_myytyjen_maukkaiden_lounaiden_maaraa_kun_maksu_ei_ole_riittava(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_korttiosto_ei_muuta_kassassa_olevaa_rahamaaraa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_maukkaan_lounaan_korttiosto_ei_muuta_kassassa_olevaa_rahamaaraa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_kortille_rahaa_ladattaessa_rahamaara_kortissaa_muuttuu_oikein(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 100)

        self.assertEqual(maksukortti.saldo_euroina(), 11.0)

    def test_kortille_rahaa_ladattaessa_kassan_rahamaara_muuttuu_oikein(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 100)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1001.0)
