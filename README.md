# Ristinolla

Pelin voittaa se pelaaja, jonka tarpeeksi monesta merkistä muodostuu katkeamaton suora, kun pelaajat vuorotellen laittavat merkkejänsä ruudukkoon.

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)

## Asennusohjeet

1. Aja asennuskomento:

```bash
poetry install
```

2. Aja käynnistämiskomento:

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

Voit muuttaa pelin kokoa ja/tai voittosuoran pituutta käynnistyksen yhteydessä määrittelemällä ympäristömuuttujat SIZE ja/tai LENGTH. Jos esim. haluat, että ruudukon koko on 20 x 20 ja että voittosuoran pituus on 6, aja komento:

```bash
SIZE=20 LENGTH=6 poetry run invoke start
```
