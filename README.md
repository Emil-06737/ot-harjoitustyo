# Ristinolla

Pelin voittaa se pelaaja, jonka tarpeeksi monesta merkistä muodostuu katkeamaton suora, kun pelaajat vuorotellen laittavat merkkejänsä ruudukkoon.

## Dokumentaatio

- [Käyttöopas](./dokumentaatio/kayttoopas.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)

## Release

- [Viikko 6](https://github.com/Emil-06737/ot-harjoitustyo/releases/tag/viikko6)
- [Viikko 5](https://github.com/Emil-06737/ot-harjoitustyo/releases/tag/viikko5)

## Asennusohjeet

1. Aja asennuskomento:

```bash
poetry install
```

2. Aja alustuskomento:

```bash
poetry run invoke initialize
```

3. Aja käynnistämiskomento:

```bash
poetry run invoke start
```

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

## Pelin asetusten muuttaminen

Voit muuttaa pelin kokoa ja/tai voittosuoran pituutta ja/tai pelaajamäärää käynnistyksen yhteydessä määrittelemällä ympäristömuuttujat SIZE ja/tai LENGTH ja/tai PLAYERS. Pelin koon täytyy olla 3-86, voittosuoran pituuden täytyy olla 3-10 ja pienempi kuin pelin koko ja pelaajamäärän täytyy olla 2-4. Jos esim. haluat, että ruudukon koko on 20 x 20 ja että voittosuoran pituus on 6 ja että pelaajia on 3, aja komento:

```bash
SIZE=20 LENGTH=6 PLAYERS=3 poetry run invoke start
```

Voit muuttaa oletusasetuksia luomalla .env-tiedoston projektin juurihakemistoon (hakemisto, jossa mm. .env.test sijaitsee) ja muuttamalla sen sisältöä. Jos esim. haluat, että edellä mainitut asetukset ovat oletusasetuksena, muuta .env-tiedosto seuraavanlaiseksi:

```
SIZE=20
LENGTH=6
PLAYERS=3
```

Myös tietokannan nimeä voi muuttaa muuttamalla .env-tiedoston sisältöä. Tämän muuttaminen parantaa tietoturvaa. Lisättävä rivi on seuraavaa muotoa:

```
NAME_OF_DATABASE_FILE=HALUAMASI_NIMI.sqlite
```

Tietokannan nimen muuttamisen jälkeen täytyy vielä ajaa alustuskomento uudestaan, jotta peli toimii:

```bash
poetry run invoke initialize
```
