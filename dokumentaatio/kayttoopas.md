# Käyttöopas

## Asennus- ja käynnistysohjeet

1. Lataa uusin release [täältä](https://github.com/Emil-06737/ot-harjoitustyo/releases).

2. Pura tiedosto haluamaasi paikkaan.

3. Siirry projektin juurihakemistoon.

4. Aja asennuskomento:

```bash
poetry install
```

5. Aja alustuskomento:

```bash
poetry run invoke initialize
```

6. Aja käynnistämiskomento:

```bash
poetry run invoke start
```

## Pelin näppäimet

- Vasen hiirinäppäin: Aseta merkki ruudukkoon.
- F1: Näytä statistiikka.
- F2: Aloita uusi peli.

## Pelin asetusten muuttaminen

Voit muuttaa pelin kokoa ja/tai voittosuoran pituutta ja/tai pelaajamäärää käynnistyksen yhteydessä määrittelemällä ympäristömuuttujat SIZE ja/tai LENGTH ja/tai PLAYERS. Pelin koon täytyy olla 3-86, voittosuoran pituuden täytyy olla 3-10 ja pienempi tai yhtäsuuri kuin pelin koko ja pelaajamäärän täytyy olla 2-4. Jos esim. haluat, että ruudukon koko on 20 x 20 ja että voittosuoran pituus on 6 ja että pelaajia on 3, aja komento:

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
NAME_OF_DATABASE_FILE=haluamasi_nimi.sqlite
```

Tietokannan nimen muuttamisen jälkeen täytyy vielä ajaa alustuskomento uudestaan, jotta peli toimii:

```bash
poetry run invoke initialize
```
