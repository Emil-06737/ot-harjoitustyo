# Ristinolla

Pelin voittaa se pelaaja, jonka tarpeeksi monesta merkistä muodostuu katkeamaton suora, kun pelaajat vuorotellen laittavat merkkejänsä ruudukkoon.

## Dokumentaatio

- [Käyttöopas](./dokumentaatio/kayttoopas.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)
- [Testaus](./dokumentaatio/testaus.md)

## Releases

- [loppupalautus](https://github.com/Emil-06737/ot-harjoitustyo/releases/tag/loppupalautus)
- [Viikko 6](https://github.com/Emil-06737/ot-harjoitustyo/releases/tag/viikko6)
- [Viikko 5](https://github.com/Emil-06737/ot-harjoitustyo/releases/tag/viikko5)

## Asennus- ja käynnistysohjeet

Löytyy [käyttöoppaasta](./dokumentaatio/kayttoopas.md) kohdasta "Asennus- ja käynnistysohjeet".

## Komentorivikomentoja

Käynnistämiskomento:

```bash
poetry run invoke start
```

Testauskomento:

```bash
poetry run invoke test
```

Testikattavuuskomento:

```bash
poetry run invoke coverage-report
```

Koodin tyylin tarkastuskomento:

```bash
poetry run invoke lint
```