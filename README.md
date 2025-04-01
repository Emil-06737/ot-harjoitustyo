# Ristinolla

Pelin voittaa se pelaaja, jonka tarpeeksi monesta merkistä muodostuu katkeamaton suora, kun pelaajat vuorotellen laittavat merkkejänsä ruudukkoon.

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)

## Asennus

1. Asenna sovelluksen riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

Sovelluksen suorittaminen:

```bash
poetry run invoke start
```

Testaus:

```bash
poetry run invoke test
```

Testikattavuus:

```bash
poetry run invoke coverage-report
```
